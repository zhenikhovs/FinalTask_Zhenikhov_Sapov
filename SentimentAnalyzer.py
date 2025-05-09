from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.classifier = pipeline("sentiment-analysis")

    def analyze(self, text: str):
        return self.classifier(text)
