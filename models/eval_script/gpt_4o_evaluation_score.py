import json
import argparse
import numpy as np

parser = argparse.ArgumentParser(description="Result file path argument")
parser.add_argument('eval_output_path', type=str, help="Evaluation output file path (.json)")

# Parse the arguments
args = parser.parse_args()

eval_file_path = args.eval_output_path
with open(eval_file_path, 'r') as file:
    result = json.load(file)

ratings = []
for t in result:
    try:
        text = t["output"]
        rating = int(text.split("Rating:")[1].split("\n")[0].strip())  # Split by "Rating:" and then by newline
        ratings.append(rating)
    except:
        pass

average = np.mean(ratings)/10.0
print(f"Average GTP-4o Rating: {average:.4f}")