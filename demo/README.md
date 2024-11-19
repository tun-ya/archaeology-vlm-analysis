# Evaluation on demo dataset

## Example command
```bash
    cd demo/gemini_pro
    python ../../models/eval_script/bleu_score_evaluation.py results_demo.json
```
```
Average BLEU Score: 0.0
```

```bash
    cd demo/gemini_pro
    python ../../models/eval_script/metric_score_evaluation.py results_demo.json
```

```
Average F1 score: 0.0288
Average Precision: 0.0152
Average Recall: 0.4167
```

## Evaluation on demo dataset
|  Models  | Evaluation Metrics       |    Score    |     Score (%)    |
|----------|--------------------------|-------------|-------------|
|**Gemini Pro**| BLEU                     |   0.0  | 0.0 |
|          | F1                       |  0.0288   | 2.88 |
|          | Precision                |  0.0152   |  1.52 |
|          | Recall                   |  0.4167  |  41.67 |
||
|**GPT 4o**| BLEU                     |   0.0  | 0.0 |
|          | F1                       |  0.0270   | 2.70 |
|          | Precision                |  0.0152   | 1.52 |
|          | Recall                   |  0.1250   | 12.50 |
||
|**LLaVa Next**| BLEU                     |   0.0  | 0.0 |
|          | F1                       |  0.0323   | 3.23 |
|          | Precision                |  0.0185   | 1.85 |
|          | Recall                   |  0.1250   | 12.50 |
||
|**Qwen2 VL**| BLEU                     |   0.0  | 0.0 |
|          | F1                       |  0.0405   | 4.05 |
|          | Precision                |  0.0219   | 2.19 |
|          | Recall                   |  0.4583   | 45.83 |