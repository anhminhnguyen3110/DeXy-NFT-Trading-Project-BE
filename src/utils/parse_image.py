import base64


def parse_image_to_base64(image) -> str:
    image_base64 = None
    if image:
        image_base64 = base64.b64encode(image).decode("utf-8")
    return image_base64
