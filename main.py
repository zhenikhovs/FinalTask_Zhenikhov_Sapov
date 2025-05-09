from fastapi import FastAPI
from transformers import T5Tokenizer, T5ForConditionalGeneration
from transformers import pipeline

app = FastAPI()
class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def analyze(self, text: str):
        return self.classifier(text)
sentiment_analyzer = SentimentAnalyzer()


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

summarizer = Summarizer('d0rj/rut5-base-summ')

@app.get("/")
async def root():
    return {"lab-6": "Для получения краткого содержания текста перейдите по ссылке /get_summary/ и передайте в параметр text ваш полный текст."}

@app.get("/get_summary/")
async def get_summary(text: str = ''):
    sum_text = summarizer.summarize(text)
    if not sum_text:
        return {"error": "Слишком короткий текст. Получение краткого содержания невозможно."}
    return {"summarized_text": sum_text}

@app.get("/health")
async def health():
    test_text = "Это тестовая строка для проверки работоспособности суммаризации."
    try:
        summary = summarizer.summarize(test_text)
        if summary:
            return {"status": "ok"}
        else:
            return {"status": "not ok", "error": "Суммаризация не работает (пустой ответ)"}
    except Exception as e:
        return {"status": "not ok", "error": str(e)}


@app.get("/get_summary_sentiment/")
async def get_summary_sentiment(text: str = ''):
    return summarize_and_analyze(text)

def summarize_and_analyze(text: str):
    sum_text = get_summ_text(text)
    sentiment = sentiment_analyzer.analyze(sum_text)
    return {"summarized_text": sum_text, "sentiment": sentiment}
