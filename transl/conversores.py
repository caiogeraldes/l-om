#!/usr/bin/env python3

"""
Transliterador Harvard-Kyoto, IAST e Devanāgarī.
"""

'''Dicionários para HK >> Dv'''
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
                 "'": '\u093D', 'oM': '\u0950', ' ': ' ', '|': '\u0964', '||': '\u0964'
                 }
hk_dv_diacriticos_vogais = {'A': '\u093E', 'a': '',
                            'i': '\u093F', 'I': '\u0940',
                            'u': '\u0941', 'U': '\u0942',
                            'R': '\u0943', 'RR': '\u0944',
                            'lR': '\u0962',
                            'e': '\u0947', 'ai': '\u0948',
                            'o': '\u094b', 'au': '\u094C'}
hk_dv_vogais = ['A', 'a', 'i', 'I', 'u', 'U',
                'R', 'RR',
                'lR', 'e', 'ai', 'o', 'au']
hk_dv_consoantes = ['k', 'g', 'G', 'c', 'j', 'J',
                    'T', 'D', 'N', 't', 'd', 'n',
                    'p', 'b', 'm', 'y', 'r', 'l', 'v',
                    'z', 'S', 's', 'h']
hk_dv_consoantes_especiais = ['G', 'J', 'N', 'n',
                              'm', 'y', 'r', 'l', 'v',
                              'z', 'S', 's']

'''Dicionários para HK >> IAST'''
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

'''Dicionário para IAST >> DV'''
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
iast_dv_diacríticos_vogais = {'ā': '\u093E', 'a': '',
                              'i': '\u093F', 'ī': '\u0940',
                              'u': '\u0941', 'ū': '\u0942',
                              'ṛ': '\u0943', 'ṝ': '\u0944',
                              'ḷ': '\u0962',
                              'e': '\u0947', 'ai': '\u0948',
                              'o': '\u094b', 'au': '\u094C'}
iast_dv_vogais = ['ā', 'a', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'e', 'ai', 'o', 'au']
iast_dv_consoantes = ['k', 'g', 'ṅ', 'c', 'j', 'ñ',
                      'ṭ', 'ḍ', 'ṇ', 't', 'd', 'n',
                      'p', 'b', 'm', 'y', 'r', 'l', 'v',
                      'ś', 'ṣ', 's', 'h']
iast_dv_consoantes_especiais = ['ṅ', 'ñ', 'ṇ', 'n',
                                'm', 'y', 'r', 'l', 'v',
                                'ś', 'ṣ', 's']
iast_dv_diacriticos = ['ṃ', 'ḥ', '\'']
iast_dv_pontuação = ['|', '||']

'''Dicionário para DV >> IAST'''
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
dv_iast_diacriticos_vogais = {'ी': 'ī', 'े': 'e', 'ॄ': 'ṝ', 'ृ': 'ṛ',
               'ै': 'ai', 'ॢ': 'ḷ', 'ो': 'o', 'ौ': 'au',
               'ा': 'ā', 'ि': 'i', 'ु': 'u', 'ू': 'ū'}
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

'''Dicionário para DV >> HK'''
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
dv_hk_diacríticos_vogais = {'ी': 'I', 'े': 'e', 'ॄ': 'RR', 'ृ': 'R',
               'ै': 'ai', 'ॢ': 'lR', 'ो': 'o', 'ौ': 'au',
               'ा': 'A', 'ि': 'i', 'ु': 'u', 'ू': 'U'}
dv_hk_vogais = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']
dv_hk_consoantes = ['क', 'ख', 'ग', 'घ', 'ङ',
                 'च', 'छ', 'ज', 'झ', 'ञ',
                 'ट', 'ठ', 'ड', 'ढ', 'ण',
                 'त', 'थ', 'द', 'ध', 'न',
                 'प', 'फ', 'ब', 'भ', 'म',
                 'य', 'र', 'ल', 'व',
                 'श', 'ष', 'स', 'ह']
dv_hk_diacriticos = ['ं', 'ः', 'ऽ']
dv_hk_pontuacao = ['।', '।।']

'''Dicionário para IAST >> HK'''
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

def hkdv(entrada):

    '''
    :param entrada: str
    :return: str
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    i = -1
    # Dicionário de correspondências HK>>DV

    '''diacriticos = ['M', 'H', '\'']
    pontuacao = ['|', '||']'''

    for letra in entrada:
        i += 1
        if letra == " ":
            saida.append(" ")
        elif letra not in hk_dv_unicode:
            saida.append(letra)
        else:
            if letra in hk_dv_vogais:
                if letra == 'a':
                    if entrada[i + 1] == 'i':
                        if entrada[i - 1] in hk_dv_consoantes:
                            saida.append(hk_dv_diacriticos_vogais['ai'])
                        else:
                            saida.append(hk_dv_unicode['ai'])
                    elif entrada[i + 1] == 'u':
                        if entrada[i - 1] in hk_dv_consoantes:
                            saida.append(hk_dv_diacriticos_vogais['au'])
                        else:
                            saida.append(hk_dv_unicode['au'])
                    else:
                        if entrada[i - 1] in hk_dv_consoantes:
                            saida.append('')
                        else:
                            saida.append(hk_dv_unicode[letra])
                elif letra == 'i' or letra == 'u':
                    if entrada[i - 1] == 'a':
                        continue
                    else:
                        if entrada[i - 1] in hk_dv_consoantes:
                            saida.append(hk_dv_diacriticos_vogais[letra])
                        else:
                            saida.append(hk_dv_unicode[letra])
                elif letra == 'R':
                    if entrada[i + 1] == 'R':
                        if entrada[i - 1] in hk_dv_consoantes:
                            saida.append(hk_dv_diacriticos_vogais['RR'])
                        else:
                            saida.append(hk_dv_unicode['RR'])
                    elif entrada[i - 1] == 'R' or entrada[i - 1] == 'l':
                        continue
                    else:
                        if entrada[i - 1] in hk_dv_consoantes:
                            saida.append(hk_dv_diacriticos_vogais[letra])
                        else:
                            saida.append(hk_dv_unicode[letra])
                else:
                    if entrada[i - 1] in hk_dv_consoantes:
                        saida.append(hk_dv_diacriticos_vogais[letra])
                    else:
                        saida.append(hk_dv_unicode[letra])
            elif letra in hk_dv_consoantes:
                if letra == 'l' and entrada[i + 1] == 'R':
                    if entrada[i - 1] in hk_dv_consoantes:
                        saida.append(hk_dv_diacriticos_vogais['lR'])
                    else:
                        saida.append(hk_dv_unicode['lR'])
                elif entrada[i + 1] == 'h' and letra not in hk_dv_consoantes_especiais:
                    saida.append(hk_dv_unicode['%sh' % letra])
                elif entrada[i] == 'h' and entrada[i - 1] in hk_dv_consoantes:
                    continue
                elif entrada[i + 1] not in hk_dv_vogais:
                    saida.append(hk_dv_unicode[letra])
                    saida.append('\u094D')
                else:
                    saida.append(hk_dv_unicode[letra])
            else:
                saida.append(hk_dv_unicode[letra])

    saida = "".join(saida)
    saida = saida.strip()
    return saida


def hkiast(entrada):

    '''
    :param entrada: str
    :return: str
    '''

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


def iastdv(entrada):

    '''
    :param entrada: str 
    :return: str 
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada
    saida = []
    i = -1

    for letra in entrada:
            i += 1
            if letra not in iast_dv_unicode:
                saida.append(letra)
            else:
                if letra in iast_dv_vogais:
                    if letra == 'a':
                        if entrada[i + 1] == 'i':
                            if entrada[i - 1] in iast_dv_consoantes:
                                saida.append(iast_dv_diacríticos_vogais['ai'])
                            else:
                                saida.append(iast_dv_unicode['ai'])
                        elif entrada[i + 1] == 'u':
                            if entrada[i - 1] in iast_dv_consoantes:
                                saida.append(iast_dv_diacríticos_vogais['au'])
                            else:
                                saida.append(iast_dv_unicode['au'])
                        else:
                            if entrada[i - 1] in iast_dv_consoantes:
                                saida.append('')
                            else:
                                saida.append(iast_dv_unicode[letra])
                    elif letra == 'i' or letra == 'u':
                        if entrada[i - 1] == 'a':
                            continue
                        else:
                            if entrada[i - 1] in iast_dv_consoantes:
                                saida.append(iast_dv_diacríticos_vogais[letra])
                            else:
                                saida.append(iast_dv_unicode[letra])
                    else:
                        if entrada[i - 1] in iast_dv_consoantes:
                            saida.append(iast_dv_diacríticos_vogais[letra])
                        else:
                            saida.append(iast_dv_unicode[letra])
                elif letra in iast_dv_consoantes:
                    if entrada[i + 1] == 'h' and letra not in iast_dv_consoantes_especiais:
                        saida.append(iast_dv_unicode['%sh' % letra])
                    elif letra == 'h' and entrada[i - 1] in iast_dv_consoantes:
                        continue
                    elif entrada[i + 1] not in iast_dv_vogais:
                        saida.append(iast_dv_unicode[letra])
                        saida.append('\u094D')
                    else:
                        saida.append(iast_dv_unicode[letra])
                else:
                    saida.append(iast_dv_unicode[letra])

    saida = "".join(saida)
    saida = saida.strip()
    return saida


def dviast(entrada):

    '''
    :param entrada: str
    :return: str
    '''

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


def dvhk(entrada):

    '''
    :param entrada: 
    :return: 
    '''

    if entrada[-1] != ' ':
        entrada = '%s  ' % entrada

    saida = []
    for i in range(len(entrada)):
        c = entrada[i]

        if c not in dv_hk_unicode.keys() and c not in dv_hk_vogais:
            saida.append(c)
            continue

        if i == len(entrada)-2:
            break

        if c not in dv_hk_unicode and c in dv_hk_vogais:
            saida.append(dv_hk_diacríticos_vogais[c])
        elif c in dv_hk_consoantes:
            if entrada[i + 1] in dv_hk_diacríticos_vogais:
                saida.append(dv_hk_unicode[c])
            elif entrada[i + 1] == ' ' or entrada[i + 1] in dv_hk_consoantes:
                saida.append(dv_hk_unicode[c])
                saida.append('a')
            elif entrada[i + 1] in dv_hk_diacriticos or entrada[i + 1] in dv_hk_pontuacao:
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


def iasthk(entrada):

    '''
    :param entrada: 
    :return: 
    '''

    saida = []
    for letra in entrada:
        if letra not in iast_hk_unicode:
            saida.append(letra)
        else:
            saida.append(letra(iast_hk_unicode[letra]))

    saida = ''.join(saida)
    saida = saida.strip()
    return saida
