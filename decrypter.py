import os
import pyaes

## abrir o arquivo criptografado
file_name * 'teste.txt.ransomwaretroll'
file = open(file_name,'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remove um novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open(f'{new_file}','rb')
new_file.write(descrypt_data)
new_file.close()

