from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

import uvicorn

app = FastAPI()

dir = "Files"

@app.get("/count")
async def Count():
    return str(len(os.listdir(dir)))

@app.get("/download")
async def download(num : int = 0):
    if num < 0 or num >= len(os.listdir(dir)):
        return "Укажите другое количество файлов"
    return FileResponse(f"{dir}\\{os.listdir(dir)[num]}", filename=os.listdir(dir)[num])



if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
