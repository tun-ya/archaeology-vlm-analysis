import re
import numpy as np
import argparse
import json

def preprocess_answer(answer):
    """
    Preprocess the answer by converting to lowercase and tokenizing it into words.
    """
    # Convert to lowercase to ensure case-insensitivity
    answer = answer.lower()
    # Tokenize the answer into words, keeping only alphabetic words
    words = re.findall(r'\b\w+\b', answer)
    return set(words)  # Using a set to avoid duplicate words

def compute_metrics(predictions, ground_truths):
    """
    Compute the F1 score, precision, and recall for a VQA task based on token overlap.
    
    Args:
    - predictions (list of str): Predicted answers from the VQA model
    - ground_truths (list of str): Corresponding ground truth answers
    
    Returns:
    - results: F1 scores, precision, and recall
    """
    all_pred_words = []
    all_gt_words = []
    
    for pred, gt in zip(predictions, ground_truths):
        # Preprocess answers
        pred_words = preprocess_answer(pred)
        gt_words = preprocess_answer(gt)
        
        # Store words for F1 score calculation
        all_pred_words.append(pred_words)
        all_gt_words.append(gt_words)
    
    # Calculate precision and recall for each prediction
    f1_scores = []
    precision_scores = []
    recall_scores = []
    for pred_words, gt_words in zip(all_pred_words, all_gt_words):
        # Find the intersection of predicted words and ground truth words
        true_positives = len(pred_words & gt_words)
        precision = true_positives / len(pred_words) if len(pred_words) > 0 else 0
        recall = true_positives / len(gt_words) if len(gt_words) > 0 else 0
        
        # Compute F1 score for this instance
        if precision + recall > 0:
            f1 = 2 * (precision * recall) / (precision + recall)
        else:
            f1 = 0
        
        f1_scores.append(f1)
        precision_scores.append(precision)
        recall_scores.append(recall)
    
    # Return the average F1 score, precision, and recall
    return np.mean(f1_scores), np.mean(precision_scores), np.mean(recall_scores)

def evaluate_on_multiple(data):
    """
    Evaluate on multiple data points and return the average score.
    
    :param data: A list of tuples, where each tuple contains a predicted answer and ground truth answer.
    :return: The average score across all data points.
    """
    f1_total_score = 0
    precision_total_score = 0
    recall_total_score = 0

    for item in result:
        prediction = item['pred_answer']
        ground_truth = item['answer']
        f1_score, precision_score, recall_score  = compute_metrics([prediction], [ground_truth])
        f1_total_score += f1_score
        precision_total_score += precision_score
        recall_total_score += recall_score
    
    # Compute the average score
    f1_average_score = f1_total_score / len(data) if data else 0
    precision_average_score = precision_total_score / len(data) if data else 0
    recall_average_score = recall_total_score / len(data) if data else 0

    return f1_average_score, precision_average_score, recall_average_score


parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('path', type=str, help="Result file path (.json)")

# Parse the arguments
args = parser.parse_args()

result_file_path = args.path
with open(result_file_path, 'r') as file:
    result = json.load(file)

# Evaluate score across multiple data points
average_f1, average_precision, average_recall = evaluate_on_multiple(result)

print(f"Average F1 score: {average_f1:.4f}")
print(f"Average Precision: {average_precision:.4f}")
print(f"Average Recall: {average_recall:.4f}")
