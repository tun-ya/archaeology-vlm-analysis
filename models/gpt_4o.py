import pandas as pd
import json
from tqdm import tqdm
from pydantic import BaseModel
from openai import OpenAI
import multiprocessing as mp
import base64
from typing import List
import json
import os
# from utils import *
import base64
from PIL import Image
import io


folder_image_path = "../../data/processed/"
dataset_path = "../../data/processed/vqa_data.json"
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

client = OpenAI(
    api_key="YOUR-KEY"
)

model_name = "gpt-4o"

byte_io = io.BytesIO()

def handle_images1(row: pd.Series) -> List[str]:
    row["image"].save(byte_io, format='JPEG')
    img_bytes = byte_io.getvalue()
    return [img_bytes]


class VQAQuestion(BaseModel):
    question: str


class VQAAnswer(BaseModel):
    answer: str = ""

def generate(text: str, images: List[str]) -> VQAAnswer:
    vqa_question = VQAQuestion(question=text)
    base64_images = [
        base64.b64encode(image).decode("utf-8") for image in images if image is not None
    ]
    images_content = [
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
        }
        for base64_image in base64_images
    ]

    messages = [
        {
            "role": "system",
            "content": """You are an advanced AI assistant specialized in Visual Question Answering (VQA). Your task is to analyze the given image and answer the provided question accurately and comprehensively. Consider all visual elements, including objects, colors, text, and spatial relationships within the image. Provide clear, concise, and relevant answers based on the visual information.""",
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"Please answer the following question based on the provided image:\n\n{vqa_question.question}",
                },
                *images_content,
            ],
        },
    ]
    
    completion = client.chat.completions.create(
        model=model_name,
        messages=messages,
        max_tokens=4000,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "answer_vqa_question",
                    "description": "Provide an answer to the Visual Question Answering task",
                    "parameters": VQAAnswer.model_json_schema(),
                },
            }
        ],
        tool_choice={"type": "function", "function": {"name": "answer_vqa_question"}},
    )

    vqa_answer = VQAAnswer.model_validate_json(
        completion.choices[0].message.tool_calls[0].function.arguments
    )
    print(vqa_answer)
    return vqa_answer


def process_row(args):
    i, row, fn, fn_images = args
    d = {}
    try:
        d["index"] = i
        images = fn_images(row)
        d["pred_answer"] = generate(row["question"], images).answer
        d["answer"] = str(row["answer"])
        d["question"] = row["question"]
        return d
    except Exception as e:
        print("Error", e)

def process_dataset(name, df, fn, fn_images):
    pool = mp.Pool(processes=mp.cpu_count())
    results = list(
        tqdm(
            pool.imap(
                process_row, [(i, row, fn, fn_images) for i, row in df.iterrows()]
            ),
            total=len(df),
            desc=f"Processing {name}",
        )
    )
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
    results = process_dataset(name, df, fn, fn_images)

    report = [r for r in results if r is not None]
    with open("../eval_script/results.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
