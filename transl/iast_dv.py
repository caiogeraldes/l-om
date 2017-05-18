#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""" Transliterador Harvard-Kyoto >>> Devanāgarī
Escrito por Caio Borges <caioaguida@gmail.com>"""

# Dicionário com correspondências entre a entrada em alfabeto Latino e a saída em Devanāgarī Unicode.

iast_dv_unicode = {'ṃ': '\u0902', 'ḥ': '\u0903',
                   'a': '\u0905', 'ā': '\u0906',
                   'i': '\u0907', 'ī': '\u0908',
                   'u': '\u0909', 'ū': '\u090A',
                   'ṛ': '\u090B', 'ṝ': 'ॠ',
                   'ḷ': '\u090C',
                   'e': '\u090F', 'ai': '\u0910',
                   'o': '\u0913', 'au': '\u0914',
                   'k': '\u0915', 'kh': '\u0916', 'g': '\u0917', 'gh': '\u0918', 'ṅ': '\u0919',
                   'c': '\u091A', 'ch': '\u091B', 'j': '\u091C', 'jh': '\u091D', 'ñ': '\u091E',
                   'ṭ': '\u091F', 'ṭh': '\u0920', 'ḍ': '\u0921', 'ḍh': '\u0922', 'ṇ': '\u0923',
                   't': '\u0924', 'th': '\u0925', 'd': '\u0926', 'dh': '\u0927', 'n': '\u0928',
                   'p': '\u092A', 'ph': '\u092B', 'b': '\u092C', 'bh': '\u092D', 'm': '\u092E',
                   'y': '\u092F', 'r': '\u0930', 'l': '\u0932', 'v': '\u0935',
                   'ś': '\u0936', 'ṣ': '\u0937', 's': '\u0938', 'h': '\u0939',
                   "'": '\u093D', 'oṃ': '\u0950', ' ': ' ', '|': '\u0964', '||': '\u0964'
                   }

# Dicionário específico para os diacríticos vocálicos.

iast_c_vogais = {'ā': '\u093E', 'a': '',
                 'i': '\u093F', 'ī': '\u0940',
                 'u': '\u0941', 'ū': '\u0942',
                 'ṛ': '\u0943', 'ṝ': '\u0944',
                 'ḷ': '\u0962',
                 'e': '\u0947', 'ai': '\u0948',
                 'o': '\u094b', 'au': '\u094C'}

# Listas para especificidades do Devanagari.

iast_vogais = ['ā', 'a', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'e', 'ai', 'o', 'au']
iast_consoantes = ['k', 'g', 'ṅ', 'c', 'j', 'ñ',
                   'ṭ', 'ḍ', 'ṇ', 't', 'd', 'n',
                   'p', 'b', 'm', 'y', 'r', 'l', 'v',
                   'ś', 'ṣ', 's', 'h']
c_especiais = ['ṅ', 'ñ', 'ṇ', 'n',
               'm', 'y', 'r', 'l', 'v',
               'ś', 'ṣ', 's']
iast_diacriticos = ['ṃ', 'ḥ', '\'']
iast = ['|', '||']


def conversor(entrada):
    entrada = "%s " % entrada
    saida = []
    i = -1

    for letra in entrada:
            i += 1
            if letra not in iast_dv_unicode:
                saida.append(letra)
            else:
                if letra in iast_vogais:
                    if letra == 'a':
                        if entrada[i + 1] == 'i':
                            if entrada[i - 1] in iast_consoantes:
                                saida.append(iast_c_vogais['ai'])
                            else:
                                saida.append(iast_dv_unicode['ai'])
                        elif entrada[i + 1] == 'u':
                            if entrada[i - 1] in iast_consoantes:
                                saida.append(iast_c_vogais['au'])
                            else:
                                saida.append(iast_dv_unicode['au'])
                        else:
                            if entrada[i - 1] in iast_consoantes:
                                saida.append('')
                            else:
                                saida.append(iast_dv_unicode[letra])
                    elif letra == 'i' or letra == 'u':
                        if entrada[i - 1] == 'a':
                            continue
                        else:
                            if entrada[i - 1] in iast_consoantes:
                                saida.append(iast_c_vogais[letra])
                            else:
                                saida.append(iast_dv_unicode[letra])
                    else:
                        if entrada[i - 1] in iast_consoantes:
                            saida.append(iast_c_vogais[letra])
                        else:
                            saida.append(iast_dv_unicode[letra])
                elif letra in iast_consoantes:
                    if entrada[i + 1] == 'h' and letra not in c_especiais:
                        saida.append(iast_dv_unicode['%sh' % letra])
                    elif letra == 'h' and entrada[i - 1] in iast_consoantes:
                        continue
                    elif entrada[i + 1] not in iast_vogais:
                        saida.append(iast_dv_unicode[letra])
                        saida.append('\u094D')
                    else:
                        saida.append(iast_dv_unicode[letra])
                else:
                    saida.append(iast_dv_unicode[letra])

    saida = "".join(saida)
    saida = saida.strip()
    return saida

if __name__ == '__main__':
    conversor(input(">>>"))
