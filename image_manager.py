import PIL.ImageGrab
import PIL.Image
import uuid

import drawing_canvas
import config


class ImageManager:
    def __init__(self) -> None:
        self.image_format = 'png'

    def save_image_from_canvas(self, drawing_canvas_: drawing_canvas.DrawingCanvas, image_name: str) -> None:
        ps_img_name = config.POSTSCRIPT_IMAGES_FOLDER + config.POSTSCRIPT_IMAGE_NAME
        drawing_canvas_.get_canvas().postscript(file=ps_img_name)
        img = PIL.ImageGrab.grab(bbox=drawing_canvas_.get_canvas_rectangle_coordinates())

        # сохраняем изображение в его исходном размере
        image_file_name = config.IMG_FOLDER + self.__make_file_name(image_name)
        img.save(image_file_name, self.image_format)

        # изменяем размер изображения
        resized_image_file_name = config.DATASET_FOLDER + self.__make_file_name(image_name)
        self.resize_image((28, 28), image_file_name, resized_image_file_name)

    def __make_file_name(self, file_name: str) -> str:
        return '{0}_{1}.{2}'.format(file_name, uuid.uuid4().hex, self.image_format)

    def load_image(self) -> None:
        pass

    def resize_image(self, size: tuple, file_name: str, output_file_name: str) -> None:
        image = PIL.Image.open(file_name)
        image = image.resize(size, PIL.Image.ANTIALIAS)
        image.save(output_file_name)
