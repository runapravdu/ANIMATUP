
!pip install "diffusers[torch,torchvision]==0.25.0" "transformers==4.36.2" "accelerate==0.26.1" "huggingface_hub==0.20.3" omegaconf -q
print("Зависимости установлены. Пожалуйста, ПЕРЕЗАПУСТИТЕ СРЕДУ ВЫПОЛНЕНИЯ и запустите Ячейку 3.2")


import torch
from diffusers import StableDiffusionPipeline, StableVideoDiffusionPipeline
from diffusers.utils import export_to_video
from google.colab import drive
import os
from PIL import Image

drive.mount('/content/drive')

image_pipe = StableDiffusionPipeline.from_pretrained("Meina/MeinaMix_V11", torch_dtype=torch.float16, use_safesensors=True, safety_checker=None).to("cuda")
style_lora_path = "/content/drive/MyDrive/AI_MODELS/LORA/bleach_style_offset.safetensors"
detail_lora_path = "/content/drive/MyDrive/AI_MODELS/LORA/add_detail.safetensors"
image_pipe.load_lora_weights(style_lora_path, adapter_name="style")
image_pipe.load_lora_weights(detail_lora_path, adapter_name="detail")
prompt = "masterpiece, best quality, (bleach anime style:1.3), 1boy, upper body, facing camera, in a futuristic city at night, rain, <lora:style:0.8> <lora:detail:0.5>"
start_frame_image = image_pipe(prompt, negative_prompt="3d, realistic", num_inference_steps=30, width=1024, height=576).images[0]
del image_pipe
torch.cuda.empty_cache()

video_pipe = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16").to("cuda")
output_frames_2d = video_pipe(start_frame_image, num_frames=25, output_type='pil').frames[0]
output_folder_2d = "generated_frames_2d"
os.makedirs(output_folder_2d, exist_ok=True)
for i, frame in enumerate(output_frames_2d):
    frame.save(os.path.join(output_folder_2d, f"frame_{i:04d}.png"))
print(f"\n>>> ПАЙПЛАЙН 2 (2D) ЗАВЕРШЕН. Кадры сохранены в '{output_folder_2d}'. ---")