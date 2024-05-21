import os
import pyaes

print('Digite somente o nome do arquivo encriptado: ')
archive = input()

print('Lendo o arquivo ...')

source = 'arquivos/' + f'{archive}' + '.txt.ransomwaretroll'
file = open(source, 'rb')
file_data = file.read()
file.close()

os.remove(source)

print('Excluindo o arquivo encriptado ...')

key = b"senhaparadesencp"

aes = pyaes.AESModeOfOperationCTR(key)

decrypto = aes.decrypt(file_data)

source_save = "arquivos/"

print('Escolha um novo nome para o arquivo: ')
new_name = input()

new_file = source_save + f'{new_name}' + '.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypto)
new_file.close()

print('Sucesso !')