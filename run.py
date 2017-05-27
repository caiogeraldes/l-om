#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GUI version of the L-om transliteration engine, made mostly for testing and fast conversions.
"""

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from transl import checktranslit
from transl import lom


class Janela(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Transliterador L-Oṃ")
        self.set_size_request(400, 200)
        self.set_border_width(20)
        self.set_position(Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        self.add(vbox)

        # Define o menu superior do app.

        self.mb = Gtk.MenuBar()
        vbox.pack_start(self.mb, True, True, 0)

        ajuda_item = Gtk.MenuItem()
        ajuda_item.set_label('Ajuda')

        ajuda_menu = Gtk.Menu()
        ajuda_menu.set_title('Ajuda')
        ajuda_item.set_submenu(ajuda_menu)

        sobre_item = Gtk.MenuItem()
        sobre_item.set_label('Sobre')
        sobre_item.connect('activate', self.sobre_clicked)
        ajuda_menu.append(sobre_item)

        self.mb.append(ajuda_item)

        # Define o interior do app.

        label = Gtk.Label()
        label.set_label("Conversor entre Alfabeto Latino e Devanāgarī.")
        vbox.pack_start(label, False, False, 0)

        # Define o Método de Entrada (HK, Iast ou Devanāgarī)

        hbox1 = Gtk.Box(spacing=6)
        vbox.pack_start(hbox1, True, True, 0)

        tag1 = Gtk.Label()
        tag1.set_label('Entrada')
        hbox1.pack_start(tag1, False, False, 0)

        self.hk_button = Gtk.RadioButton.new_with_label_from_widget(None, "Harvard-Kyoto")
        hbox1.pack_start(self.hk_button, False, False, 0)

        self.iast_button = Gtk.RadioButton.new_from_widget(self.hk_button)
        self.iast_button.set_label("Iast")
        hbox1.pack_start(self.iast_button, False, False, 0)

        self.dv_button2 = Gtk.RadioButton.new_from_widget(self.hk_button)
        self.dv_button2.set_label("Devanāgarī")
        hbox1.pack_start(self.dv_button2, False, False, 0)

        # Define o Método de Saída (Devanāgarī ou Iast)

        hbox2 = Gtk.Box(spacing=6)
        vbox.pack_start(hbox2, True, True, 0)

        tag2 = Gtk.Label()
        tag2.set_label('Saida')
        hbox2.pack_start(tag2, False, False, 0)

        self.dv_button = Gtk.RadioButton.new_with_label_from_widget(None, "Devanāgarī")
        hbox2.pack_start(self.dv_button, False, False, 0)

        self.iast_button2 = Gtk.RadioButton.new_from_widget(self.dv_button)
        self.iast_button2.set_label("Iast")
        hbox2.pack_start(self.iast_button2, False, False, 0)

        # Locais de Input e Output

        self.texto = Gtk.Entry()
        self.texto.set_text("Escolha o sistema de escrita da entrada e insira o texto.")
        self.texto.connect("activate", self.conversor)
        vbox.pack_start(self.texto, True, True, 0)

        self.saida = Gtk.Entry()
        self.saida.set_text("Escolha o sistema de escrita de saída.")
        vbox.pack_start(self.saida, True, True, 0)

        # Botões de Operação

        self.botao = Gtk.Button(label="Conversor")
        self.botao.set_alignment(0.5, 0.5)
        self.botao.connect("clicked", self.conversor)
        vbox.pack_start(self.botao, True, False, 0)

        self.botao2 = Gtk.Button(label="Sobre")
        self.botao2.connect('clicked', self.sobre_clicked)
        vbox.pack_start(self.botao2, False, False, 0)

    # Define a abertura da janela 'Sobre'

    def sobre_clicked(self, widget):
        sobre = Gtk.AboutDialog()
        sobre.set_border_width(20)
        sobre.set_program_name('Transliterador L-Oṃ')
        sobre.set_logo(GdkPixbuf.Pixbuf.new_from_file_at_size('logo/lom.png', 100, 100))
        sobre.set_version('0.4')
        sobre.set_license("""Copyright (c) 2017 Caio Borges.
                          This file is part of L-om. L-om is free software: you can redistribute it and/or modify 
                          it under the terms of the GNU General Public License as published by
                          the Free Software Foundation, either version 3 of the License, or
                          (at your option) any later version.
                           
                          This program is distributed in the hope that it will be useful,
                          but WITHOUT ANY WARRANTY; without even the implied warranty of
                          MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
                          GNU General Public License for more details.
                            
                          You should have received a copy of the GNU General Public License
                          along with this program.  If not, see <http://www.gnu.org/licenses/>.""")
        sobre.set_comments('Transliterador com os métodos:'
                           '\n\nHarvard-Kyoto >> Devanāgarī e Iast '
                           '\nIast >> Devanāgarī\nDevanāgarī >> Iast \n\n'
                           '~~~ Ainda com alguns bugs com relação ao uso de múltiplas linhas. \n'
                           'Converte o recuo em um caractere UTF-8, o qual '
                           'desaparece em editores de texto como Office. ~~~')

        sobre.set_copyright('\u00A9 Caio Borges, 2017.')
        sobre.set_authors(['Caio Borges Aguida Geraldes'])
        sobre.run()
        sobre.destroy()

    def erro_translit(self, metodo_esperado, metodo_obtido):
        t_erro = Gtk.MessageDialog()
        t_erro.add_buttons(Gtk.STOCK_OK, Gtk.ResponseType.OK)
        t_erro.set_title("Erro no sistema de transliteração")
        t_erro.set_keep_above(True)
        t_erro.set_markup("""Eita, o método de transliteração do texto de entrada não corresponde ao método escolhido.
                          \n\tMétodo esperado: %s \n\tMétodo checado: %s. \nA transliteração feita apresentará falhas.
                          """ % (metodo_esperado, metodo_obtido))
        t_erro.run()
        t_erro.destroy()

    # Engine

    def conversor(self, widget):
        entrada = self.texto.get_text()
        metodo_checagem = checktranslit.checker(entrada)
        saida = None
        if self.hk_button.get_active():

            if metodo_checagem == 'Harvard-kyoto' or metodo_checagem is None:
                pass
            else:
                self.erro_translit('Harvard-kyoto', metodo_checagem)

            if self.dv_button.get_active():
                saida = lom.hkdv(entrada)
            elif self.iast_button2.get_active():
                saida = lom.hkiast(entrada)
        elif self.iast_button.get_active():

            if metodo_checagem == 'Iast' or metodo_checagem is None:
                pass
            else:
                self.erro_translit("Iast", metodo_checagem)

            if self.dv_button.get_active():
                saida = lom.iastdv(entrada)
            elif self.iast_button2.get_active():
                saida = "Iast >> Iast ?"
        elif self.dv_button2.get_active():

            if metodo_checagem == "Devanagari":
                pass
            else:
                self.erro_translit('Devanagari', metodo_checagem)

            if self.iast_button2.get_active():
                saida = lom.dviast(entrada)
            elif self.dv_button.get_active():
                saida = "Devanāgarī >> Devanāgarī ?"
        self.saida.set_text(saida)

if __name__ == '__main__':
        window = Janela()
        window.connect("delete-event", Gtk.main_quit)
        window.show_all()
        Gtk.main()
