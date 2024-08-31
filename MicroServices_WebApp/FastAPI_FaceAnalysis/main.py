import numpy as np 
import cv2
from src.face_analysis import AgeGenderEstimator , FaceAnalysis , RetinaFace
from fastapi import FastAPI , UploadFile , File
from fastapi.responses import JSONResponse



app = FastAPI()
face_analysis_obj = FaceAnalysis("models/det_10g.onnx" , "models/genderage.onnx")

@app.get("/")
def index():
    return {"hello":"world"}

 
# recieve image from webapp to analyze
@app.post("/faceanalysis")
async def analyze_face(file: UploadFile= File(...)):
    input_image = await file.read()
    numpy_array_image = np.frombuffer(input_image , np.uint8)
    cv2image = cv2.imdecode(numpy_array_image , cv2.IMREAD_COLOR )
    output_image, genders , ages =  face_analysis_obj.detect_age_gender(cv2image)
    result = {"genders":genders , "ages":ages }
    print(ages)
    return JSONResponse(result)

if __name__ == '__main__':
    app.run(port="5000" , debug=True)