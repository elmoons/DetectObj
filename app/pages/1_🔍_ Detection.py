import streamlit as st
from io import BytesIO
from PIL import Image
import os

# Создаем директории для сохранения файлов, если они не существуют
IMAGE_SAVE_DIR = 'saved_images'
VIDEO_SAVE_DIR = 'saved_videos'

os.makedirs(IMAGE_SAVE_DIR, exist_ok=True)
os.makedirs(VIDEO_SAVE_DIR, exist_ok=True)

st.write("# Обнаружение воздушных объектов с помощью анализа видеоинформации")

# Функция для обработки изображения (пока пустая)
def process_image(image_path: str):
    # Здесь будет логика обработки изображения
    pass

# Функция для обработки видео (пока пустая)
def process_video(video_path: str):
    # Здесь будет логика обработки видео
    pass

# Загрузка медиафайла
media_file = st.file_uploader("Загрузите фото или видео для обнаружения объектов, видео только в формате mp4",
                              type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

if media_file is not None:
    # Проверка типа файла
    if media_file.type.startswith("image"):
        # Открываем изображение с помощью PIL
        image = Image.open(media_file)

        # Конвертируем изображение в формат JPG
        img_io = BytesIO()
        image = image.convert("RGB")  # Преобразуем изображение в RGB
        image.save(img_io, format='JPEG')
        img_io.seek(0)

        # Сохранение изображения в папку
        image_filename = os.path.join(IMAGE_SAVE_DIR, f"{media_file.name.split('.')[0]}.jpg")
        with open(image_filename, 'wb') as out_file:
            out_file.write(img_io.getbuffer())

        # Вызываем функцию обработки изображения
        process_image(image_filename)

        # Показ загруженного изображения на странице
        st.image(image, caption="Загруженное изображение и сохраненное как JPG", use_column_width=True)

    elif media_file.type.startswith("video"):
        # Сохранение видео в папку
        video_filename = os.path.join(VIDEO_SAVE_DIR, media_file.name)
        with open(video_filename, 'wb') as out_file:
            out_file.write(media_file.read())

        # Вызываем функцию обработки видео
        process_video(video_filename)

        # Показ видео на странице
        st.video(media_file)
