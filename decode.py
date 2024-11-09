import os

dir = input("Введите распакованную директорию:\n")
key = int(input("Введите ключ:\n"))

for i in range(len(os.listdir(dir))):
    arr = b''
    with open(f'{dir}\\{os.listdir(dir)[i]}', 'rb') as f:
        arr = f.read()
    sharr = bytearray()
    for j in range(len(arr)):
        sharr.append(arr[j] ^ key)
    with open(f'{dir}\\{os.listdir(dir)[i]}', 'wb') as f:
        f.write(sharr)