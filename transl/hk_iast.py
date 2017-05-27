#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module holds a converting script for Harvard-Kyoto >> IAST.
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

if __name__ == '__main__':
    hkiast(input(">>>"))
