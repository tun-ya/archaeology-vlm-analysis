# LLaVa Next

## Evaluation command
```bash
    cd models/llava_next_7b
    python ../../models/eval_script/bleu_score_evaluation.py results_processed_data.json
```
```
Average BLEU Score: 0.0001913632972443511
```

```bash
    cd models/llava_next_7b
    python ../../models/eval_script/metric_score_evaluation.py results_processed_data.json
```
```
Average F1 score: 0.0390
Average Precision: 0.0283
Average Recall: 0.1905
```