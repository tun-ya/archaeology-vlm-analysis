# Model Evaluation

## Example command
### 1. Model inference
```bash
    python gemini_pro/gemini_pro.py ../demo/data/ ../demo/data/vqa_data.json gemini_pro/results_demo.json
```

### 2. Model evaluation
#### BLEU (Bilingual Evaluation Understudy)
```bash
    python eval_script/bleu_score_evaluation.py gemini_pro/results_demo.json
```
#### F1, Precesion and Recall
```bash
    python eval_script/metric_score_evaluation.py gemini_pro/results_demo.json
```

## Evaluation on processed data

|  Models  | Evaluation Metrics       |    Score    |     Score (%)    |
|----------|--------------------------|-------------|-------------|
|**Gemini Pro**| BLEU                     |   0.0000614  | 0.00614 |
|          | F1                       |  0.0244   | 2.44 |
|          | Precision                |  0.0166   |  1.66 |
|          | Recall                   |  0.0996   |  9.96 |
||
|**LLaVa Next**| BLEU                     |   0.0001914  | 0.01914 |
|          | F1                       |  0.0390   | 3.90 |
|          | Precision                |  0.0283   | 2.83 |
|          | Recall                   |  0.1905   | 19.05 |
