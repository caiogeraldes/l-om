#!/usr/bin/env python3

"""
Module of textual script conversion between systems of representation of Classical Sanskrit Devanagari. Works with IAST, 
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

import lom
import checktranslit


def textual_conversor(text, type_input='Iast', type_output="Devanagari"):
    """
    :param text: 
    :param type_input: 
    :param type_output: 
    :return: 
    """

    input_file = open("%s.txt" % text, mode='r')
    lines = input_file.readlines()
    output_file = open("%s_output.txt" % text, mode="x")

    while type_input is None:
        print("The type of input is %s? [Y/N]" % checktranslit.checker(lines[0]))
        answer = input('>>>')
        if answer == 'Y' or answer == 'y':
            type_input = checktranslit.checker(lines[0])
        elif answer == 'N' or answer == 'n':
            type_input = input("Type the mode of input [Devanagari/Iast/Harvard-kyoto:").capitalize()

    if type_input == 'Iast':
        if type_output == "Devanagari":
            for line in lines:
                output_file.write(lom.iastdv(line) + '\n')
        if type_output == 'Harvard-kyoto':
            for line in lines:
                output_file.write(lom.iasthk(line) + '\n')
    elif type_input == 'Harvard-kyoto':
        if type_output == "Devanagari":
            for line in lines:
                output_file.write(lom.hkdv(line) + '\n')
        elif type_output == "Iast":
            for line in lines:
                output_file.write(lom.hkiast(line) + '\n')
    elif type_input == 'Devanagari':
        if type_output == "Iast":
            for line in lines:
                output_file.write(lom.dviast(line) + '\n')
        elif type_output == "Harvard-kyoto":
            for line in lines:
                output_file.write(lom.dviast(line) + '\n')
    else:
        print("The type of input isn't valid.")

if __name__ == "__main__":
    textual_conversor("textos/teste")
