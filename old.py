# from transformers import MBartTokenizer, MBartForConditionalGeneration
#
#
# def get_summ_text(textForSumm):
#     model_name = "IlyaGusev/mbart_ru_sum_gazeta"
#     tokenizer = MBartTokenizer.from_pretrained(model_name)
#     model = MBartForConditionalGeneration.from_pretrained(model_name)
#
#     input_ids = tokenizer(
#         [textForSumm],
#         max_length=600,
#         padding="max_length",
#         truncation=True,
#         return_tensors="pt",
#     )["input_ids"]
#
#     output_ids = model.generate(
#         input_ids=input_ids,
#         no_repeat_ngram_size=4
#     )[0]
#
#     summary = tokenizer.decode(output_ids, skip_special_tokens=True)
#     return summary


# from transformers import AutoTokenizer, T5ForConditionalGeneration
# import streamlit as st
#
# model_name = "IlyaGusev/rut5_base_sum_gazeta"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)
#
#
# def get_summ_text(textForSumm):
#     input_ids = tokenizer(
#         [textForSumm],
#         max_length=10,
#         add_special_tokens=True,
#         padding="max_length",
#         truncation=True,
#         return_tensors="pt"
#     )["input_ids"]
#
#     output_ids = model.generate(
#         input_ids=input_ids,
#         no_repeat_ngram_size=4
#     )[0]
#
#     summary = tokenizer.decode(output_ids, skip_special_tokens=True)
#     return summary
#
#
# st.header("Краткое содержание текста")
# st.subheader("(Summarization text)")
# text = st.text_area('Полный текст для сжатия:',  key='textInput')
# col1, col2 = st.columns(2)
#
# with col1:
#     clicked = st.button('Сжать текст!')
# def on_fill_click():
#     exampleText = 'Цифровизация – это социально-экономическая трансформация, которую вызовет массовое внедрение и усвоение новых технологий создания, обработки, анализа и передачи информации. Сельское хозяйство становится одним из основных потребителей цифровых технологий. Генерация большого объема данных разнообразными датчиками в теплицах, полях, фермах и других производственных площадках особенно актуализирует применение цифровых технологий анализа агроэкономических данных. Широкое применение инструментов и методов Data Science, машинного обучения, нейронных сетей в конечном счете позволит существенно повысить эффективность принимаемых управленческих решений в АПК.'
#     st.session_state.textInput = exampleText
# with col2:
#     st.button("Заполнить поле текстом", on_click=on_fill_click)
#
#
# if clicked:
#     if len(text.strip()):
#         data_load_state = st.text('Ожидайте, идет сжатие текста.')
#         summText = get_summ_text(text)
#         data_load_state.subheader('Результат сжатия:')
#         st.write(summText)
#     else:
#         st.text('Введите текст!')





#
# from transformers import AutoTokenizer, T5ForConditionalGeneration
# import streamlit as st
#
# model_name = "IlyaGusev/rut5_base_headline_gen_telegram"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)
#
#
# def get_summ_text(textForSumm):
#     input_ids = tokenizer(
#         [textForSumm],
#         max_length=600,
#         add_special_tokens=True,
#         padding="max_length",
#         truncation=True,
#         return_tensors="pt"
#     )["input_ids"]
#
#     output_ids = model.generate(
#         input_ids=input_ids
#     )[0]
#
#     headline = tokenizer.decode(output_ids, skip_special_tokens=True)
#
#     return headline
#
#
# st.header("Краткое содержание текста")
# st.subheader("(Summarization text)")
# text = st.text_area('Полный текст для сжатия:',  key='textInput')
# col1, col2 = st.columns(2)
#
# with col1:
#     clicked = st.button('Сжать текст!')
# def on_fill_click():
#     exampleText = 'Цифровизация – это социально-экономическая трансформация, которую вызовет массовое внедрение и усвоение новых технологий создания, обработки, анализа и передачи информации. Сельское хозяйство становится одним из основных потребителей цифровых технологий. Генерация большого объема данных разнообразными датчиками в теплицах, полях, фермах и других производственных площадках особенно актуализирует применение цифровых технологий анализа агроэкономических данных. Широкое применение инструментов и методов Data Science, машинного обучения, нейронных сетей в конечном счете позволит существенно повысить эффективность принимаемых управленческих решений в АПК.'
#     st.session_state.textInput = exampleText
# with col2:
#     st.button("Заполнить поле текстом", on_click=on_fill_click)
#
#
# if clicked:
#     if len(text.strip()):
#         data_load_state = st.text('Ожидайте, идет сжатие текста.')
#         summText = get_summ_text(text)
#         data_load_state.subheader('Результат сжатия:')
#         st.write(summText)
#     else:
#         st.text('Введите текст!')







# import streamlit as st
# import torch
# from transformers import T5ForConditionalGeneration, T5Tokenizer
# MODEL_NAME = 'cointegrated/rut5-base-absum'
# model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
# tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)
#
# def summarize(
#     text, n_words=None, compression=None,
#     max_length=1000, num_beams=3, do_sample=False, repetition_penalty=10.0,
#     **kwargs
# ):
#     if n_words:
#         text = '[{}] '.format(n_words) + text
#     elif compression:
#         text = '[{0:.1g}] '.format(compression) + text
#     x = tokenizer(text, return_tensors='pt', padding=True).to(model.device)
#     with torch.inference_mode():
#         out = model.generate(
#             **x,
#             max_length=max_length, num_beams=num_beams,
#             do_sample=do_sample, repetition_penalty=repetition_penalty,
#             **kwargs
#         )
#     return tokenizer.decode(out[0], skip_special_tokens=True)
#
#
# st.header("Краткое содержание текста")
# st.subheader("(Summarization text)")
# text = st.text_area('Полный текст для сжатия:',  key='textInput')
# col1, col2 = st.columns(2)
#
# with col1:
#     clicked = st.button('Сжать текст!')
# def on_fill_click():
#     exampleText = 'Цифровизация – это социально-экономическая трансформация, которую вызовет массовое внедрение и усвоение новых технологий создания, обработки, анализа и передачи информации. Сельское хозяйство становится одним из основных потребителей цифровых технологий. Генерация большого объема данных разнообразными датчиками в теплицах, полях, фермах и других производственных площадках особенно актуализирует применение цифровых технологий анализа агроэкономических данных. Широкое применение инструментов и методов Data Science, машинного обучения, нейронных сетей в конечном счете позволит существенно повысить эффективность принимаемых управленческих решений в АПК.'
#     st.session_state.textInput = exampleText
# with col2:
#     st.button("Заполнить поле текстом", on_click=on_fill_click)
#
#
# if clicked:
#     if len(text.strip()):
#         data_load_state = st.text('Ожидайте, идет сжатие текста.')
#         summText = summarize(text)
#         data_load_state.subheader('Результат сжатия:')
#         st.write(summText)
#     else:
#         st.text('Введите текст!')



#
# КЛАССНЫЙ
#
#
# import streamlit as st
# from transformers import T5Tokenizer, T5ForConditionalGeneration
#
# def get_summ_text(textForSumm):
#     tokenizer = T5Tokenizer.from_pretrained('d0rj/rut5-base-summ')
#     model = T5ForConditionalGeneration.from_pretrained('d0rj/rut5-base-summ').eval()
#
#     input_ids = tokenizer(textForSumm, return_tensors='pt').input_ids
#     outputs = model.generate(input_ids)
#     summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
#
#     return summary
#
#
# st.header("Краткое содержание текста")
# st.subheader("(Summarization text)")
# text = st.text_area('Полный текст для сжатия:',  key='textInput')
# col1, col2 = st.columns(2)
#
# with col1:
#     clicked = st.button('Сжать текст!')
# def on_fill_click():
#     exampleText = 'Цифровизация – это социально-экономическая трансформация, которую вызовет массовое внедрение и усвоение новых технологий создания, обработки, анализа и передачи информации. Сельское хозяйство становится одним из основных потребителей цифровых технологий. Генерация большого объема данных разнообразными датчиками в теплицах, полях, фермах и других производственных площадках особенно актуализирует применение цифровых технологий анализа агроэкономических данных. Широкое применение инструментов и методов Data Science, машинного обучения, нейронных сетей в конечном счете позволит существенно повысить эффективность принимаемых управленческих решений в АПК.'
#     st.session_state.textInput = exampleText
# with col2:
#     st.button("Заполнить поле текстом", on_click=on_fill_click)
#
#
# if clicked:
#     if len(text.strip()):
#         data_load_state = st.text('Ожидайте, идет сжатие текста.')
#         summText = get_summ_text(text)
#         data_load_state.subheader('Результат сжатия:')
#         st.write(summText)
#     else:
#         st.text('Введите текст!')