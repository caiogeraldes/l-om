#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module holds a converting script for Devanāgarī >>> Harvard-Kyoto.
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

if __name__ == '__main__':
    dvhk(input(">>>"))
