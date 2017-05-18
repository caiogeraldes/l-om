#!/usr/bin/python
# -*- coding: utf-8 -*-

# Transliterador Harvard-Kyoto >> IAST
# Escrito por Caio Borges <caioaguida@gmail.com>

# Dicionário com correspondências entre a entrada em alfabeto Latino e a saída em IAST Unicode.

hk_iast_unicode = {
    'M': 'ṃ',
    'H': 'ḥ',
    'a': 'a',
    'A': 'ā',
    'i': 'i',
    'I': 'ī',
    'u': 'u',
    'U': 'ū',
    'R': 'ṛ',
    'lR': 'ḷ',
    'e': 'e',
    'o': 'o',
    'k': 'k',
    'g': 'g',
    'G': 'ṅ',
    'c': 'c',
    'j': 'j',
    'J': 'ñ',
    'T': 'ṭ',
    'D': 'ḍ',
    'N': 'ṇ',
    't': 't',
    'd': 'd',
    'n': 'n',
    'p': 'p',
    'b': 'b',
    'm': 'm',
    'y': 'y',
    'r': 'r',
    'l': 'l',
    'v': 'v',
    'z': 'ś',
    'S': 'ṣ',
    's': 's',
    'h': 'h',
    "'": '\'',
    ' ': ' ',
    '|': '\u0964',
    '||': '\u0964'
                 }


# Função responsável pela conversão.

def conversor(entrada):
    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada

    saida = []
    for i in range(len(entrada)):
        c = entrada[i]

        if c not in hk_iast_unicode.keys():
            saida.append(c)
            continue

        if c == 'l' and entrada[i + 1] == 'R':
            saida.append(hk_iast_unicode['lR'])
        elif c == 'R' and entrada[i - 1] == 'l':
            continue
        else:
            saida.append(hk_iast_unicode[c])
    saida = ''.join(saida)
    saida = saida.strip()
    return saida

if __name__ == '__main__':
    conversor(input(">>>"))
