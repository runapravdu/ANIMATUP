# ANIMAT VIDEO
AI-Agent  for generating a stylized video with sound
# Automation of the process of creating videos in 2D and 3D styles, including descriptions, background music, and final assembly
1: ПОДГОТОВКА ДАННЫХ (Data Engineering & ML)**

**Задача:** Превратить набор сырых видео в готовый, аннотированный датасет для обучения. Этот пайплайн демонстрирует ваши навыки в **Spark**, **Python** и **ML (BLIP)**.

**Ячейка 1: Нарезка видео на кадры с помощью Spark**
*   **Вход:** ZIP-архив с видеофайлами.
*   **Действие:** Использует Spark для распараллеливания процесса и извлечения кадров из каждого видео.
*   **Выход:** Папка `extracted_frames`, содержащая сотни или тысячи изображений `.jpg`.
