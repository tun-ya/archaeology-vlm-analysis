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
import argparse

parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('result_path', type=str, help="Result file path (.json)")
parser.add_argument('eval_output_path', type=str, help="Evaluation output file path (.json)")

# Parse the arguments
args = parser.parse_args()

eval_file_path = args.eval_output_path
result_file_path = args.result_path
with open(result_file_path, 'r') as file:
    result = json.load(file)

df = pd.DataFrame(result)

client = OpenAI(
    api_key="YOUR-KEY"
)

model_name = "gpt-4o"


class QAQuestion(BaseModel):
    question: str


class QAAnswer(BaseModel):
    answer: str = ""

def generate(text: str) -> QAAnswer:
    vqa_question = QAQuestion(question=text)

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
                    "text": f"I will provide a generated response and a ground truth text. Please compare the two and give a rating from 0 to 10, where 0 is completely incorrect and 10 is perfect. Explain why you gave this rating, and describe any differences between the generated response and the ground truth text.:\n\n{vqa_question.question} Begin your answer with Rating:(number)",
                },
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
                    "name": "answer_qa_question",
                    "description": "Provide an answer to the Visual Question Answering task",
                    "parameters": QAAnswer.model_json_schema(),
                },
            }
        ],
        tool_choice={"type": "function", "function": {"name": "answer_qa_question"}},
    )

    vqa_answer = QAAnswer.model_validate_json(
        completion.choices[0].message.tool_calls[0].function.arguments
    )
    # print(vqa_answer)
    return vqa_answer


def process_row(args):
    i, row, fn = args
    d = {}
    try:
        d["index"] = i
        d["pred_answer"] = row["pred_answer"]
        d["answer"] = row["answer"]
        d["question"] = row["question"]
        input_question = "Generated Response:" + row["pred_answer"] + "\n\nGround Truth:" + row["answer"]
        d["output"] = generate(input_question).answer
        return d
    except Exception as e:
        print("Error", e)

def process_dataset(name, df, fn):
    pool = mp.Pool(processes=mp.cpu_count())
    results = list(
        tqdm(
            pool.imap(
                process_row, [(i, row, fn) for i, row in df.iterrows()]
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
    "qa": mtvqa_doc_to_text, # signle sentence
}
names = list(name_to_processor.keys())

for name in tqdm(names):
    print(f"Evaluating {name} dataset")
    fn = name_to_processor[name]

    start = 0
    stop = 100    
    for i in range(1000):
        if stop > df.shape[0]:
            results = process_dataset(name, df[start:], fn)

            report = [r for r in results if r is not None]
            with open(eval_file_path, "a", encoding="utf-8") as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            break
        else:
            results = process_dataset(name, df[start:stop], fn)

            report = [r for r in results if r is not None]
            with open(eval_file_path, "a", encoding="utf-8") as f:
                json.dump(report, f, ensure_ascii=False, indent=2)
            start = stop
            stop += 100
