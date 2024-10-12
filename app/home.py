import streamlit as st
from PIL import Image

# Заголовок страницы
st.write('# Комплексное решение по кейсу "Обнаружение воздушных объектов с помощью анализа видеоинформации"')

# Описание кейса
st.write("""
Данный WEB-сервис представляет собой систему, способную обнаруживать беспилотные летательные аппараты 
на видеоинформации с использованием дообученной модели YOLOv11. Объекты классифицируются на самолеты и вертолеты, 
результаты обнаружения сохраняются с таймкодами для анализа.
""")
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
# Логотипы
image_mpt = Image.open('img/mpt_logo_red.png')
image_rus = Image.open('img/Russia.png')

# Создание двух колонок для отображения изображений
col1, col2 = st.columns(2)

# Размещение изображений по колонкам
with col1:
    st.image(image_mpt, use_column_width=True)

with col2:
    st.image(image_rus, use_column_width=True)
