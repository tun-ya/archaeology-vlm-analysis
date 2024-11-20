# Qwen2-VL

## Result example
*Responses generated from Qwen2-VL*
```
qwen2_vl_7b
└── results_processed_data.json
```

```json
    {
        "image": "images/78-12-23.jpg",
        "question": "Describe this image",
        "answer": "Silver, repoussed into a butterfly, stamped, with four silver wires attached to appliqued silver balls and one small, oval, bezel-set turquoise stone.",
        "pred_answer": "The image depicts a brooch designed in the shape of a butterfly. The brooch is crafted from a shiny, metallic material, likely silver or a similar alloy. The wings of the butterfly are intricately detailed with fine lines and patterns, giving them a delicate and ornate appearance. The body of the butterfly features a central oval gemstone, which is a vibrant turquoise color, adding a touch of color to the otherwise metallic design. The overall design is elegant and artistic, combining natural inspiration with fine craftsmanship."
    }
```

## GPT-4o evaluation example
*Evaluated responses from GPT-4o*
```
qwen2_vl_7b
└── gpt_evaluation.json
```
```json
    {
    "index": 1988,
    "pred_answer": "The image depicts a brooch designed in the shape of a butterfly. The brooch is crafted from a shiny, metallic material, likely silver or a similar alloy. The wings of the butterfly are intricately detailed with fine lines and patterns, giving them a delicate and ornate appearance. The body of the butterfly features a central oval gemstone, which is a vibrant turquoise color, adding a touch of color to the otherwise metallic design. The overall design is elegant and artistic, combining natural inspiration with fine craftsmanship.",
    "answer": "Silver, repoussed into a butterfly, stamped, with four silver wires attached to appliqued silver balls and one small, oval, bezel-set turquoise stone.",
    "question": "Describe this image",
    "output": "Rating: 9\n\nExplanation: The generated response and the ground truth text describe similar visual aspects of the brooch, specifically focusing on its butterfly shape and materials used. Both mention the use of silver and highlight a turquoise stone in an oval form as part of the design. \n\nKey Differences and Similarities:\n1. Description of Material: Both texts identify the material as silver, with the generated response suggesting a shiny metallic appearance likely resembling silver, while the ground truth explicitly states it is \"silver repoussed.\"\n2. Detail on Design: The generated response emphasizes the intricate details and patterns on the wings and the overall elegant design whereas the ground truth specifies attributes like being \"stamped\" and having \"four silver wires attached to appliqued silver balls.\"\n3. Gemstone Description: Both describe an oval turquoise stone, but the ground truth text provides additional detail, noting the stone is bezel-set.\n\nThe overall content is highly congruent and describes the primary features accurately, thus deserving a rating close to perfect. The slight differences in technical description and specific techniques like \"repoussed\" or \"bezel-set\" prevent a perfect score."
  }
```