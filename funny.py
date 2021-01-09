from PIL import Image, ImageDraw, ImageSequence, ImageFont
import io

def get_funny_thing(text):
    original_funny = Image.open("a.gif")

    frames = []

    for frame in ImageSequence.Iterator(original_funny):
        frame = frame.convert('RGB')

        # Draw the text on the frame
        d = ImageDraw.Draw(frame)
        font = ImageFont.truetype("david.ttf", 22)
        d.text((150-len(text)*5,10),text,fill=(0,0,0), font=font)
        del d

        b = io.BytesIO()

        frame.save(b, format="GIF")
        frame = Image.open(b)

        frames.append(frame)

    gif_bytes = io.BytesIO()
    frames[0].save(gif_bytes, format="GIF", save_all=True, append_images=frames[1:])

    gif_bytes.seek(0)
    return gif_bytes