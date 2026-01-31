from PIL import Image
from utils import binary_to_text

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    binary_data = ""
    for pixel in pixels:
        for value in pixel:
            binary_data += str(value & 1)

    message = binary_to_text(binary_data)
    print("🔓 Hidden Message:")
    print(message)

if __name__ == "__main__":
    img_path = input("Enter encoded image path: ")
    decode_image(img_path)
