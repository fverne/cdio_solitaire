from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse

from PIL import Image
from io import BytesIO
import torch

from convert import getboardDTO
from preprocess import preprocess

app = FastAPI()


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


# Takes image file, returns SolitaireBoard DTO
@app.post("/")
async def processrequest(file: UploadFile = File(...),
                         model_name: str = Form(...)):

    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name + '.pt')
    results = model(Image.open(BytesIO(await file.read())))
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
