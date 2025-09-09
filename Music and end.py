
!pip install scipy moviepy -q # Убедимся, что все для сборки на месте
from diffusers import AudioLDM2Pipeline
import scipy.io.wavfile
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import glob
import os

print("--- Генерация фоновой музыки... ---")
audio_pipe = AudioLDM2Pipeline.from_pretrained("cvssp/audioldm2", torch_dtype=torch.float16).to("cuda")
audio_prompt = "cinematic synthwave music, heavy rain falling"
audio = audio_pipe(audio_prompt, num_inference_steps=200, audio_length_in_s=2.0).audios[0] 
output_audio_path = "background_music.wav"
sampling_rate = audio_pipe.scheduler.config.sampling_rate
scipy.io.wavfile.write(output_audio_path, rate=sampling_rate, data=audio)
del audio_pipe
torch.cuda.empty_cache()
print(f"Музыка сгенерирована: '{output_audio_path}'\n")
print("Сборка видеоклипов")
frames_2d = sorted(glob.glob(os.path.join('generated_frames_2d', '*.png')))
clip_2d = ImageSequenceClip(frames_2d, fps=7)
frames_3d = sorted(glob.glob(os.path.join('generated_frames_3d', '*.png')))
clip_3d = ImageSequenceClip(frames_3d, fps=7)
print("--- Финальный монтаж... ---")
background_audio = AudioFileClip(output_audio_path)
final_video = concatenate_videoclips([clip_2d, clip_3d])
final_output_path = "final_movie.mp4"
final_video.write_videofile(final_output_path, codec="libx264", audio_codec="aac")
print(f"\n ПРОЕКТ ЗАВЕРШЕН! Финальное видео сохранено в '{final_output_path}' ---")
