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
        try:
            char = chr(int(byte, 2))
            message += char
            if message.endswith("<<<END>>>"):
                break
        except ValueError:
            break

    return message.replace("<<<END>>>", "")

# === Main ===
if __name__ == "__main__":
    image_path = input("Enter the image name (ex:- output.png): ").strip()
    secret = extract_text(image_path)
    print("[🔓] Hidden message:", secret)