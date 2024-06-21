from fastapi import FastAPI, UploadFile, File
from paddleocr import PaddleOCR
import uvicorn
import cv2
import numpy as np

app = FastAPI()


@app.post('/extract_text_info')
async def extract_text_info(files: UploadFile = File(...)):
    
    #Save the uploaded image temporarily
    contents = await files.read()

    nparr = np.fromstring(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    #frame = r'images\3.bmp'

    # Perform OCR on the uploaded image
    # Initialize PaddleOCR reader
    ocr = PaddleOCR()
    result = ocr.ocr(frame)

    # Extract and collect the detected text
    detected_text = [line[1][0] for res in result for line in res]

    # Find "UNITS PER YEAR" and get the previous value
    power_consumption = None
    for i, text in enumerate(detected_text):
        if text == 'UNITS PER YEAR':
            if i - 1 >= 0:
                power_consumption = detected_text[i - 1]
                print("power_consumption",power_consumption)

    # Find "Total Volume" and get the next value, only execute once
    total_volume = None
    total_volume_found = False
    for i, text in enumerate(detected_text):
        if text == 'Total Volume' and not total_volume_found:
            if i + 1 < len(detected_text):
                total_volume = detected_text[i + 1]
                total_volume_found = True
                print("total_volume",total_volume)

    return {"power_consumption": power_consumption, "total_volume": total_volume}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5001)