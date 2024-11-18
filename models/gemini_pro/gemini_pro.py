import pandas as pd
import io
import json
import os
from tqdm import tqdm
from typing import List
from PIL import Image
import shutil
# from utils import *
import google.generativeai as genai
import os
import multiprocessing as mp
import time
import random
import argparse

parser = argparse.ArgumentParser(description="Path arguments")
parser.add_argument('images_folder', type=str, help="Images folder path ex. ../../data/processed/")
parser.add_argument('dataset_path', type=str, help="Dataset file path (.json) ex. ../../data/processed/vqa_data.json")
parser.add_argument('result_path', type=str, help="Result file path (.json) ex. results.json")

# Parse the arguments
args = parser.parse_args()

folder_image_path = args.images_folder                  #   "../../data/processed/"
dataset_path = args.dataset_path                        #   "../../data/processed/vqa_data.json"
results_path = args.result_path                         #   "results.json"
with open(dataset_path, 'r') as file:
    datasets = json.load(file)

df = pd.DataFrame(datasets)

def load_image(path):
    try:
        return Image.open(path)
    except (IOError, SyntaxError):
        return None

df["image_path"] = folder_image_path + df["image"]
df["image"] = df["image_path"].apply(lambda x: load_image(x))

genai.configure(api_key="YOUR-KEY")
model = genai.GenerativeModel("gemini-1.5-pro")

byte_io = io.BytesIO()

def handle_images1(row: pd.Series) -> List[str]:
    row["image"].save(byte_io, format='JPEG')
    img_bytes = byte_io.getvalue()
    return [img_bytes]

def save_images(images: List[str], worker_id, with_resize: bool = True):
    for i, image in enumerate(images):
        if image is None: continue
        with open(f"temp/gem-pro/image_{worker_id}_{i}.jpg", "wb") as f:
            f.write(image)

        if with_resize:
            img = Image.open(f"temp/gem-pro/image_{worker_id}_{i}.jpg")
            width, height = img.size
            new_width = 512 if width > height else int((512 / height) * width)
            new_height = int((512 / width) * height) if width > height else 512
            img = img.resize((new_width, new_height))
            img = img.convert("RGB")
            img.save(f"temp/gem-pro/image_{worker_id}_{i}.jpg", format="JPEG")

def generate(prompt: str, images: List[str], worker_id)-> str:
    save_images(images, worker_id)
    images = [Image.open(f"temp/gem-pro/image_{worker_id}_{i}.jpg") for i in range(len(images))]
    response = model.generate_content([prompt, *images])
    return response.text
        
    
answer_field = "answer"
def process_row(args):
    i, row, fn, fn_images = args
    worker_id = mp.current_process().pid
    d = {}
    max_retries = 5
    retry_count = 0
    er = None

    while retry_count < max_retries:
        try:
            d['index'] = i
            images = fn_images(row)
            d['pred_answer'] = generate(row["question"], images, worker_id)
            d['answer'] = str(row[answer_field])
            d['question'] = row["question"]
            return d
        except Exception as e:
            er = str(e)
            if "Quota exceeded" in er:
                retry_count += 1
                wait_time = 30 + random.uniform(0, 10)  # Add random jitter to avoid collision
                print(f"Quota exceeded. Retrying in {wait_time:.2f} seconds... (Attempt {retry_count}/{max_retries})")
                time.sleep(wait_time)
            else:
                print(f"Error processing row {i}: {e}")
                break  # Exit if the error is not quota-related
    print(f"Failed to process row {i} after {max_retries} attempts due to: {er}")
    return None

def process_dataset(name, df, fn, fn_images):
    pool = mp.Pool(processes=mp.cpu_count())
    results = list(tqdm(
        pool.imap(process_row, [(i, row, fn, fn_images) for i, row in df.iterrows()]),
        total=len(df),
        desc=f"Processing {name}"
    ))
    pool.close()
    pool.join()
    return [r for r in results if r is not None]

def mtvqa_doc_to_text():
    pass

name_to_processor = {
    "mtvqa": mtvqa_doc_to_text, # signle sentence
}
name_to_handle_type = {
    "mtvqa": handle_images1,
}
names = list(name_to_processor.keys())
os.makedirs("results", exist_ok=True)
os.makedirs("temp", exist_ok=True)
os.makedirs("temp/gem-pro", exist_ok=True)

for name in tqdm(names):
    print(f"Evaluating {name} dataset")
    fn = name_to_processor[name]
    fn_images = name_to_handle_type[name]
    results = []
    results = process_dataset(name, df, fn, fn_images)

    report = [r for r in results if r is not None]
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
