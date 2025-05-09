from transformers import T5Tokenizer, T5ForConditionalGeneration

class Summarizer:
    def __init__(self, model_name: str):
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name).eval()

    def summarize(self, text: str) -> str:
        if not text:
            return ''
        input_ids = self.tokenizer(text, return_tensors='pt').input_ids
        outputs = self.model.generate(input_ids)
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary