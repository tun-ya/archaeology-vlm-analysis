import re
import argparse
import json

def preprocess_answer(answer):
    """
    Preprocess the answer by converting to lowercase and tokenizing it into words.
    Also removes any non-alphabetic characters (optional).
    """
    # Convert to lowercase and remove any non-alphabetic characters
    answer = answer.lower()
    answer = re.sub(r'[^a-z\s]', '', answer)
    # Tokenize the answer into words
    return set(answer.split())

def evaluate_vqa(predictions, ground_truths):
    """
    Evaluate VQA by checking if the predicted answers contain any words from the ground truth answers.
    
    Args:
    - predictions (list of str): Predicted answers from the VQA model
    - ground_truths (list of str): Corresponding ground truth answers
    
    Returns:
    - correct_count (int): The number of correct predictions (where any word overlaps)
    """
    correct_count = 0
    
    for pred, gt in zip(predictions, ground_truths):
        # Preprocess answers
        pred_words = preprocess_answer(pred)
        gt_words = preprocess_answer(gt)
        
        # Check if there's any intersection of words
        if pred_words & gt_words:  # '&' finds intersection of sets
            correct_count += 1
    
    return correct_count

def evaluate_on_multiple(data):
    """
    Evaluate on multiple data points and return the average score.
    
    :param data: A list of tuples, where each tuple contains a predicted answer and ground truth answer.
    :return: The average score across all data points.
    """
    total_score = 0
    for item in result:
        prediction = item['pred_answer']
        ground_truth = item['answer']
        score = evaluate_vqa(prediction, ground_truth)
        total_score += score
    
    # Compute the average score
    average_score = total_score / len(data) if data else 0
    return average_score


parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('path', type=str, help="Result file path (.json)")

# Parse the arguments
args = parser.parse_args()

result_file_path = args.path
with open(result_file_path, 'r') as file:
    result = json.load(file)

# Evaluate score across multiple data points
average = evaluate_on_multiple(result)

print(f"Average word count: {average}")
