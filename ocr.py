import os, io

def detect_text(path):
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    print(texts[0].description)

file_name = os.path.join(
    os.path.dirname(__file__),
    './output/Img4.jpg')

detect_text(file_name)
