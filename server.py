# Group 1 - CDIO Project, 21-06-21

import base64
import io

import torch
from PIL import Image
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from convert import getboardDTO
from preprocess import preprocess
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:8000",
        "http://localhost:8080",
        "http://localhost:8082",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Converts the results from the model to a JSON, which we will convert to a DTO later.
def modelresults(results, model):
    return [
        [
            {
                "class": int(pred[5]),
                "class_name": model.model.names[int(pred[5])],
                "normalized_box": pred[:4].tolist(),
                "confidence": float(pred[4]),
            }
            for pred in result
        ]
        for result in results.xyxyn
    ]


# HHTP get, for debugging
@app.get("/")
def home(request: Request):
    '''
    Returns barebones HTML form allowing the user to select a file and model
    '''

    html_content = '''
<form method="post" enctype="multipart/form-data">
  <div>
    <label>Upload Image</label>
    <input name="file" type="file" multiple>
    <div>
      <label>Select YOLO Model</label>
      <select name="model_name">
        <option>yolov5s6</option>
        <option>yolov5m6</option>
      </select>
    </div>
  </div>
  <button type="submit">Submit</button>
</form>
'''

    return HTMLResponse(content=html_content, status_code=200)


class ImageModel(BaseModel):
    image: str


# Takes b64 encoded image file (param name 'file'), returns SolitaireBoard DTO
@app.post("/")
async def processrequest(image: ImageModel):

    # Loads the yolov5 model
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5m6.pt')

    # runs the model on the image
    decodedtest = base64.b64decode(image.image)
    iostream = io.BytesIO(decodedtest)
    imageopener = Image.open(iostream)
    results = model(imageopener)

    # Saves the results
    json_results = modelresults(results, model)

    # Checks if 3 instances of a card appears, which should never happen
    if not preprocess(json_results):
        return False

    # Returns the SolitaireBoard DTO
    return getboardDTO(json_results)


if __name__ == '__main__':
    import uvicorn

    app_str = 'server:app'
    uvicorn.run(app_str, host='localhost', port=8000, reload=False, workers=1)
