# ANIMAT VIDEO
AI-Agent  for generating a stylized video with sound
# Automation of the process of creating videos in 2D and 3D styles, including descriptions, background music, and final assembly
1) ПОДГОТОВКА ДАННЫХ (Data Engineering & ML)

**Задача:** Превратить набор сырых видео в готовый, аннотированный датасет для обучения.Используя **Spark**, **Python** и **ML (BLIP)**.

**1: Нарезка видео на кадры с помощью Spark**
*   **Вход:** ZIP-архив с видеофайлами.
*   **Действие:** Использует Spark для распараллеливания процесса и извлечения кадров из каждого видео.
*   **Выход:** Папка `extracted_frames`, содержащая сотни или тысячи изображений `.jpg`.
  
**2: Автоматическое создание описаний к фото (BLIP)**
*   **Вход:** Папка `extracted_frames` с изображениями.
*   **Действие:** Использует нейросеть BLIP для "просмотра" каждого изображения и генерации текстового описания.
*   **Выход:** Для каждого `image.jpg` создается файл `image.txt` с описанием.
#### **ПАЙПЛАЙН 2: ГЕНЕРАЦИЯ ВИЗУАЛЬНЫХ АССЕТОВ (Deep Learning)**
**Задача:** Создать базовой картинке в 2D или 3D стилях.

**3: Генерация картинок с высокой деталезацией**

<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/94d9f3c1-ecae-4af7-9822-490ddc0ed91f" />
<img width="1024" height="576" alt="image" src="https://github.com/user-attachments/assets/4cf4a049-c9a8-425a-b759-a142fbf74985" />

**Задача:** Создать базовые видеоклипы в 2D и 3D стилях.

**4: Генерация 2D-кадра и "оживление" в видео**
*   **Вход:** Ваши LoRA-модели с Google Drive.
*   **Действие:** Создает один идеальный 2D-кадр например в стиле "Bleach", а затем "оживляет" его с помощью SVD, сохраняя кадры на диск для экономии памяти.
*   **Выход:** Папка `generated_frames_2d` с кадрами для 2D-видео.


https://github.com/user-attachments/assets/a21fdfde-1f34-4d85-82e8-387f984303f6



https://github.com/user-attachments/assets/b73b91df-187b-4495-83cd-a67c7bd2bfaa

**5: Генерация музыки и финальный монтаж**
*   **Вход:** Папки с кадрами (`generated_frames_2d` и `generated_frames_3d`).
*   **Действие:** Генерирует фоновую музыку с помощью AudioLDM 2. Затем с помощью MoviePy собирает два видеоклипа, накладывает на них музыку и склеивает в один финальный фильм.
*   **Выход:** Финальный файл `final_movie.mp4`.
  

Uploading 0911(2).mp4…















