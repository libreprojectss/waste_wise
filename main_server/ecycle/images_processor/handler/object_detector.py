from PIL import Image
from ultralytics import YOLO
# from image_processor.handler.save_result import save_image
import threading
from django.conf import settings
from PIL import Image
from django.core.files.base import ContentFile
from images_processor.models import resultImage
from images_processor.helpers.base64_convert import ImageToBase64
import base64

import os
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'trained_model/best.pt')


def save_image(results,imageObj):
    for r in results:
        im_array = r.plot()  
        
        im = Image.fromarray(im_array[..., ::-1])

        image_data = ImageToBase64(im)

        decoded_image = ContentFile(base64.b64decode(image_data.encode()), name=f'{imageObj.id}image.png')

        
        result_image = resultImage(image=decoded_image, result_of=imageObj)
        result_image.save()
        
        return result_image



def detect_object(imageObj):
    # Load a pretrained YOLOv8n model
    image_link=settings.BACKEND_URL+imageObj.image.url
    model = YOLO(model_path)

    # Define path to the image file
    print(image_link)
    source = image_link

    # Run inference on the source
    results = model.predict(source)  # list of Results objects

    names = model.names
    a=set()

    # print(results[0].names) # To determine total category made for detection
    # threading.Thread(target=save_image, args=(results,)).start()
    result=save_image(results,imageObj)
    # Show the results
    for r in results:
            for c in r.boxes.cls:
                #  print(names[int(c)]) # get class name corrosponding to class number detected
                a.add(names[int(c)]) # add to set object


    for item in a:
         print(item) # print detected object uniquely
    return {"result":list(a),"image":settings.BACKEND_URL+result.image.url}

# detect_object()