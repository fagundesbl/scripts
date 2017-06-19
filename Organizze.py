#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil, os

print('Script para organizar arquivos')

# Pasta
sync = '/home/bfagundes/Arquivos'
documents = sync + '/Files/Documents'

caminhos = [os.path.join(sync, nome) for nome in os.listdir(sync)]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]

# Arquivos do google
gddoc = [arq for arq in arquivos if arq.lower().endswith(".gddoc")]
gdsheet = [arq for arq in arquivos if arq.lower().endswith(".gdsheet")]
pdf = [arq for arq in arquivos if arq.lower().endswith(".pdf")]
odt = [arq for arq in arquivos if arq.lower().endswith(".odt")]
docx = [arq for arq in arquivos if arq.lower().endswith(".docx")]

# Movendo os arquivos
for arq in gddoc:
	print(arq)
	shutil.move(arq, documents + '/docs/')
	
for arq in docx:
	print(arq)
	shutil.move(arq, documents + '/docs/')

for arq in odt:
	print(arq)
	shutil.move(arq, documents + '/docs/')

for arq in gdsheet:
	print(arq)
	shutil.move(arq, documents + '/sheets/')

for arq in pdf:
	print(arq)
	shutil.move(arq, documents + '/shelf/')

