import base64

# DE PNG A B64 ********************************
with open('b64Entrada/git.png', 'rb') as imagefile:
    byteform=base64.b64encode(imagefile.read())

f=open('b64Salida/git.bin','wb')
f.write(byteform)
f.close()


print('imagen codificada con exito - b64Salida')
