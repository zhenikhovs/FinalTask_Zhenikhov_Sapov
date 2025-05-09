from main import get_summ_text, summarize_and_analyze
from fastapi.testclient import TestClient
from sentiment_analyzer import SentimentAnalyzer
from main import app

def test_age_count_2():
    assert get_summ_text(
        'Деловая среда становится все более конкурентной, поэтому обучение персонала необходимо для повышения результативности работы, снижения ошибок и улучшения качества продукции и услуг. Портал разрабатывался и внедрялся в ООО «Легаси Студио». Проблемы обучения заключались в том, что выдаваемая информация неструктурирована, приходилось отвлекать опытных специалистов, образовательные платформы имеют каждая свою структуру, руководство не могло контролировать процесс обучения сотрудников. ') == 'Школьная среда становится все более конкурентной, поэтому обучение персонала необходимо для повышения результативности работы, снижения ошибок и улучшения качества продукции и услуг.'


def test_age_count_3():
    assert get_summ_text(
        'Деловая среда становится все более конкурентной, поэтому обучение персонала необходимо для повышения результативности работы, снижения ошибок и улучшения качества продукции и услуг. Портал разрабатывался и внедрялся в ООО «Легаси Студио». Проблемы обучения заключались в том, что выдаваемая информация неструктурирована, приходилось отвлекать опытных специалистов, образовательные платформы имеют каждая свою структуру, руководство не могло контролировать процесс обучения сотрудников. Цель данного проекта заключается в создании системы, которая уменьшит трудовые и временные затраты наставников на обучение и позволит ввести контроль за продвижением обучения сотрудников.') == '«Легаси Студио» предлагает создать систему, которая уменьшит трудовые и временные затраты наставников на обучение.'

def test_empty_text():
    assert get_summ_text('Привет') == ''

def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_sentiment_analyzer():
    analyzer = SentimentAnalyzer()
    text = "Это очень хороший и интересный текст, который должен быть воспринят положительно."
    result = analyzer.analyze(text)
    assert isinstance(result, list)
    assert len(result) > 0
    assert "label" in result[0]
    assert "score" in result[0]

def test_summarize_and_analyze():
    text = "Это очень хороший и интересный текст, который должен быть воспринят положительно."
    result = summarize_and_analyze(text)
    assert "summarized_text" in result
    assert "sentiment" in result
    assert isinstance(result["sentiment"], list)
    assert len(result["sentiment"]) > 0
    assert "label" in result["sentiment"][0]
    assert "score" in result["sentiment"][0]
