#!/usr/bin/env python3

"""
Module of script conversion between systems of representation of Classical Sanskrit Devanagari. Works with IAST, 
Harvard-Kyoto and Devanagari itself.
"""

"""
    Copyright (c) 2017 Caio Borges.
    This file is part of L-om.
    L-om is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

'''Dictionaries for HK >> Dv'''
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
hk_dv_vowel_diacritics = {'A': '\u093E', 'a': '',
                          'i': '\u093F', 'I': '\u0940',
                          'u': '\u0941', 'U': '\u0942',
                          'R': '\u0943', 'RR': '\u0944',
                          'lR': '\u0962',
                          'e': '\u0947', 'ai': '\u0948',
                          'o': '\u094b', 'au': '\u094C'}
hk_dv_vowels = ['A', 'a', 'i', 'I', 'u', 'U',
                'R', 'RR',
                'lR', 'e', 'ai', 'o', 'au']
hk_dv_consonants = ['k', 'g', 'G', 'c', 'j', 'J',
                    'T', 'D', 'N', 't', 'd', 'n',
                    'p', 'b', 'm', 'y', 'r', 'l', 'v',
                    'z', 'S', 's', 'h']
hk_dv_special_consonants = ['G', 'J', 'N', 'n',
                            'm', 'y', 'r', 'l', 'v',
                            'z', 'S', 's']
hk_dv_diacritics = ['M', 'H', '\'']
hk_dv_punctuation = ['|', '||']

'''Dictionaries for HK >> IAST'''
hk_iast_unicode = {'M': 'ṃ', 'H': 'ḥ', 'a': 'a', 'A': 'ā',
                   'i': 'i', 'I': 'ī', 'u': 'u', 'U': 'ū',
                   'R': 'ṛ', 'lR': 'ḷ', 'e': 'e', 'o': 'o',
                   'k': 'k', 'g': 'g', 'G': 'ṅ', 'c': 'c',
                   'j': 'j', 'J': 'ñ', 'T': 'ṭ', 'D': 'ḍ',
                   'N': 'ṇ', 't': 't', 'd': 'd', 'n': 'n',
                   'p': 'p', 'b': 'b', 'm': 'm', 'y': 'y',
                   'r': 'r', 'l': 'l', 'v': 'v', 'z': 'ś',
                   'S': 'ṣ', 's': 's', 'h': 'h', "'": '\'',
                   ' ': ' ', '|': '\u0964', '||': '\u0964'
                   }

'''Dictionaries for IAST >> DV'''
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
iast_dv_vowel_diacritics = {'ā': '\u093E', 'a': '',
                            'i': '\u093F', 'ī': '\u0940',
                            'u': '\u0941', 'ū': '\u0942',
                            'ṛ': '\u0943', 'ṝ': '\u0944',
                            'ḷ': '\u0962',
                            'e': '\u0947', 'ai': '\u0948',
                            'o': '\u094b', 'au': '\u094C'}
iast_dv_vowels = ['ā', 'a', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'e', 'ai', 'o', 'au']
iast_dv_consonants = ['k', 'g', 'ṅ', 'c', 'j', 'ñ',
                      'ṭ', 'ḍ', 'ṇ', 't', 'd', 'n',
                      'p', 'b', 'm', 'y', 'r', 'l', 'v',
                      'ś', 'ṣ', 's', 'h']
iast_dv_special_consonants = ['ṅ', 'ñ', 'ṇ', 'n',
                              'm', 'y', 'r', 'l', 'v',
                              'ś', 'ṣ', 's']
iast_dv_diacritics = ['ṃ', 'ḥ', '\'']
iast_dv_punctuation = ['|', '||']

'''Dictionaries for DV >> IAST'''
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
dv_iast_vowel_diacritics = {'ी': 'ī', 'े': 'e', 'ॄ': 'ṝ', 'ृ': 'ṛ',
                            'ै': 'ai', 'ॢ': 'ḷ', 'ो': 'o', 'ौ': 'au',
                            'ा': 'ā', 'ि': 'i', 'ु': 'u', 'ू': 'ū'}
dv_iast_vowels = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']
dv_iast_consonants = ['क', 'ख', 'ग', 'घ', 'ङ',
                      'च', 'छ', 'ज', 'झ', 'ञ',
                      'ट', 'ठ', 'ड', 'ढ', 'ण',
                      'त', 'थ', 'द', 'ध', 'न',
                      'प', 'फ', 'ब', 'भ', 'म',
                      'य', 'र', 'ल', 'व',
                      'श', 'ष', 'स', 'ह']
dv_iast_diacritics = ['ं', 'ः', 'ऽ']
dv_iast_punctuation = ['।', '।।']

'''Dictionaries for DV >> HK'''
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
dv_hk_vowel_diacritics = {'ी': 'I', 'े': 'e', 'ॄ': 'RR', 'ृ': 'R',
                          'ै': 'ai', 'ॢ': 'lR', 'ो': 'o', 'ौ': 'au',
                          'ा': 'A', 'ि': 'i', 'ु': 'u', 'ू': 'U'}
dv_hk_vowels = ['ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो', 'ौ', 'ा', 'ि', 'ु', 'ू']
dv_hk_consonants = ['क', 'ख', 'ग', 'घ', 'ङ',
                    'च', 'छ', 'ज', 'झ', 'ञ',
                    'ट', 'ठ', 'ड', 'ढ', 'ण',
                    'त', 'थ', 'द', 'ध', 'न',
                    'प', 'फ', 'ब', 'भ', 'म',
                    'य', 'र', 'ल', 'व',
                    'श', 'ष', 'स', 'ह']
dv_hk_diacritics = ['ं', 'ः', 'ऽ']
dv_hk_punctuation = ['।', '।।']

'''Dictionary for IAST >> HK'''
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


def hkdv(input_text):

    """
    :param input_text: Text to be transliterated, written in Harvard-Kyoto.
    :return: Text in Devanagari.
    """

    if input_text[-1] != ' ':
        input_text = input_text.center(len(input_text) + 2)
    output_text = []
    i = -1

    for letter in input_text:
        i += 1
        if letter == " ":
            output_text.append(" ")
        elif letter not in hk_dv_unicode:
            output_text.append(letter)
        else:
            if letter in hk_dv_vowels:
                if letter == 'a':
                    if input_text[i + 1] == 'i':
                        if input_text[i - 1] in hk_dv_consonants:
                            output_text.append(hk_dv_vowel_diacritics['ai'])
                        else:
                            output_text.append(hk_dv_unicode['ai'])
                    elif input_text[i + 1] == 'u':
                        if input_text[i - 1] in hk_dv_consonants:
                            output_text.append(hk_dv_vowel_diacritics['au'])
                        else:
                            output_text.append(hk_dv_unicode['au'])
                    else:
                        if input_text[i - 1] in hk_dv_consonants:
                            output_text.append('')
                        else:
                            output_text.append(hk_dv_unicode[letter])
                elif letter == 'i' or letter == 'u':
                    if input_text[i - 1] == 'a':
                        continue
                    else:
                        if input_text[i - 1] in hk_dv_consonants:
                            output_text.append(hk_dv_vowel_diacritics[letter])
                        else:
                            output_text.append(hk_dv_unicode[letter])
                elif letter == 'R':
                    if input_text[i + 1] == 'R':
                        if input_text[i - 1] in hk_dv_consonants:
                            output_text.append(hk_dv_vowel_diacritics['RR'])
                        else:
                            output_text.append(hk_dv_unicode['RR'])
                    elif input_text[i - 1] == 'R' or input_text[i - 1] == 'l':
                        continue
                    else:
                        if input_text[i - 1] in hk_dv_consonants:
                            output_text.append(hk_dv_vowel_diacritics[letter])
                        else:
                            output_text.append(hk_dv_unicode[letter])
                else:
                    if input_text[i - 1] in hk_dv_consonants:
                        output_text.append(hk_dv_vowel_diacritics[letter])
                    else:
                        output_text.append(hk_dv_unicode[letter])
            elif letter in hk_dv_consonants:
                if letter == 'l' and input_text[i + 1] == 'R':
                    if input_text[i - 1] in hk_dv_consonants:
                        output_text.append(hk_dv_vowel_diacritics['lR'])
                    else:
                        output_text.append(hk_dv_unicode['lR'])
                elif input_text[i + 1] == 'h' and letter not in hk_dv_special_consonants:
                    output_text.append(hk_dv_unicode['%sh' % letter])
                elif letter == 'h' and input_text[i - 1] in hk_dv_consonants:
                    if input_text[i+1] not in hk_dv_vowels:
                        output_text.append('\u094D')
                elif input_text[i + 1] not in hk_dv_vowels:
                    output_text.append(hk_dv_unicode[letter])
                    output_text.append('\u094D')
                else:
                    output_text.append(hk_dv_unicode[letter])
            else:
                output_text.append(hk_dv_unicode[letter])

    output_text = "".join(output_text)
    output_text = output_text.strip()
    return output_text


def hkiast(input_text):

    """
    :param input_text: Text to be transliterated, written in Harvard-Kyoto.
    :return: Text in IAST.
    """

    if input_text[-1] != ' ':
        input_text = input_text.center(len(input_text) + 2)
    output_text = []

    for i in range(len(input_text)):
        c = input_text[i]

        if c not in hk_iast_unicode.keys():
            output_text.append(c)
            continue

        if c == 'l' and input_text[i + 1] == 'R':
            output_text.append(hk_iast_unicode['lR'])
        elif c == 'R' and input_text[i - 1] == 'l':
            continue
        else:
            output_text.append(hk_iast_unicode[c])
    output_text = ''.join(output_text)
    output_text = output_text.strip()
    return output_text


def iastdv(input_text):

    """
    :param input_text: Text to be transliterated, written in IAST.
    :return: Text in Devanagari.
    """

    if input_text[-1] != ' ':
        input_text = input_text.center(len(input_text) + 2)
    output_text = []
    i = -1

    for letter in input_text:
            i += 1
            if letter not in iast_dv_unicode:
                output_text.append(letter)
            else:
                if letter in iast_dv_vowels:
                    if letter == 'a':
                        if input_text[i + 1] == 'i':
                            if input_text[i - 1] in iast_dv_consonants:
                                output_text.append(iast_dv_vowel_diacritics['ai'])
                            else:
                                output_text.append(iast_dv_unicode['ai'])
                        elif input_text[i + 1] == 'u':
                            if input_text[i - 1] in iast_dv_consonants:
                                output_text.append(iast_dv_vowel_diacritics['au'])
                            else:
                                output_text.append(iast_dv_unicode['au'])
                        else:
                            if input_text[i - 1] in iast_dv_consonants:
                                output_text.append('')
                            else:
                                output_text.append(iast_dv_unicode[letter])
                    elif letter == 'i' or letter == 'u':
                        if input_text[i - 1] == 'a':
                            continue
                        else:
                            if input_text[i - 1] in iast_dv_consonants:
                                output_text.append(iast_dv_vowel_diacritics[letter])
                            else:
                                output_text.append(iast_dv_unicode[letter])
                    else:
                        if input_text[i - 1] in iast_dv_consonants:
                            output_text.append(iast_dv_vowel_diacritics[letter])
                        else:
                            output_text.append(iast_dv_unicode[letter])
                elif letter in iast_dv_consonants:
                    if input_text[i + 1] == 'h' and letter not in iast_dv_special_consonants:
                        output_text.append(iast_dv_unicode['%sh' % letter])
                    elif letter == 'h' and input_text[i - 1] in iast_dv_consonants:
                        if input_text[i+1] not in iast_dv_vowels:
                                output_text.append('\u094D')
                    elif input_text[i + 1] not in iast_dv_vowels:
                        output_text.append(iast_dv_unicode[letter])
                        output_text.append('\u094D')
                    else:
                        output_text.append(iast_dv_unicode[letter])
                else:
                    output_text.append(iast_dv_unicode[letter])

    output_text = "".join(output_text)
    output_text = output_text.strip()
    return output_text


def dviast(input_text):

    """
    :param input_text: Text to be transliterated, written in Devanagari
    :return: Text in IAST
    """

    if input_text[-1] != ' ':
        input_text = input_text.center(len(input_text) + 2)
    output_text = []
    i = -1

    for letter in input_text:
        i += 1
        if letter not in dv_iast_unicode.keys() and letter not in dv_iast_vowels:
            output_text.append(letter)
            continue

        if i == len(input_text)-2:
            break

        if letter not in dv_iast_unicode and letter in dv_iast_vowels:
            output_text.append(dv_iast_vowel_diacritics[letter])
        elif letter in dv_iast_consonants:
            if input_text[i + 1] in dv_iast_vowel_diacritics:
                output_text.append(dv_iast_unicode[letter])
            elif input_text[i + 1] == ' ' or input_text[i + 1] in dv_iast_consonants:
                output_text.append(dv_iast_unicode[letter])
                output_text.append('a')
            elif input_text[i + 1] in dv_iast_diacritics or input_text[i + 1] in dv_iast_punctuation:
                output_text.append(dv_iast_unicode[letter])
                output_text.append('a')
            else:
                if input_text[i + 1] == '्':
                    output_text.append(dv_iast_unicode[letter])
                else:
                    print('epa')
        else:
            output_text.append(dv_iast_unicode[letter])

        for a in output_text:
            if a == '्':
                output_text.pop(output_text.index(a))

    output_text = ''.join(output_text)
    output_text = output_text.strip()
    return output_text


def dvhk(input_text):

    """
    :param input_text: Text to be transliterated, written in Devanagari.
    :return: Text in Harvard-Kyoto
    """

    if input_text[-1] != ' ':
        input_text = input_text.center(len(input_text) + 2)
    output_text = []
    i = -1

    for letter in input_text:
        i += 1
        if letter not in dv_hk_unicode.keys() and letter not in dv_hk_vowels:
            output_text.append(letter)
            continue

        if i == len(input_text)-2:
            break

        if letter not in dv_hk_unicode and letter in dv_hk_vowels:
            output_text.append(dv_hk_vowel_diacritics[letter])
        elif letter in dv_hk_consonants:
            if input_text[i + 1] in dv_hk_vowel_diacritics:
                output_text.append(dv_hk_unicode[letter])
            elif input_text[i + 1] == ' ' or input_text[i + 1] in dv_hk_consonants:
                output_text.append(dv_hk_unicode[letter])
                output_text.append('a')
            elif input_text[i + 1] in dv_hk_diacritics or input_text[i + 1] in dv_hk_punctuation:
                output_text.append(dv_hk_unicode[letter])
                output_text.append('a')
            else:
                if input_text[i + 1] == '्':
                    output_text.append(dv_hk_unicode[letter])
                else:
                    print('epa')
        else:
            output_text.append(dv_hk_unicode[letter])

        for a in output_text:
            if a == '्':
                output_text.pop(output_text.index(a))

    output_text = ''.join(output_text)
    output_text = output_text.strip()
    return output_text


def iasthk(input_text):

    """
    :param input_text: Text to be transliterated, written in IAST.
    :return: Text in Harvard-Kyoto.
    """

    output_text = []
    for letter in input_text:
        if letter not in iast_hk_unicode:
            output_text.append(letter)
        else:
            output_text.append(letter(iast_hk_unicode[letter]))

    output_text = ''.join(output_text)
    output_text = output_text.strip()
    return output_text
