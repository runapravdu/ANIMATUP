import torch
from diffusers import StableVideoDiffusionPipeline
from diffusers.utils import load_image
from PIL import Image
import os

video_pipe = StableVideoDiffusionPipeline.from_pretrained("stabilityai/stable-video-diffusion-img2vid-xt", torch_dtype=torch.float16, variant="fp16").to("cuda")
image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/svd/rocket.png"
start_frame_image_3d = load_image(image_url).resize((1024, 576))
output_frames_3d = video_pipe(start_frame_image_3d, num_frames=25, output_type='pil').frames[0]
output_folder_3d = "generated_frames_3d"
os.makedirs(output_folder_3d, exist_ok=True)
for i, frame in enumerate(output_frames_3d):
    frame.save(os.path.join(output_folder_3d, f"frame_{i:04d}.png"))
print(f"\n>>> ПАЙПЛАЙН 2 (3D) ЗАВЕРШЕН. Кадры сохранены в '{output_folder_3d}'. ---")