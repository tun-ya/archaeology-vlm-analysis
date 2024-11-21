import json
import argparse
import numpy as np
from rouge_score import rouge_scorer

# Initialize the ROUGE scorer
scorer = rouge_scorer.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)

def calculate_rouge_score(prediction, ground_truth):
    """
    Calculate the ROUGE_1 score between predicted and ground-truth answers.

    :param prediction: The predicted answer string.
    :param ground_truth: The ground truth (reference) answer string.
    :return: ROUGE score : precision, recall, fmeasure (floats between 0 and 1)
    """
    
    # Compute the ROUGE scores
    scores = scorer.score(ground_truth, prediction)
    return scores

def evaluate_rouge_on_multiple(data):
    """
    Evaluate ROUGE score on multiple data points and return the average score.
    
    :param data: A list of tuples, where each tuple contains a predicted answer and ground truth answer.
    :return: The average ROUGE score across all data points.
    """
    rouge_scores = []
    for item in result:
        prediction = item['pred_answer']
        ground_truth = item['answer']
        scores = calculate_rouge_score(prediction, ground_truth)
        rouge_scores.append(scores)
    
    return rouge_scores


parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('path', type=str, help="Result file path (.json)")

# Parse the arguments
args = parser.parse_args()

result_file_path = args.path
with open(result_file_path, 'r') as file:
    result = json.load(file)

# Evaluate score across multiple data points
rouge_scores = evaluate_rouge_on_multiple(result)
average_f_rouge = {metric: np.mean([score[metric].fmeasure for score in rouge_scores]) for metric in rouge_scores[0].keys()}
average_precision_rouge = {metric: np.mean([score[metric].precision for score in rouge_scores]) for metric in rouge_scores[0].keys()}
average_recall_rouge = {metric: np.mean([score[metric].recall for score in rouge_scores]) for metric in rouge_scores[0].keys()}


# Print average ROUGE scores
print("Average ROUGE scores:")
for metric, avg_score in average_f_rouge.items():
    print(f"{metric} F-measure: {avg_score:.4f}")
for metric, avg_score in average_precision_rouge.items():
    print(f"{metric} Precision: {avg_score:.4f}")
for metric, avg_score in average_recall_rouge.items():
    print(f"{metric} Recall: {avg_score:.4f}")

