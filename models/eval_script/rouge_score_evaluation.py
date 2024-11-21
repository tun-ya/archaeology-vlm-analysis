import json
import argparse
from rouge_score import rouge_scorer

# Example reference (ground truth) and hypothesis (generated text)
reference = "The quick brown fox jumps over the lazy dog."
hypothesis = "A fast brown fox jumped over a lazy dog."

# Initialize the ROUGE scorer
scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)


def calculate_rouge1_score(prediction, ground_truth):
    """
    Calculate the ROUGE_1 score between predicted and ground-truth answers.

    :param prediction: The predicted answer string.
    :param ground_truth: The ground truth (reference) answer string.
    :return: ROUGE_1 score : precision, recall, fmeasure (floats between 0 and 1)
    """
    
    # Compute the ROUGE scores
    scores = scorer.score(ground_truth, prediction)
    for _, score in scores.items():
        precision = score.precision
        recall = score.recall
        fmeasure = score.fmeasure

    return precision, recall, fmeasure

def evaluate_rouge1_on_multiple(data):
    """
    Evaluate ROUGE score on multiple data points and return the average score.
    
    :param data: A list of tuples, where each tuple contains a predicted answer and ground truth answer.
    :return: The average ROUGE score across all data points.
    """
    f_total_score = 0
    precision_total_score = 0
    recall_total_score = 0

    for item in result:
        prediction = item['pred_answer']
        ground_truth = item['answer']
        precision_score, recall_score, f_score = calculate_rouge1_score(prediction, ground_truth)
        f_total_score += f_score
        precision_total_score += precision_score
        recall_total_score += recall_score
    
    # Compute the average BLEU score
    f_average_score = f_total_score / len(data) if data else 0
    precision_average_score = precision_total_score / len(data) if data else 0
    recall_average_score = recall_total_score / len(data) if data else 0

    return f_average_score, precision_average_score, recall_average_score


parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('path', type=str, help="Result file path (.json)")

# Parse the arguments
args = parser.parse_args()

result_file_path = args.path
with open(result_file_path, 'r') as file:
    result = json.load(file)

# Evaluate score across multiple data points
average_f, average_precision, average_recall = evaluate_rouge1_on_multiple(result)

print(f"Average ROUGE_1 F-measure score: {average_f:.4f}")
print(f"Average ROUGE_1 Precision: {average_precision:.4f}")
print(f"Average ROUGE_1 Recall: {average_recall:.4f}")

