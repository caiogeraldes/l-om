#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module checks if the type of input is either IAST, Harvard Kyoto or Devanagari.
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

def checker(input_text):

    """
    :param input_text: str. Text to be tested on its system of writing.
    :return: str. The text's system of writing or None.
    """

    dv = ['थ', 'ह', 'ण', 'ऐ', 'ख', 'म', 'द', 'छ', 'उ', 'ल', 'च', 'अ',
          'क', 'त', 'ढ', 'ड', 'य', 'व', 'ऋ', 'ऊ', 'प', 'ष', 'घ',
          'ब', 'फ', 'ई', 'आ', 'इ', 'ज', 'ऌ', 'ट', 'ठ', 'भ', 'न',
          '।', 'झ', 'औ', 'ञ', 'स', 'र', 'ऽ', 'ॐ', 'ग', 'ध', 'ओ',
          'ए', 'श', 'ङ']
    iast = ['ñ', 'ṭ', 'ḍ', 'ṇ','ś', 'ṣ','ṅ', 'ṃ', 'ḥ', 'ā', 'ī', 'ū', 'ṛ', 'ṝ', 'ḷ']
    hk = ['A', 'I', 'U', 'R', 'L', 'G', 'J', 'T', 'D', 'N', 'z', 'M']

    for i in input_text:
        if i in dv:
            translit = 'Devanagari'
            return translit
        elif i in iast:
            translit = 'Iast'
            return translit
        elif i in hk:
            translit = 'Harvard-kyoto'
            return translit
        else:
            translit = None 

if __name__ == "__main__":
    print(checker(input(">>>")))
