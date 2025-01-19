from fastapi import FastAPI, UploadFile
from pathlib import Path

UPLOAD_DIR = Path() / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI()


@app.post("/uploadimage/")
async def create_upload_image(image_upload: UploadFile):
    if image_upload.size == 0:
        return {"message": "File is empty"}

    image = await image_upload.read()
    save_path = UPLOAD_DIR / image_upload.filename
    with open(save_path, "wb") as file:
        file.write(image)
    return {"filename": image_upload.filename}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
