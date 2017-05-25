# L-oṃ

## Hello or नमस्ते

This is a small python script I developed as a personal project for learning the basics of programming and helping me and some fellow mates that are studying sanskrit at the University of São Paulo, Brasil. For a long time we were trying to make some fast transliterations of texts for quoting in papers, articles and even class' handouts and althought there are many transliterators avaliable online, I felt the need of trying by myself to implement one and share it.

## Introduction

L-oṃ is a transliterator script for Classical Sanskrit Devanāgarī (which means it still have no accentuation nor modern Indian languages' phonemes and graphemes) written in Python 3. It has the following ways:
  - Harvard-Kyoto to Devanāgarī
  - Harvard-Kyoto to IAST
  - IAST to Devanāgarī
  - Devanāgarī to IAST

Although I suppose it's quite useless, there are also the methods:
  - Devanāgarī to Harvard-Kyoto
  - IAST to Harvard-Kyoto

## Structure

Dealing with strings proved to be quite hard when I was starting (when I first coded the L-oṃ, I was leaning python for a couple of weeks), so many of the solutions here are -excuse my portuguese- "gambiarras" -- and I guess "hack" translates that.
Basically, for each way of moving either the sanskrit devanāgarī to a roman-script, either from IAST/Harvard-Kyoto to the itself nāgarī, I build a dictionary correlating the input system to the output system in its Unicode. The script breaks the input string in a list, walks it item by item and, while checking its enviroment, chooses from a set of dictionaries which character to append in a output list that is then joined into a string and finally printet or saved into a .txt. Which means that most of the code is dedicated to if-statements checking if there's or not a vowel or consonant before the letter being transliterated, if there must be a virāma etc.
