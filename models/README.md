# archaeology-vlm-analysis


```bash
    python gemini_pro/gemini_pro.py ../demo/ ../demo/vqa_data.json gemini_pro/results_demo.json
```

```bash
    python eval_script/bleu_score_evaluation.py gemini_pro/results_demo.json
```

```bash
    python eval_script/word_count_evaluation.py gemini_pro/results_demo.json
```