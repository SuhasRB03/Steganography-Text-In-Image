from PIL import Image
import base64

def to_binary(data):
    return ''.join(format(ord(char), '08b') for char in data)

def hide_text(img_path, text, output_path):
    # Encode text to base64
    encoded_text = base64.b64encode(text.encode()).decode()
    binary_text = to_binary(encoded_text + "<<<END>>>")
    
    img = Image.open(img_path).convert("RGB")
    pixels = list(img.getdata())

    new_pixels = []
    data_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if data_index < len(binary_text):
            r = (r & ~1) | int(binary_text[data_index])
            data_index += 1
        if data_index < len(binary_text):
            g = (g & ~1) | int(binary_text[data_index])
            data_index += 1
        if data_index < len(binary_text):
            b = (b & ~1) | int(binary_text[data_index])
            data_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    print("[✔] Text hidden in", output_path)

# === Main ===
if __name__ == "__main__":
    image_path = input("Enter the image path: ").strip()
    secret_text = input("Enter the text to hide: ").strip()
    output_path = input("Enter output image filename (e.g., output.png): ").strip()

    hide_text(image_path, secret_text, output_path)