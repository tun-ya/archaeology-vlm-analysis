import csv
import json

# Function to generate a simple question for VQA
def generate_question_and_answer1(row):
    # Example questions based on the object's materials
    materials = row['Materials']
    
    question = f"What is this object made of?"
    answer = materials  # Answer is the material mentioned in the row

    # You could create other question types depending on your needs
    # For now, returning one simple question-answer pair
    return {
        "image": row['image_path'],
        "question": question,
        "answer": answer
    }

def generate_question_and_answer2(row):
    # Example questions based on the object's culture
    culture = row['Culture']
    
    question = f"What is this object's culture?"
    answer = culture  # Answer is the culture mentioned in the row

    # Returning one simple question-answer pair
    return {
        "image": row['image_path'],
        "question": question,
        "answer": answer
    }

def generate_question_and_answer3(row):
    # Example questions based on the object's description
    description = row['Description']
    
    # Questions could be about the object, its culture, or materials
    question = f"Describe this image"
    answer = description  # Answer is the material mentioned in the row

    # You could create other question types depending on your needs
    # For now, returning one simple question-answer pair
    return {
        "image": row['image_path'],
        "question": question,
        "answer": answer
    }

# Read CSV and convert to VQA format
def create_vqa_format(csv_file, output_json_file):
    vqa_data = []
    
    with open(csv_file, mode='r') as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            vqa_entry = generate_question_and_answer1(row)
            vqa_data.append(vqa_entry)
            vqa_entry = generate_question_and_answer2(row)
            vqa_data.append(vqa_entry)
            vqa_entry = generate_question_and_answer3(row)
            vqa_data.append(vqa_entry)
    
    # Write the output to a JSON file
    with open(output_json_file, mode='w') as outfile:
        json.dump(vqa_data, outfile, indent=4)

# Specify the input CSV and output JSON file paths
input_csv = 'processed_data.csv'  # Replace with your actual CSV file path
output_json = 'vqa_data.json'  # Output VQA formatted JSON file

create_vqa_format(input_csv, output_json)