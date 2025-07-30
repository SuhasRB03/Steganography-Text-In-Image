from PIL import Image

def extract_text(img_path):
    img = Image.open(img_path)
    pixels = list(img.getdata())

    binary_text = ""
    for pixel in pixels:
        for value in pixel[:3]:
            binary_text += str(value & 1)

    chars = [binary_text[i:i+8] for i in range(0, len(binary_text), 8)]
    message = ""
    for byte in chars:
        char = chr(int(byte, 2))
        message += char
        if message.endswith("<<<END>>>"):
            break
    return message.replace("<<<END>>>", "")

# Example
secret = extract_text("output.png")
print("[🔓] Hidden message:", secret)