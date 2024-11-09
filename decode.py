import os

dir = input("Введите распакованную директорию:\n")

for i in range(len(os.listdir(dir))):
    arr = b''
    with open(f'{dir}\\{os.listdir(dir)[i]}', 'rb') as f:
        arr = f.read()
    sharr = bytearray()
    for j in range(len(arr)):
        sharr.append(arr[j] ^ 4)
    with open(f'{dir}\\{os.listdir(dir)[i]}', 'wb') as f:
        f.write(sharr)