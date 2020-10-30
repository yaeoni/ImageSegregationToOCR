from google.protobuf.json_format import MessageToDict
import os, io
import json

from imgSeg import imgSeg

def detect_document(path):
    result = []
    count = imgSeg(path)
    print(count)
    count=5
    for i in range(count, 0, -1):
        path = os.path.join(os.path.dirname(__file__),
        './output/Img'+str(i)+'.jpg')

        """Detects document features in an image."""
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()

        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = vision.types.Image(content=content)

        response = client.document_text_detection(image=image)

        #data = json.dumps(response.text_annotations)
        #print(data.get("description"))

        response = MessageToDict(response, preserving_proto_field_name = True)
        data = response['text_annotations']
        data = data[0]
        data = data['description']
        temp ={"name": (5-i)+1, "contents":data}
        result.append(temp)
    print(result)


"""
for i in range(count,1,-1):
    file_name = os.path.join(
        os.path.dirname(__file__),
        './output/Img'+str(i)+'.jpg')

    detect_document(file_name)
"""

a = detect_document("http://gi.esmplus.com/orgastore/img/hobak_total.jpg")
