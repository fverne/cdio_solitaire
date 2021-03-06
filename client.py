# Group 1 - CDIO Project, 21-06-21

# Example client. Won't be used in the final product.
import base64

import requests as r
import json
from pprint import pprint


def send_request(image='images/3init1.jpg'):
    files = open(image, "rb")  # pass the files here

    # Convert to base64
    imgBytes = files.read()
    b64imgBytes = base64.b64encode(imgBytes).decode()

    apiData = {'image': b64imgBytes}

    res = r.post("http://localhost:8000/",
                 json=apiData)

    pprint(json.loads(res.text))


if __name__ == '__main__':
    send_request()
