import shutil
import os

# Pasta
sync = '/home/bfagundes/Sync'
documents = sync + '/Files/Documents'

caminhos = [os.path.join(sync, nome) for nome in os.listdir(sync)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

# Arquivos do google
gddoc = [arq for arq in arquivos if arq.lower().endswith(".gddoc")]
gdsheet = [arq for arq in arquivos if arq.lower().endswith(".gdsheet")]
pdf = [arq for arq in arquivos if arq.lower().endswith(".pdf")]
odt = [arq for arq in arquivos if arq.lower().endswith(".odt")]

# Movendo os arquivos
for arq in gddoc:
    shutil.move(arq, documents + '/docs')

for arq in odt:
    shutil.move(arq, documents + '/docs')

for arq in gdsheet:
    shutil.move(arq, documents + '/sheets')

for arq in pdf:
    shutil.move(arq, documents + '/shelf')

