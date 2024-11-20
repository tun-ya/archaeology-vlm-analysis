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
#### GPT-4o
```bash
    python eval_script/gpt_4o_evaluation.py results_demo.json demo_gpt_evaluation.json
    python eval_script/gpt_4o_evaluation_score.py demo_gpt_evaluation.json
```


## Evaluation metrics on processed dataset

|  Models  | Evaluation Metrics       |    Score    |     Score (%)    |
|----------|--------------------------|-------------|-------------|
|**Gemini-Pro**| BLEU                     |   0.0000614  | 0.00614 |
|          | F1                       |  0.0244   | 2.44 |
|          | Precision                |  0.0166   |  1.66 |
|          | Recall                   |  0.0996   |  9.96 |
||
|**GPT-4o**| BLEU                     |   0.0001236  | 0.01236 |
|          | F1                       |  0.0410   | 4.10 |
|          | Precision                |  0.0304   |  3.04 |
|          | Recall                   |  0.1214   |  12.14 |
||
|**LLaVa-NeXT**| BLEU                     |   0.0001914  | 0.01914 |
|          | F1                       |  0.0390   | 3.90 |
|          | Precision                |  0.0283   | 2.83 |
|          | Recall                   |  0.1905   | 19.05 |

## GPT-4o evaluation on processed dataset
|  Models  |    Score    |     Score (%)    |
|----------|-------------|-------------|
|**Gemini-Pro**|  0.3385  | 33.85 |
|**GPT-4o**|  0.3745  | 37.45 |
|**LLaVa-NeXT**|  0.4763  | 47.63 |
|**Qwen2-VL**|     |  |

### Example evaluation output
```json
[
  {
    "index": 12,
    "pred_answer": "This object appears to be made of clay or ceramic.",
    "answer": "Ceramic",
    "question": "What is this object made of?",
    "output": "Rating: 9\n\nExplanation: The generated response \"This object appears to be made of clay or ceramic\" closely matches the ground truth \"Ceramic.\" Both responses identify ceramic as the material, which is correct. However, the generated response introduces uncertainty by saying \"appears to be made of\" and includes \"clay,\" which is not part of the ground truth. These additions slightly differentiate it from the succinct and certain nature of the ground truth text."
  },
  {
    "index": 13,
    "pred_answer": "The object appears to be pre-Columbian, possibly from the Mesoamerican region, such as Mayan or Aztec culture, due to its intricate carvings and style.",
    "answer": "Lowland Maya",
    "question": "What is this object's culture?",
    "output": "Rating: 8\n\nExplanation: The generated response and the ground truth text both indicate a connection to the Maya culture. The generated response suggests the object is possibly Mayan or Aztec from the Mesoamerican region, while the ground truth specifies \"Lowland Maya.\" The generated response is broader and includes \"possibly\" and \"Aztec,\" which is not mentioned in the ground truth. However, it correctly identifies the intricate carvings and style indicative of pre-Columbian Mesoamerican artifacts. The main difference is the generated response's broader scope, including the Aztec culture, which slightly diverges from the specific Maya identification."
  },
  {
    "index": 14,
    "pred_answer": "The image shows a terracotta vase with decorative engravings. It is an earthy reddish-brown color and has a detailed pattern etched on its surface, including swirling designs, which may depict intricate motifs or symbols. The vase is narrow towards the top, with a slightly flared base.",
    "answer": "Mold-made vessel with scene showing mirrored images of the ruler of the Maya Underworld.",
    "question": "Describe this image",
    "output": "Rating: 3\n\nExplanation:\n\n- Differences in Description:\n  The generated response describes a \"terracotta vase with decorative engravings\" and highlights its \"earthy reddish-brown color,\" \"detailed pattern,\" and \"swirling designs.\" It emphasizes the shape of the vase, mentioning a \"narrow top\" and \"slightly flared base.\" However, it lacks specific cultural or contextual information.\n\n- Ground Truth Specificity:\n  The ground truth text is more specific, identifying the object as a \"mold-made vessel\" featuring \"mirrored images of the ruler of the Maya Underworld.\" This provides clear historical and cultural context, which is entirely missing from the generated response.\n\n- Overall Assessment:\n  The generated response is somewhat relevant as it correctly identifies a vase-like object with a decorative aspect, but misses the essential cultural significance and specific details provided in the ground truth. The differences in focus and the absence of the historical context result in a low rating."
  }
]
```