# Evaluation on demo dataset

## Example command
### BLEU (Bilingual Evaluation Understudy)
```bash
    cd demo/gemini_pro
    python ../../models/eval_script/bleu_score_evaluation.py results_demo.json
```
```
Average BLEU Score: 0.0
```
### F1, Precesion and Recall
```bash
    cd demo/gemini_pro
    python ../../models/eval_script/metric_score_evaluation.py results_demo.json
```

```
Average F1 score: 0.0288
Average Precision: 0.0152
Average Recall: 0.4167
```

### GPT-4o
```bash
    cd demo/gemini_pro
    python ../../models/eval_script/gpt_4o_evaluation_score.py demo_gpt_evaluation.json
```

```
Average GTP-4o Rating: 0.6000
```

## Evaluation metrics on demo dataset
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

## GPT-4o evaluation on demo dataset
|  Models  |    Score    |     Score (%)    |
|----------|-------------|-------------|
|**Gemini Pro**|   0.6000  | 60.00 |
|**GPT 4o**|   0.3667  | 36.67 |
|**LLaVa Next**|   0.5333  | 53.33 |
|**Qwen2 VL**|   0.6333  | 63.33 |

### Example evaluation output
```json
[
  {
    "index": 0,
    "pred_answer": "The object appears to be made of wood.",
    "answer": "Ceramic",
    "question": "What is this object made of?",
    "output": "Rating: 3\n\nThe generated response describes the object as made of wood, while the ground truth indicates it is ceramic. These are distinctly different materials, with ceramic being a non-metallic, often clay-based material that is hardened by heat, and wood being a natural, fibrous material derived from trees. Although both materials can have similar uses, such as in decorative items, they have very different appearances and properties. The generated response fails to accurately identify the material based on the ground truth, resulting in a rating closer to zero, but it still makes a plausible guess about a potential material for objects, hence the score being above absolute zero."
  },
  {
    "index": 1,
    "pred_answer": "The object appears to be a ceramic or wooden mask resembling those from indigenous cultures of modern-day Mexico and Central America. It is reminiscent of pre-Columbian or Mesoamerican art, possibly from the Aztec, Maya, or a similar indigenous culture. The mask features animal motifs, which are common in these cultures.",
    "answer": "Paracas",
    "question": "What is this object's culture?",
    "output": "Rating: 2\n\nExplanation: The generated response is largely incorrect. It identifies the object as a mask from indigenous cultures of Mexico and Central America, relating it to pre-Columbian Mesoamerican art such as Aztec or Maya. However, the ground truth identifies it as \"Paracas,\" which refers to a culture that developed in the Andes region, specifically in what is now modern-day Peru, South America, rather than Mexico or Central America. The mention of animal motifs in the generated response might be a weak overlap but does not significantly align with the ground truth.\n\nDifferences:\n1. Cultural Region: The generated response incorrectly identifies the geographical and cultural origins as Mexico and Central America, while the ground truth specifies the Paracas culture from Peru.\n2. Specificity: The ground truth precisely names the Paracas culture, whereas the generated response makes broader assumptions about Mesoamerican cultures.\n3. Artifact Description: The generated response describes the artifact as resembling pre-Columbian masks, while the ground truth does not confirm it being a mask or related to that particular art style."
  },
  {
    "index": 2,
    "pred_answer": "The image shows a sculptural mask with a dual design. The mask features a human face with exaggerated features including large almond-shaped eyes, a broad nose, and a wide mouth. The cheeks have vertical stripes, giving it a stylized appearance. Atop the human face, there's an animal figure, possibly a totemic creature with an open mouth and sharp teeth, horns or ears, and pronounced nostrils. The mask has a mix of earthy orange and tan colors, with black details accentuating specific features. The overall design is artistic and likely has cultural or ritual significance.",
    "answer": "Pottery with mask; unusual type; animal mask on forehead.",
    "question": "Describe this image",
    "output": "Rating: 6\n\nExplanation: \n\n1. **Overall Description**:\n   - Both the generated response and the ground truth describe a mask. The ground truth specifies \"Pottery with mask,\" whereas the generated response does not explicitly mention pottery.\n\n2. **Design and Features**:\n   - The ground truth simply mentions \"animal mask on forehead.\" Meanwhile, the generated response offers a more detailed description, noting a \"dual design\" with features like large eyes, a wide mouth, and an animal figure on top.\n\n3. **Colors**:\n   - The generated response highlights the colors (earthy orange and tan) and additional black detailing, which the ground truth does not mention.\n\n4. **Cultural Significance**:\n   - The generated response speculates on cultural significance, which is absent in the ground truth.\n\nThe generated response provides a more embellished and detailed visual description, whereas the ground truth text is concise and focused more on the type and structure (pottery with mask, animal mask on forehead) without elaborating on visual details or colors."
  }
]
```