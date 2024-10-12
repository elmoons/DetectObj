from typing import Annotated
import uvicorn
from fastapi import FastAPI, File, UploadFile
import os
from fastapi.responses import StreamingResponse
from PIL import Image
import numpy as np
from io import BytesIO

# Инициализация FastAPI
app = FastAPI()

# Пути для хранения медиафайлов
IMAGE_DIR = "media/images"
VIDEO_DIR = "media/videos"

# Создаем директории, если они не существуют
os.makedirs(IMAGE_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)


# Функция для обработки изображения
def process_image(image):
    # Тут будет логика обработки изображения
    print("дошло")


# Функция для обработки видео
def process_video(file_path: str):
    # Тут будет логика обработки видео
    print("дошло")


# Эндпоинт для загрузки изображения
@app.post("/upload_image/")
async def upload_image(file: Annotated[UploadFile | None, File(description="Upload an image")] = None):
    if file is None:
        return {"error": "No file uploaded"}

    # Получаем расширение файла
    file_extension = file.filename.split('.')[-1].lower()

    if file_extension not in ["jpg", "jpeg", "png"]:
        return {"error": "Unsupported file type"}

    # Сохраняем изображение в папку
    image_path = os.path.join(IMAGE_DIR, file.filename)
    with open(image_path, "wb") as img_file:
        img_file.write(await file.read())

    # Открываем и обрабатываем изображение
    with Image.open(image_path) as image:
        image_data = np.array(image)
        processed_image = process_image(image_data)

    return {"message": f"Image saved at {image_path}"}


# Эндпоинт для загрузки видео
@app.post("/upload_video/")
async def upload_video(file: Annotated[UploadFile | None, File(description="Upload a video")] = None):
    if file is None:
        return {"error": "No file uploaded"}

    # Получаем расширение файла
    file_extension = file.filename.split('.')[-1].lower()

    if file_extension not in ["mp4", "avi", "mov"]:
        return {"error": "Unsupported file type"}

    # Сохраняем видео в папку
    video_path = os.path.join(VIDEO_DIR, file.filename)
    with open(video_path, "wb") as vid_file:
        vid_file.write(await file.read())

    # Логика обработки видео (пока не добавлена)
    frames = process_video(video_path)

    return {"message": f"Video saved at {video_path}", "frames_processed": len(frames)}


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
