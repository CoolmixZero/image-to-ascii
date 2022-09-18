import PIL.Image


class ImageToASCII:
    ASCII_CHARS = ['@', '%', '#', '*', '+', '=', '-', ';', ':', ',', '.']

    def __init__(self, image):
        self.image = image

    def get_image_data(self, new_width: int = 100):
        """
        Resizes, converts image and transforms pixels to ascii
        :param new_width: sets new width for the image
        :return: resized image
        """
        self.image = self.resize_image(new_width)
        self.image = self.convert_to_gray()
        self.image = self.pixels_to_ascii()
        return self.image

    def resize_image(self, new_width: int = 100):
        """
        Resizes image with a new width and height
        :param new_width: sets new width for the image
        :return: resized image
        """
        width, height = self.image.size
        ratio = height / width
        new_height = int(new_width * ratio)
        return self.image.resize((new_width, new_height))

    def convert_to_gray(self):
        """
        Converts image to black and white colors
        :return: converted image
        """
        return self.image.convert("L")

    def pixels_to_ascii(self):
        """
        Converts RGBA of pixels to ASCII characters
        :return: image characters
        """
        pixels = self.image.getdata()
        return "".join([self.ASCII_CHARS[pixel // 25] for pixel in pixels])


def main(path, new_width: int = 100):
    """
    Starts converting image to ASCII
    :param path: path to image
    :param new_width: sets new width for the image
    :return: None
    """
    try:
        img = PIL.Image.open(path)
        image = ImageToASCII(img)

        # convert image to ASCII
        new_image_data = image.get_image_data(new_width)

        # format
        pixel_count = len(new_image_data)
        ascii_image = "\n".join(new_image_data[i:(i + new_width)] for i in range(0, pixel_count, new_width))

        # print result
        print(ascii_image)

        # save image to .txt
        with open(f"{path[:-4]}.txt", "w") as f:
            f.write(ascii_image)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main('monkey.jpg', new_width)
