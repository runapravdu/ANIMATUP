!pip install pyspark opencv-python -q
import os
from google.colab import files
import cv2
import glob
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import BooleanType

print("--- Пожалуйста, загрузите ваш ZIP-архив с исходными видео... ---")
os.makedirs('source_videos', exist_ok=True)
uploaded = files.upload()
if uploaded:
    zip_filename = list(uploaded.keys())[0]
    !unzip -o "{zip_filename}" -d source_videos
else:
    raise RuntimeError("Видео не были загружены.")

output_frames_dir = 'extracted_frames'
os.makedirs(output_frames_dir, exist_ok=True)
def process_video_spark(video_path):
    try:
        video_filename = os.path.basename(video_path)
        video_capture = cv2.VideoCapture(video_path)
        fps = video_capture.get(cv2.CAP_PROP_FPS)
        if not fps or fps < 1: fps = 25
        frame_count, saved_count = 0, 0
        while True:
            success, frame = video_capture.read()
            if not success: break
            if frame_count % int(fps/2) == 0:
                frame_save_path = os.path.join(output_frames_dir, f"{os.path.splitext(video_filename)[0]}_frame_{saved_count:04d}.jpg")
                cv2.imwrite(frame_save_path, frame)
                saved_count += 1
            frame_count += 1
        video_capture.release()
        return True
    except:
        return False

spark = SparkSession.builder.appName("VideoFrameExtraction").getOrCreate()
video_files = glob.glob(os.path.join('source_videos', '**', '*.*'), recursive=True)
df = spark.createDataFrame([(f,) for f in video_files], ["video_path"])
process_video_udf = udf(process_video_spark, BooleanType())
result_df = df.withColumn("processed", process_video_udf(df["video_path"]))
result_df.collect()
spark.stop()

num_frames = len(glob.glob(os.path.join(output_frames_dir, '*.jpg')))
print(f"\n>>> ПАЙПЛАЙН 1 (ЭТАП 1) ЗАВЕРШЕН. Извлечено кадров: {num_frames} ---")