import PIL.Image


class TransformImage:

    def __init__(self, path: str, *, new_width: int = 100):
        self.path = path
        self.image: PIL.Image = self._open_image()
        self.new_width = new_width
        self.ascii_chars: list = []

    def _open_image(self) -> PIL.Image:
        return PIL.Image.open(self.path)

    @staticmethod
    def get_ascii_chars(chars: str) -> list:
        return [char for char in chars]

    @staticmethod
    def reverse_ascii_chars(chars: str | list) -> list:
        return [char for char in reversed(chars)]

    @staticmethod
    def print_ascii_image(ascii_image: str) -> None:
        print(ascii_image)

    def save_ascii_image(self, ascii_image: str) -> None:
        with open(f"{self.path[:-4]}.txt", "w") as f:
            f.write(ascii_image)

    def get_image_data(self, ascii_chars: list) -> PIL.Image:
        self.image = self._resize_image()
        self.image = self._convert_to_gray()
        self.image = self._pixels_to_ascii(ascii_chars)
        return self.image

    def _resize_image(self) -> PIL.Image:
        width, height = self.image.size
        ratio = height / width
        new_height = int(self.new_width * ratio)
        return self.image.resize((self.new_width, new_height))

    def _convert_to_gray(self) -> PIL.Image:
        return self.image.convert("L")

    def _pixels_to_ascii(self, ascii_chars: list) -> str:
        pixels = self.image.getdata()
        return "".join([ascii_chars[pixel // 25] for pixel in pixels])

    def format_image(self, new_image_data, *, sep='\n') -> str:
        pixel_count = len(new_image_data)
        return sep.join(
            new_image_data[i:(i + self.new_width)]
            for i in range(0, pixel_count, self.new_width))


def main(path: str, new_width: int) -> None:
    try:
        image = TransformImage(path, new_width=new_width)

        # convert image to ASCII
        ascii_chars = image.get_ascii_chars("@%#*+=-;:,.")  # image.reverse_ascii_chars() if needed
        new_image_data = image.get_image_data(ascii_chars)

        # format
        ascii_image = image.format_image(new_image_data)

        # print result
        image.print_ascii_image(ascii_image)

        # save image to .txt
        image.save_ascii_image(ascii_image)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main('monkey.jpg', new_width=300)
