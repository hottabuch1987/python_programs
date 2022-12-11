import pyAesCrypt
password = input('Ведите пароль для шифрования файла: ')

#encypt
pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

#decypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)