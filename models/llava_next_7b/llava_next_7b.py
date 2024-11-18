from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration, AutoTokenizer
import torch
import json
import copy
from tqdm import tqdm
from PIL import Image
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

processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf")

model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf", torch_dtype=torch.float16, low_cpu_mem_usage=True) 
model.to("cuda:0")

outputs = copy.deepcopy(datasets)
for i in tqdm(range(len(outputs))):
    try:
        image = Image.open(folder_image_path + outputs[i]["image"])
    except (IOError, SyntaxError):
        continue
    conversation = [
        {
        "role": "user",
        "content": [
            {"type": "text", "text": outputs[i]["question"]},
            {"type": "image"},
            ],
        },
    ]
    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    inputs = processor(images=image, text=prompt, return_tensors="pt").to("cuda:0")

    output = model.generate(**inputs, max_new_tokens=100)
    pred_answer = processor.decode(output[0], skip_special_tokens=True)
    parts = pred_answer.split("[/INST]", 1)
    outputs[i]["pred_answer"] = parts[1].strip() if len(parts) > 1 else pred_answer

with open(results_path, 'w') as file:
    json.dump(outputs, file, indent=4)  

print(f"Data has been saved to result.json")