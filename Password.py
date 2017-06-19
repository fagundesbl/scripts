#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib, string, time, os

def sum(numbers):
    val = 0
    for idx in range(len(numbers)):
        val += int(numbers[idx])

    if val > 9:
        return (str(val))[1]
    else:
        return str(val)


def hash(val, key):
    h = hashlib.md5()
    h.update(val.encode('utf-8') + key.encode('utf-8'))
    return h.hexdigest()


def split(val,name):
    foo = ''
    for idx in range(len(val)):
        if val[idx].isdigit():
            foo += (str(int(val[idx]) - idx)).replace('-', '')

        elif type(val[idx]) is str:
            if val[idx - 1].isdigit():
                foo += ' '

            if name.find(val[idx]) == -1:
                foo += val[idx]
            else:
                foo += val[idx].upper()

            try:
                if val[idx + 1].isdigit():
                    foo += ' '
            except IndexError:
                pass

    return foo.split(' ')


def passwd(val):
    foo = ''
    for idx in range(len(val)):
        if foo.find(val[idx]) == -1:
            if val[idx].isdigit():
                foo += sum(val[idx])
            else:
                foo += val[idx]

    return foo


if __name__ == "__main__":
    site = input('Entre com o nome do site : ').lower().capitalize()
    key = input('Digite a chave de acesso : ')  # key = getpass.getpass('Digite a chave de acesso : ')
    num = int(input('Infome a variação: '))

    # Criando o hash
    if type(num) is int:
        key = hash(site, key * num)
    else:
        key = hash(site, key)

    # Separando as letras dos números
    key = split(key, site)

    # Obtendo a senha basica
    key = passwd(key)

    bar0 = "Az1" + key[0:4] + "$" + key[5:8] + "@" + "2BF"
    bar1 = passwd(split(hash(bar0, key),key))

    os.system('cls' if os.name == 'nt' else 'clear')
    print('SENHA E CHAVE DE ACESSO DO SITE %s (Variacao %s):' % (site,num))
    print('Senha de acesso  : %s ' % str(bar0))
    print('Chave            : %s ' % str(bar1))

    time.sleep(60)  # pause 5.5 seconds
