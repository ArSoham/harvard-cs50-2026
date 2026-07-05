"""edges.py
Applies an edge detection filter to an image and saves the result."""

from PIL import Image, ImageFilter


def main():
    before = Image.open("image.bmp")
    after = before.filter(ImageFilter.FIND_EDGES)
    after.save("out.bmp")


if __name__ == "__main__":
    main()
