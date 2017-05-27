#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module holds a converting script for IAST >> Harvard-Kyoto.
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

if __name__ == "__main__":
    iasthk(input(">>>"))
