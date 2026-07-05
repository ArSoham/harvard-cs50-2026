"""blur.py
Applies a box blur filter to a sample image and writes the transformed output.
"""

from PIL import Image, ImageFilter


def main():
    before = Image.open("image.bmp")
    after = before.filter(ImageFilter.BoxBlur(10))
    after.save("out.bmp")


if __name__ == "__main__":
    main()
