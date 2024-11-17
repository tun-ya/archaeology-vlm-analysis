from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration, AutoTokenizer
import torch
import json
import copy
from tqdm import tqdm
from PIL import Image

processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf")

model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf", torch_dtype=torch.float16, low_cpu_mem_usage=True) 
model.to("cuda:0")

folder_image_path = "../Dataset"
dataset_path = "../Dataset/datasets.json"
with open(dataset_path, 'r') as file:
    datasets = json.load(file)

outputs = copy.deepcopy(datasets)
for i in tqdm(range(len(outputs))):
    try:
        image = Image.open(folder_image_path + outputs[i]["image_path"].replace('\\', '/'))
    except (IOError, SyntaxError):
        continue
    conversation = [
        {
        "role": "user",
        "content": [
            # {"type": "text", "text": outputs[i]["question"]},
            {"type": "text", "text": "Describe this image."},
            {"type": "image"},
            ],
        },
    ]
    prompt = processor.apply_chat_template(conversation, add_generation_prompt=True)
    inputs = processor(images=image, text=prompt, return_tensors="pt").to("cuda:0")

    output = model.generate(**inputs, max_new_tokens=100)
    pred_answer = processor.decode(output[0], skip_special_tokens=True)
    parts = pred_answer.split("[/INST]", 1)
    outputs[i]["answer"] = parts[1].strip() if len(parts) > 1 else pred_answer

with open('result.json', 'w') as file:
    json.dump(outputs, file, indent=4)  

print(f"Data has been saved to result.json")