from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/uploadimage/")
async def create_upload_image(image: UploadFile):
    return {"filename": image.filename}

# if __name__ == "__main__":
#     main()
