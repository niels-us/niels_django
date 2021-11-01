import base64

# #DE B64 A PNG *******************************
file=open('b64Salida/git.bin', 'rb')
byte=file.read()
file.close()

fh= open('b64Retorn/git.png', 'wb')
fh.write(base64.b64decode((byte)))
fh.close()

print('imagen decodificada con exito - b64Retorn')
