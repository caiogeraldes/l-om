#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""""" Transliterador Harvard-Kyoto >>> Devanāgarī
Escrito por Caio Borges <caioaguida@gmail.com>"""

# Dicionário com correspondências entre a entrada em alfabeto Latino e a saída em Devanāgarī Unicode.

hk_dv_unicode = {'M': '\u0902', 'H': '\u0903',
                 'a': '\u0905', 'A': '\u0906', 'i': '\u0907', 'I': '\u0908',
                 'u': '\u0909', 'U': '\u090A', 'R': '\u090B', 'RR': '\u0960', 'lR': '\u090C',
                 'e': '\u090F', 'ai': '\u0910', 'o': '\u0913', 'au': '\u0914',
                 'k': '\u0915', 'kh': '\u0916', 'g': '\u0917', 'gh': '\u0918', 'G': '\u0919',
                 'c': '\u091A', 'ch': '\u091B', 'j': '\u091C', 'jh': '\u091D', 'J': '\u091E',
                 'T': '\u091F', 'Th': '\u0920', 'D': '\u0921', 'Dh': '\u0922', 'N': '\u0923',
                 't': '\u0924', 'th': '\u0925', 'd': '\u0926', 'dh': '\u0927', 'n': '\u0928',
                 'p': '\u092A', 'ph': '\u092B', 'b': '\u092C', 'bh': '\u092D', 'm': '\u092E',
                 'y': '\u092F', 'r': '\u0930', 'l': '\u0932', 'v': '\u0935',
                 'z': '\u0936', 'S': '\u0937', 's': '\u0938', 'h': '\u0939',
                 "'": '\u093D', 'oM': '\u0950', ' ': ' ',  '|': '\u0964', '||': '\u0964'
                 }

# Dicionário específico para os diacríticos vocálicos.

hk_c_vogais = {'A': '\u093E', 'a': '',
               'i': '\u093F', 'I': '\u0940',
               'u': '\u0941', 'U': '\u0942',
               'R': '\u0943', 'RR': '\u0944',
               'lR': '\u0962',
               'e': '\u0947', 'ai': '\u0948',
               'o': '\u094b', 'au': '\u094C'}

# Listas para especificidades do Devanagari.

hk_vogais = ['A', 'a', 'i', 'I', 'u', 'U',
             'R', 'RR',
             'lR', 'e', 'ai', 'o', 'au']
hk_consoantes = ['k', 'g', 'G', 'c', 'j', 'J',
                 'T', 'D', 'N', 't', 'd', 'n',
                 'p', 'b', 'm', 'y', 'r', 'l', 'v',
                 'z', 'S', 's', 'h']
c_especiais = ['G', 'J', 'N', 'n',
               'm', 'y', 'r', 'l', 'v',
               'z', 'S', 's']
hk_diacriticos = ['M', 'H', '\'']
hk_pontuacao = ['|', '||']


def conversor(entrada):
    entrada = "%s " % entrada
    saida = []
    i = -1

    for letra in entrada:
            i += 1
            if letra not in hk_dv_unicode:
                saida.append(letra)
            else:
                if letra in hk_vogais:
                    if letra == 'a':
                        if entrada[i + 1] == 'i':
                            if entrada[i - 1] in hk_consoantes:
                                saida.append(hk_c_vogais['ai'])
                            else:
                                saida.append(hk_dv_unicode['ai'])
                        elif entrada[i + 1] == 'u':
                            if entrada[i - 1] in hk_consoantes:
                                saida.append(hk_c_vogais['au'])
                            else:
                                saida.append(hk_dv_unicode['au'])
                        else:
                            if entrada[i - 1] in hk_consoantes:
                                saida.append('')
                            else:
                                saida.append(hk_dv_unicode[letra])
                    elif letra == 'i' or letra == 'u':
                        if entrada[i - 1] == 'a':
                            continue
                        else:
                            if entrada[i - 1] in hk_consoantes:
                                saida.append(hk_c_vogais[letra])
                            else:
                                saida.append(hk_dv_unicode[letra])
                    elif letra == 'R':
                        if entrada[i + 1] == 'R':
                            if entrada[i - 1] in hk_consoantes:
                                saida.append(hk_c_vogais['RR'])
                            else:
                                saida.append(hk_dv_unicode['RR'])
                        elif entrada[i - 1] == 'R' or entrada[i - 1] == 'l':
                            continue
                        else:
                            if entrada[i - 1] in hk_consoantes:
                                saida.append(hk_c_vogais[letra])
                            else:
                                saida.append(hk_dv_unicode[letra])
                    else:
                        if entrada[i - 1] in hk_consoantes:
                            saida.append(hk_c_vogais[letra])
                        else:
                            saida.append(hk_dv_unicode[letra])
                elif letra in hk_consoantes:
                    if letra == 'l' and entrada[i + 1] == 'R':
                        if entrada[i - 1] in hk_consoantes:
                            saida.append(hk_c_vogais['lR'])
                        else:
                            saida.append(hk_dv_unicode['lR'])
                    elif entrada[i + 1] == 'h' and letra not in c_especiais:
                        saida.append(hk_dv_unicode['%sh' % letra])
                    elif entrada[i] == 'h' and entrada[i - 1] in hk_consoantes:
                        continue
                    elif entrada[i + 1] not in hk_vogais:
                        saida.append(hk_dv_unicode[letra])
                        saida.append('\u094D')
                    else:
                        saida.append(hk_dv_unicode[letra])
                else:
                    saida.append(hk_dv_unicode[letra])

    saida = "".join(saida)
    saida = saida.strip()
    return saida

if __name__ == '__main__':
    print(conversor(input('>>>')))
