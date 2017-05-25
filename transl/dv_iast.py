#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Transliterador  Devanāgarī >>> IAST
# Escrito por Caio Borges <caioaguida@gmail.com>

# Dicionário com correspondências entre a entrada em Devanāgarī Unicode e saída em IAST.

dv_iast_unicode = {'ट': 'ṭ', 'ण': 'ṇ', 'ऊ': 'ū', 'ऋ': 'ṛ',
                   'श': 'ś', 'द': 'd', 'उ': 'u', 'ग': 'g',
                   'ज': 'j', 'थ': 'th', 'अ': 'a', 'आ': 'ā',
                   'ञ': 'ñ', 'ब': 'b', 'ङ': 'ṅ', 'म': 'm',
                   'न': 'n', 'ः': 'ḥ', 'त': 't', 'ष': 'ṣ',
                   'छ': 'ch', 'ढ': 'ḍh', 'ठ': 'ṭh', 'क': 'k',
                   'इ': 'i', 'ख': 'kh', 'च': 'c', 'ध': 'dh',
                   'ऐ': 'ai', 'ह': 'h', 'घ': 'gh', 'व': 'v',
                   'ओ': 'o', ' ': ' ', 'ऽ': "'", 'ॐ': 'oṃ',
                   'ड': 'ḍ', 'ई': 'ī', 'ए': 'e', 'झ': 'jh',
                   'ऌ': 'ḷ', 'य': 'y', '।': '|', 'फ': 'ph',
                   'औ': 'au', 'ल': 'l', 'स': 's', 'भ': 'bh',
                   'प': 'p', 'ं': 'ṃ', 'र': 'r'}

# Dicionário específico para os diacríticos vocálicos.

dv_iast_diacriticos_vogais = {'ी': 'ī', 'े': 'e', 'ॄ': 'ṝ', 'ृ': 'ṛ',
               'ै': 'ai', 'ॢ': 'ḷ', 'ो': 'o', 'ौ': 'au',
               'ा': 'ā', 'ि': 'i', 'ु': 'u', 'ू': 'ū'}

# Listas para especificidades do Devanagari.

dv_iast_vogais = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']

dv_iast_consoantes = ['क', 'ख', 'ग', 'घ', 'ङ',
                 'च', 'छ', 'ज', 'झ', 'ञ',
                 'ट', 'ठ', 'ड', 'ढ', 'ण',
                 'त', 'थ', 'द', 'ध', 'न',
                 'प', 'फ', 'ब', 'भ', 'म',
                 'य', 'र', 'ल', 'व',
                 'श', 'ष', 'स', 'ह']

dv_iast_diacriticos = ['ं', 'ः', 'ऽ']
dv_iast_pontuacao = ['।', '।।']


# Função responsável pela conversão.


def conversor(entrada):

    entrada = "%s " % entrada
    saida = []

    for i in range(len(entrada)):
        c = entrada[i]

        if c not in dv_iast_unicode.keys() and c not in dv_iast_vogais:
            saida.append(c)
            continue

        if i == len(entrada)-2:
            break

        if c not in dv_iast_unicode and c in dv_iast_vogais:
            saida.append(dv_iast_diacriticos_vogais[c])
        elif c in dv_iast_consoantes:
            if entrada[i + 1] in dv_iast_diacriticos_vogais:
                saida.append(dv_iast_unicode[c])
            elif entrada[i + 1] == ' ' or entrada[i + 1] in dv_iast_consoantes:
                saida.append(dv_iast_unicode[c])
                saida.append('a')
            elif entrada[i + 1] in dv_iast_diacriticos or entrada[i + 1] in dv_iast_pontuacao:
                saida.append(dv_iast_unicode[c])
                saida.append('a')
            else:
                if entrada[i + 1] == '्':
                    saida.append(dv_iast_unicode[c])
                else:
                    print('epa')
        else:
            saida.append(dv_iast_unicode[c])

        for c in saida:
            if c == '्':
                saida.pop(saida.index(c))

    saida = ''.join(saida)
    saida = saida.strip()
    return saida

if __name__ == '__main__':
    conversor(input(">>>"))
