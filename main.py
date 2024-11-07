from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import os
import zipstream
import random

import uvicorn

app = FastAPI()

dir = "Files\\"

@app.get("/count")
async def Count():
    return str(len(os.listdir(dir)))


@app.get("/download")
async def download(num : int = 0):
    if num == 0 or num > len(os.listdir(dir)):
        return "Укажите другое количество файлов"

    dirlist = os.listdir(dir)
    randomnumbers = list()
    for i in range(num):
        randomnumbers.append(random.choice(dirlist))
        dirlist.remove(randomnumbers[len(randomnumbers) - 1])
    z = zipstream.ZipFile()
    for data in randomnumbers:
        z.write(f"Files\\{data}")

    return StreamingResponse(z)


if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
