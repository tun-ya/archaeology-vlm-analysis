# LLaVa-NeXT

## Result example
*Responses generated from LLaVa-NeXT*
```
llava_next_7b
└── results_processed_data.json
```

```json
    {
        "image": "images/29-41-753.jpg",
        "question": "Describe this image",
        "answer": "Grey ware. mask or part of urn; face wearing half mask",
        "pred_answer": "The image shows a small, grayish-brown sculpture of a humanoid face with a stylized, possibly ancient or prehistoric, appearance. The face has a prominent nose, eyes, and mouth, with a somewhat angular and simplistic design. The sculpture is placed on a white surface, and there is a black and white checkered ruler next to it, indicating its size. Below the sculpture, there is a clear plastic ruler with a black strip and"
    }
```

## GPT-4o evaluation example
*Evaluated responses from GPT-4o*
```
llava_next_7b
└── gpt_evaluation.json
```
```json
    {
        "index": 365,
        "pred_answer": "The image shows a small, grayish-brown sculpture of a humanoid face with a stylized, possibly ancient or prehistoric, appearance. The face has a prominent nose, eyes, and mouth, with a somewhat angular and simplistic design. The sculpture is placed on a white surface, and there is a black and white checkered ruler next to it, indicating its size. Below the sculpture, there is a clear plastic ruler with a black strip and",
        "answer": "Grey ware. mask or part of urn; face wearing half mask",
        "question": "Describe this image",
        "output": "Rating: 8\n\nThe generated response and the ground truth text both describe a sculpture with a humanoid face. However, there are some differences and additional details in each:\n\n1. Color:\n   - Both responses agree on the color being grayish.\n   - The generated response describes it as \"grayish-brown,\" whereas the ground truth simply says \"Grey ware.\"\n\n2. Description of the Face:\n   - The generated response mentions \"a prominent nose, eyes, and mouth\" and describes it as \"stylized, possibly ancient or prehistoric\" with \"angular and simplistic design.\"\n   - The ground truth describes it as \"face wearing half mask,\" which is not specifically mentioned in the generated response.\n\n3. Context and Position:\n   - The generated response notes the sculpture is placed on a white surface and next to a checkered ruler, indicating size.\n   - The ground truth does not provide this contextual information.\n\n4. Additional Details:\n   - The ground truth suggests it might be \"a mask or part of urn,\" which is a specific contextual detail missing from the generated response.\n   - The generated response started to describe a ruler with a black strip below the sculpture, but is incomplete.\n\nOverall, both descriptions provide a good understanding of the object's appearance, but the generated response adds some context and descriptive details. The ground truth offers a more specific historical or functional context that the generated response lacks. The generated response could have been rated higher if it included mention of the mask or urn context from the ground truth."
    }
```