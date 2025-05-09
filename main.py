from fastapi import FastAPI
from Summarizer import Summarizer
from SentimentAnalyzer import SentimentAnalyzer

app = FastAPI()

sentiment_analyzer = SentimentAnalyzer()
summarizer = Summarizer('d0rj/rut5-base-summ')

@app.get("/")
async def root():
    return {
        "health": "Для работоспособности проекта перейдите по ссылке /health/. Если статус success - все работает прекрасно.",
        "get_summary": "Для получения краткого содержания текста перейдите по ссылке /get_summary/ и передайте в параметр text ваш полный текст.",
        "get_sentiment": "Для получения тональности текста перейдите по ссылке /get_sentiment/ и передайте в параметр text ваш полный текст.",
        "get_summary_sentiment": "Для получения краткого содержания текста и тональности краткого содержания перейдите по ссылке /get_summary_sentiment/ и передайте в параметр text ваш полный текст."
    }

@app.get("/get_summary/")
async def get_summary(text: str = ''):
    if not (text):
         return {
                "status" : "error",
                "error_message": "Текст отсутствует. Введите текст."
            }
    sum_text = summarizer.summarize(text)
    if not sum_text:
        return {
            "status" : "error",
            "error_message": "Слишком короткий текст. Получение краткого содержания невозможно."
        }
    return {
        "status" : "success",
        "summarized_text": sum_text
    }

@app.get("/health")
async def health():
    test_text = "Это тестовая строка для проверки работоспособности суммаризации."
    try:
        summary = summarizer.summarize(test_text)
        if summary:
            return {
                "status": "success"
            }
        else:
            return {
                "status": "error",
                "error_message": "Суммаризация не работает (пустой ответ)"
            }
    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }

@app.get("/get_sentiment/")
async def get_sentiment(text: str = ''):
    sentiment = sentiment_analyzer.analyze(sum_text)
    return {
            "status" : "success",
            "sentiment": sentiment
        }

@app.get("/get_summary_sentiment/")
async def get_summary_sentiment(text: str = ''):
    return summarize_and_analyze(text)

def summarize_and_analyze(text: str):
    sum_text = summarizer.summarize(text)
    sentiment = sentiment_analyzer.analyze(sum_text)
    return {
        "status" : "success",
        "summarized_text": sum_text,
        "sentiment": sentiment
    }
