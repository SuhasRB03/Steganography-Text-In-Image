# Steganography-Text-In-Image
Steganography – Hide Text in Images Using Python
A lightweight Python project that demonstrates how to hide secret messages inside image files using the Least Significant Bit (LSB) steganography technique. The messages are first encoded using Base64 to add a simple layer of obfuscation. This project is great for learning about digital forensics, cybersecurity, and covert communication.

# Features

- Hides secret text inside images using the LSB method
- Extracts hidden messages from stego-images
- Base64-encodes the message for light obfuscation
- Supports standard image formats like PNG and JPG
- Clean, beginner-friendly code structure with comments
- Command-line interface (no GUI)

# How It Works
- The message you enter is encoded with base64 and appended with a special delimiter: <<<END>>>.
- This encoded string is converted to binary (0s and 1s).
- Each bit is embedded into the least significant bit of the red, green, or blue color channels of the image pixels.
- To retrieve the hidden message, the script scans the LSBs of all pixels, rebuilds the binary string, converts it back to characters, and decodes the Base64 string up to the <<<END>>> marker.

# Tools & Technologies
- Language: Python 3.x
- Libraries:
- [Pillow (PIL)] – for image processing
- Base64 – built-in Python module for encoding/decoding

# Decode the Secret Message
echo "your_base64_string" | base64 -d
