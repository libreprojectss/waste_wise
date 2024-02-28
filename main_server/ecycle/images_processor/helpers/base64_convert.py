from PIL import Image
import base64
from io import BytesIO

def ImageToBase64(im):
    buffered = BytesIO()
    im.save(buffered, format="PNG")  # Adjust the format based on your needs
    return base64.b64encode(buffered.getvalue()).decode('utf-8')
