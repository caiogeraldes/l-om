#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def checker(input):

    dv = ['थ', 'ह', 'ण', 'ऐ', 'ख', 'म', 'द', 'छ', 'उ', 'ल', 'च', 'अ',
          'क', 'त', 'ढ', 'ड', 'य', 'व', 'ऋ', 'ऊ', 'प', 'ष', 'घ',
          'ब', 'फ', 'ई', 'आ', 'इ', 'ज', 'ऌ', 'ट', 'ठ', 'भ', 'न',
          '।', 'झ', 'औ', 'ञ', 'स', 'र', 'ऽ', 'ॐ', 'ग', 'ध', 'ओ',
          'ए', 'श', 'ङ']
    iast = [ 'ñ', 'ṭ', 'ḍ', 'ṇ','ś', 'ṣ','ṅ', 'ṃ', 'ḥ', 'ā', 'ī', 'ū', 'ṛ', 'ṝ', 'ḷ']
    hk = ['A', 'I', 'U', 'R', 'L', 'G', 'J', 'T', 'D', 'N', 'z', 'M']

    for i in input:
        if i in dv:
            translit = 'Devanagari'
            return translit
            break
        elif i in iast:
            translit = 'Iast'
            return translit
            break
        elif i in hk:
            translit = 'Harvard-kyoto'
            return translit
            break
        else:
            translit = None 

if __name__ == "__main__":
	print(checker(input(">>>")))
