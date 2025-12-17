from PIL import Image
import os

img_path = '/Users/mosama/.gemini/antigravity/brain/981661f4-7d6e-4bf4-bc0f-9f3676b2eb18/podcast_mic_icon_1766001955715.png'
output_path = 'portfolio/static/portfolio/img/favicon.ico'

# Create directory if not exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

img = Image.open(img_path)
img.save(output_path, format='ICO', sizes=[(32, 32)])
print(f"Favicon saved to {output_path}")
