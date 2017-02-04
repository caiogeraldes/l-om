#! usr/bin/env python3
# -*- coding: utf-8 -*-

def checker(entrada):

    dv = ['थ', 'ह', 'ण', 'ऐ', 'ख', 'म', 'द', 'छ', 'उ', 'ल', 'च', 'अ',
          'क', 'त', 'ढ', 'ड', 'य', 'व', 'ऋ', 'ऊ', 'प', 'ष', 'घ',
          'ब', 'फ', 'ई', 'आ', 'इ', 'ज', 'ऌ', 'ट', 'ठ', 'भ', 'न',
          '।', 'झ', 'औ', 'ञ', 'स', 'ं', 'र', 'ऽ', 'ॐ', 'ग', 'ध', 'ओ',
          'ए', 'ः', 'श', 'ङ', 'ी', 'े', 'ॄ', 'ृ', 'ै', 'ॢ', 'ो',
          'ौ', 'ा', 'ि', 'ु', 'ू', 'ऽ']
    iast = [ 'ñ', 'ṭ', 'ḍ', 'ṇ','ś', 'ṣ','ṅ', 'ṃ', 'ḥ', 'ā', 'ī', 'ū', 'ṛ', 'ṝ', 'ḷ']
    hk = ['A', 'I', 'U', 'R', 'L', 'G', 'J', 'T', 'D', 'N', 'z', 'M']

    for i in entrada:
        if i in dv:
            translit = 'dv'
            return translit
            break
        elif i in iast:
            translit = 'iast'
            return translit
            break
        elif i in hk:
            translit = 'hk'
            return translit
            break
        else:
            translit = None
