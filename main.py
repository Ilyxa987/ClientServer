from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
import os
import zipstream
import random

import uvicorn

app = FastAPI()

dir = "Files\\"

@app.get("/count")
async def Count():
    return str(len(os.listdir(dir)))


@app.get("/get_script")
async def get_script():
    return FileResponse("decode.py", media_type='application/octet-stream',filename="decode.py")


@app.get("/download")
async def download(num : int = 0):
    if num == 0 or num > len(os.listdir(dir)):
        return "Укажите другое количество файлов"

    def iterable(filename):
        with open(filename, mode="rb") as file_like:
            arr = file_like.read()
            sharr = bytearray()
            for i in range(len(arr)):
                sharr.append(arr[i] ^ 4)
            yield bytes(sharr)
            """arr = "abcdef\n"
            sharr = ""
            for i in range(len(arr)):
                sharr += chr(ord(arr[i]) ^ 4)
            yield bytes(sharr, 'utf-8')"""

    dirlist = os.listdir(dir)
    randomnumbers = list()
    for i in range(num):
        randomnumbers.append(random.choice(dirlist))
        dirlist.remove(randomnumbers[len(randomnumbers) - 1])
    z = zipstream.ZipFile()
    for data in randomnumbers:
        z.write_iter(f"{dir}{data}", iterable(f"{dir}{data}"))

    return StreamingResponse(z)


if __name__ == '__main__':
    uvicorn.run(app,
                host='127.0.0.1',
                port=80)
