#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
This module holds a converting script for Harvard-Kyoto >>> Devanāgarī.
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
hk_dv_consonants = ['k', 'g', 'G',
                    'c', 'j', 'J',
                    'T', 'D', 'N',
                    't', 'd', 'n',
                    'p', 'b', 'm',
                    'y', 'r', 'l', 'v',
                    'z', 'S', 's', 'h']
hk_dv_special_consonants = ['G', 'J', 'N', 'n', 'm',
                            'y', 'r', 'l', 'v',
                            'z', 'S', 's']
hk_dv_diacritics = ['M', 'H', '\'']
hk_dv_punctuation = ['|', '||']


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

if __name__ == '__main__':
    hkdv(input(">>>"))
