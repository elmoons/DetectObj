import streamlit as st
import requests
from io import BytesIO

# URL FastAPI сервера
API_IMAGE_URL = "http://127.0.0.1:8000/upload_image/"
API_VIDEO_URL = "http://127.0.0.1:8000/upload_video/"

st.write("# Обнаружение воздушных объектов с помощью анализа видеоинформации")

# Загрузка медиафайла
media_file = st.file_uploader("Загрузите фото или видео для обнаружения объектов",
                              type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

if media_file is not None:
    # Проверка типа файла
    if media_file.type.startswith("image"):
        # Показ изображения
        st.image(media_file, caption="Uploaded Image", use_column_width=True)

        # Отправка изображения на FastAPI для обработки
        files = {"file": media_file}
        response = requests.post(API_IMAGE_URL, files=files)

        # Обработка ответа
        if response.status_code == 200:
            # Если обработка успешна, показываем результат
            processed_image = BytesIO(response.content)
            st.image(processed_image, caption="Processed Image", use_column_width=True)
        else:
            st.error(f"Error processing image. Status code: {response.status_code}")

    elif media_file.type.startswith("video"):
        # Показ видео
        st.video(media_file)

        # Отправка видео на FastAPI для обработки
        files = {"file": media_file}
        response = requests.post(API_VIDEO_URL, files=files)

        # Обработка ответа
        if response.status_code == 200:
            result = response.json()
            st.success(f"Video processed! {result['frames']} frames processed.")
        else:
            st.error(f"Error processing video. Status code: {response.status_code}")
