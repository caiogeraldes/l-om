#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Transliterador Harvard-Kyoto >> IAST
# Escrito por Caio Borges <caioaguida@gmail.com>

# Dicionário com correspondências entre a entrada em alfabeto Latino e a saída em IAST Unicode.

iast_hk_unicode = {'i': 'i', 'p': 'p', "'": "'",
                   'u': 'u', 'ś': 'z', 'k': 'k',
                   'ñ': 'J', 'n': 'n', 't': 't',
                   'r': 'r', 'e': 'e', ' ': ' ',
                   'o': 'o', 'ā': 'A', 'ḥ': 'H',
                   'm': 'm', 'a': 'a', 'c': 'c',
                   'ḍ': 'D', 'ū': 'U', '।': '||',
                   'h': 'h', 'b': 'b', 'j': 'j',
                   'ṅ': 'G', 'g': 'g', 'l': 'l',
                   'ṇ': 'N', 'd': 'd', 'ṃ': 'M',
                   'y': 'y', 'v': 'v', 'ṣ': 'S',
                   'ṛ': 'R', 'ī': 'I', 'ḷ': 'lR',
                   's': 's', 'ṭ': 'T'}

def conversor(entrada):
    saida = []
    for letra in entrada:
        if letra not in iast_hk_unicode:
            saida.append(letra)
        else:
            saida.append(letra(iast_hk_unicode[letra]))

    saida = ''.join(saida)
    return(saida)

if __name__ == "__main__":
    conversor(">>>")
