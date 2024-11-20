# LLaVa-NeXT

## Result example
*Responses generated from LLaVa-NeXT*
```
llava_next_7b
└── results_processed_data.json
```

```json
    {
        "image": "images/153817_800.jpg",
        "question": "Describe this image",
        "answer": "Silver, repoussed into a butterfly, stamped, with four silver wires attached to appliqued silver balls and one small, oval, bezel-set turquoise stone.",
        "pred_answer": "The image shows a piece of jewelry, specifically a brooch, against a plain white background. The brooch features a design that resembles a butterfly, with a prominent central body that has a textured surface and a teal-colored stone set in the center. The wings of the butterfly are spread out, and the body is adorned with what appears to be a pattern of small, intricate details. The brooch has a metallic finish, with the body and"
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
    "index": 1988,
    "pred_answer": "The image shows a piece of jewelry, specifically a brooch, against a plain white background. The brooch features a design that resembles a butterfly, with a prominent central body and two symmetrical wings. The body of the butterfly has a textured surface with a series of small, round embellishments that could be beads or stones. The wings are elongated and have a smooth, polished finish.\n\nThe brooch has a teal-colored",
    "answer": "Silver, repoussed into a butterfly, stamped, with four silver wires attached to appliqued silver balls and one small, oval, bezel-set turquoise stone.",
    "question": "Describe this image",
    "output": "Rating: 7\n\nThe generated response and the ground truth text describe a butterfly-themed piece of jewelry, but there are some differences and gaps in detail:\n\n1. Shape and Design: Both descriptions refer to the design of a butterfly. However, the ground truth provides additional detail by mentioning that it is \"repoussed,\" indicating a particular metalworking technique used.\n\n2. Material and Texture: The ground truth specifically notes that the brooch is made of silver, which is not directly mentioned in the generated response. The generated response does mention a \"textured surface,\" but not the repoussé technique.\n\n3. Embellishments: The generated response mentions \"small, round embellishments,\" while the ground truth states these are \"appliqued silver balls.\" The ground truth provides more specificity.\n\n4. Turquoise Stone: The ground truth specifies a \"small, oval, bezel-set turquoise stone,\" whereas the generated response mentions a \"teal-colored\" element, which could relate to the turquoise stone but lacks the precision of the ground truth.\n\n5. Wiring Details: The ground truth mentions \"four silver wires,\" a detail absent in the generated response.\n\nOverall, while the generated response captures the general appearance of a butterfly-themed brooch, it lacks some specifics provided in the ground truth, particularly regarding materials and specific design elements. This leads to a slightly less complete and accurate description, warranting a rating of 7."
  }
```