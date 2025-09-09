
!pip install transformers "Pillow<10.0" -q
print("Зависимости установлены. Пожалуйста, ПЕРЕЗАПУСТИТЕ СРЕДУ ВЫПОЛНЕНИЯ (Runtime -> Restart session) и запустите Ячейку 2")


from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
import glob
import os

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")

image_files = glob.glob(os.path.join('extracted_frames', '*.jpg'))
for image_path in image_files:
    txt_path = os.path.splitext(image_path)[0] + '.txt'
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, return_tensors="pt").to("cuda")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    with open(txt_path, 'w') as f:
        f.write(f"ohwx kenji, {caption}")

print(f"\n>>> ПАЙПЛАЙН 1 (ЭТАП 2) ЗАВЕРШЕН. Создано {len(image_files)} .txt файлов. ---")