from PIL import Image
from utils import text_to_binary

def encode_image(image_path, secret_text, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    pixels = list(img.getdata())

    binary_secret = text_to_binary(secret_text)
    data_index = 0
    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel

        if data_index < len(binary_secret):
            r = (r & ~1) | int(binary_secret[data_index])
            data_index += 1
        if data_index < len(binary_secret):
            g = (g & ~1) | int(binary_secret[data_index])
            data_index += 1
        if data_index < len(binary_secret):
            b = (b & ~1) | int(binary_secret[data_index])
            data_index += 1

        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    print("✅ Message hidden successfully!")

if __name__ == "__main__":
    img_path = input("Enter input image path: ")
    message = input("Enter secret message: ")
    out_path = input("Enter output image path: ")

    encode_image(img_path, message, out_path)
