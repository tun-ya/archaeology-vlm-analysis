import json
import evaluate
import argparse

bleu = evaluate.load("bleu")

def calculate_bleu_score(prediction, ground_truth):
    """
    Calculate the BLEU score between predicted and ground-truth answers.

    :param prediction: The predicted answer string.
    :param ground_truth: The ground truth (reference) answer string.
    :return: BLEU score (a float between 0 and 1)
    """
    
    bleu_score = bleu.compute(predictions=[prediction], references=[ground_truth])['bleu']
    
    return bleu_score

def evaluate_bleu_on_multiple(data):
    """
    Evaluate BLEU score on multiple data points and return the average score.
    
    :param data: A list of tuples, where each tuple contains a predicted answer and ground truth answer.
    :return: The average BLEU score across all data points.
    """
    total_bleu_score = 0
    for item in result:
        prediction = item['pred_answer']
        ground_truth = item['answer']
        bleu_score = calculate_bleu_score(prediction, ground_truth)
        total_bleu_score += bleu_score
    
    # Compute the average BLEU score
    average_bleu_score = total_bleu_score / len(data) if data else 0
    return average_bleu_score


parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('path', type=str, help="Result file path (.json)")

# Parse the arguments
args = parser.parse_args()

result_file_path = args.path
with open(result_file_path, 'r') as file:
    result = json.load(file)

# Evaluate BLEU score across multiple data points
average_bleu = evaluate_bleu_on_multiple(result)

print(f"Average BLEU Score: {average_bleu}")