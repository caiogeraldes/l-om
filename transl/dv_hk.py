#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Transliterador  Devanāgarī >>> Harvard-Kyoto
# Escrito por Caio Borges <caioaguida@gmail.com>

# Dicionário com correspondências entre a entrada em Devanāgarī Unicode e saída em Harvard Kyoto.

dv_hk_unicode = {'ट': 'T', 'ण': 'N', 'ऊ': 'U', 'ऋ': 'R',
                 'श': 'z', 'द': 'd', 'उ': 'u', 'ग': 'g',
                 'ज': 'j', 'थ': 'th', 'अ': 'a', 'आ': 'A',
                 'ञ': 'J', 'ब': 'b', 'ङ': 'G', 'म': 'm',
                 'न': 'n', 'ः': 'H', 'त': 't', 'ष': 'S',
                 'छ': 'ch', 'ढ': 'Dh', 'ठ': 'Th', 'क': 'k',
                 'इ': 'i', 'ख': 'kh', 'च': 'c', 'ध': 'dh',
                 'ऐ': 'ai', 'ह': 'h', 'घ': 'gh', 'व': 'v',
                 'ओ': 'o', ' ': ' ', 'ऽ': "'", 'ॐ': 'oM',
                 'ड': 'D', 'ई': 'I', 'ए': 'e', 'झ': 'jh',
                 'ऌ': 'lR', 'य': 'y', '।': '|', 'फ': 'ph',
                 'औ': 'au', 'ल': 'l', 'स': 's', 'भ': 'bh',
                 'प': 'p', 'ं': 'M', 'र': 'r'}

# Dicionário específico para os diacríticos vocálicos.

dv_c_vogais = {'ी': 'I', 'े': 'e', 'ॄ': 'RR', 'ृ': 'R',
               'ै': 'ai', 'ॢ': 'lR', 'ो': 'o', 'ौ': 'au',
               'ा': 'A', 'ि': 'i', 'ु': 'u', 'ू': 'U'}

# Listas para especificidades do Devanagari.

dv_vogais = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']

dv_consoantes = ['क', 'ख', 'ग', 'घ', 'ङ',
                 'च', 'छ', 'ज', 'झ', 'ञ',
                 'ट', 'ठ', 'ड', 'ढ', 'ण',
                 'त', 'थ', 'द', 'ध', 'न',
                 'प', 'फ', 'ब', 'भ', 'म',
                 'य', 'र', 'ल', 'व',
                 'श', 'ष', 'स', 'ह']

dv_diacriticos = ['ं', 'ः', 'ऽ']
dv_pontuacao = ['।', '।।']


# Função responsável pela conversão.


def conversor(entrada):
    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada

    saida = []
    for i in range(len(entrada)):
        c = entrada[i]

        if c not in dv_hk_unicode.keys() and c not in dv_vogais:
            saida.append(c)
            continue

        if i == len(entrada)-2:
            break

        if c not in dv_hk_unicode and c in dv_vogais:
            saida.append(dv_c_vogais[c])
        elif c in dv_consoantes:
            if entrada[i + 1] in dv_c_vogais:
                saida.append(dv_hk_unicode[c])
            elif entrada[i + 1] == ' ' or entrada[i + 1] in dv_consoantes:
                saida.append(dv_hk_unicode[c])
                saida.append('a')
            elif entrada[i + 1] in dv_diacriticos or entrada[i + 1] in dv_pontuacao:
                saida.append(dv_hk_unicode[c])
                saida.append('a')
            else:
                if entrada[i + 1] == '्':
                    saida.append(dv_hk_unicode[c])
                else:
                    print('epa')
        else:
            saida.append(dv_hk_unicode[c])

        for c in saida:
            if c == '्':
                saida.pop(saida.index(c))

    saida = ''.join(saida)
    saida = saida.strip()
    return saida

if __name__ == '__main__':
    conversor(input(">>>"))
