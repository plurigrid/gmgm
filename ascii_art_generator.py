```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_ascii_art(prompt):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=500, temperature=0.7, top_p=0.8)

    ascii_art = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return ascii_art
```