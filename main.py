from fastapi import FastAPI
from transformers import T5Tokenizer, T5ForConditionalGeneration

app = FastAPI()

def get_summ_text(textForSumm):
    tokenizer = T5Tokenizer.from_pretrained('d0rj/rut5-base-summ')
    model = T5ForConditionalGeneration.from_pretrained('d0rj/rut5-base-summ').eval()

    input_ids = tokenizer(textForSumm, return_tensors='pt').input_ids
    outputs = model.generate(input_ids)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary


@app.get("/")
async def root():
    return {"lab-6": "Для получения краткого содержания текста перейдите по ссылке /get_summary/ и передайте в параметр text ваш полный текст."}


@app.get("/get_summary/")
async def get_summary(text: str = ''):
    sum_text = get_summ_text(text)
    return {"summarized_text": sum_text}

