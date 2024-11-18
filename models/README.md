# Model Evaluation

## Model inference
```bash
    python gemini_pro/gemini_pro.py ../demo/data/ ../demo/data/vqa_data.json gemini_pro/results_demo.json
```

## Model evaluation
### BLEU (Bilingual Evaluation Understudy)
```bash
    python eval_script/bleu_score_evaluation.py gemini_pro/results_demo.json
```
### F1, Precesion and Recall
```bash
    python eval_script/metric_score_evaluation.py gemini_pro/results_demo.json
```
