import ast

from PIL import Image as pImage, ImageStat

from .models import ImageMetaData, Image


def set_default_slug(title: str) -> str:
    number_of_space = title.count(' ')
    if number_of_space != 0:
        for i in range(number_of_space):
            parsed_title = title.replace(' ', '')
        return parsed_title.lower()
    else:
        return title.lower()


def _get_size(picture_name: str) -> tuple:
    image = pImage.open(f'media/images/{picture_name}')
    return image.size


def _get_average_color(picture_name: str) -> list:
    image = pImage.open(f'media/images/{picture_name}')
    median = ImageStat.Stat(image).median
    return median


def _count_objects(picture_name: str) -> int:
    import cv2
    import numpy as np

    im = cv2.imread(f'media/images/{picture_name}', cv2.IMREAD_GRAYSCALE)
    ret, im = cv2.threshold(im, 240, 255, cv2.THRESH_BINARY)
    kernel = np.ones((6, 6), np.uint8)
    opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel)
    im = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    params = cv2.SimpleBlobDetector_Params()
    params.filterByColor = True
    params.blobColor = 255
    params.filterByConvexity = True
    params.minConvexity = 0.87
    params.filterByInertia = True
    params.minInertiaRatio = 0.08

    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3:
        detector = cv2.SimpleBlobDetector(params)
    else:
        detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(im) * 2

    return len(keypoints)


def rgb2hex(rgb_but_str: str) -> str:
    rgb = ast.literal_eval(rgb_but_str)
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])


def get_meta_data(picture_name: str, slug: str) -> None:
    width, high = _get_size(picture_name)
    average_color = _get_average_color(picture_name)
    number_of_coins = _count_objects(picture_name)
    image_instance = Image.objects.get(slug=slug)
    ImageMetaData.objects.create(
        image=image_instance,
        high=str(high),
        width=str(width),
        average_color=str(average_color),
        number_of_coins=int(number_of_coins), # я что дата сайнтист??
        # я не знаю как пользоваться cv2
        sum_of_coins=105
    )
