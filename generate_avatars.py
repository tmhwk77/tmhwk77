import os
import io
import sys
from rembg import remove
from PIL import Image, ImageDraw, ImageFilter

def remove_background(input_path):
    print(f"Processing {input_path}...")
    with open(input_path, 'rb') as i:
        input_data = i.read()
        output_data = remove(input_data)
        return Image.open(io.BytesIO(output_data))

def create_solid_background(size, color):
    return Image.new("RGBA", size, color)

def create_gradient_background(size, color1, color2):
    base = Image.new("RGBA", size, color1)
    top = Image.new("RGBA", size, color2)
    mask = Image.new("L", size)
    mask_data = []
    for y in range(size[1]):
        for x in range(size[0]):
            mask_data.append(int(255 * (y / size[1])))
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def main():
    # Look for input image
    input_files = [f for f in os.listdir('.') if f.lower().startswith('input.') or f.lower().startswith('user_provided_image_')]
    
    if not input_files:
        print("Error: Please upload an image named 'input.png' or 'input.jpg' to the workspace.")
        return

    input_path = input_files[0]
    print(f"Found input image: {input_path}")
    
    try:
        # Get subject with transparent background
        subject = remove_background(input_path)
        
        # Resize if too large (optional, but good for consistent avatars)
        # standard linkedin is 400x400 but high res is better. 
        # Let's keep original resolution but ensure subject is centered/fitted if we were doing advanced composition.
        # For now, just composition over background of same size.
        
        width, height = subject.size
        
        # 1. Professional Blue Gradient
        bg_blue = create_gradient_background((width, height), (220, 230, 255, 255), (100, 149, 237, 255)) # Light to Cornflower Blue
        comp_blue = Image.alpha_composite(bg_blue, subject)
        comp_blue.save("avatar_professional_blue.png")
        print("Saved avatar_professional_blue.png")
        
        # 2. Neutral Grey
        bg_grey = create_solid_background((width, height), (240, 240, 240, 255))
        comp_grey = Image.alpha_composite(bg_grey, subject)
        comp_grey.save("avatar_neutral_grey.png")
        print("Saved avatar_neutral_grey.png")
        
        # 3. Clean White
        bg_white = create_solid_background((width, height), (255, 255, 255, 255))
        comp_white = Image.alpha_composite(bg_white, subject)
        comp_white.save("avatar_clean_white.png")
        print("Saved avatar_clean_white.png")
        
        # 4. Dark Mode / Slate
        bg_slate = create_solid_background((width, height), (40, 44, 52, 255))
        comp_slate = Image.alpha_composite(bg_slate, subject)
        comp_slate.save("avatar_dark_slate.png")
        print("Saved avatar_dark_slate.png")

        print("Done! You can now download the generated images.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
