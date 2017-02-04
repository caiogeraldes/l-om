#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf
from lom import hk_dv, iast_dv, hk_iast, dv_iast

class Janela(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Transliterador L-Oṃ")
        self.set_size_request(400, 200)
        self.set_border_width(20)

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
        vbox.pack_start(label, True, True, 0)

        # Define o Método de Entrada (HK, IAST ou Devanāgarī)

        hbox1 = Gtk.Box(spacing=6)
        vbox.pack_start(hbox1, True, True, 0)

        tag1 = Gtk.Label()
        tag1.set_label('Entrada')
        hbox1.pack_start(tag1, False, False, 0)

        self.hk_button = Gtk.RadioButton.new_with_label_from_widget(None, "Harvard-Kyoto")
        hbox1.pack_start(self.hk_button, False, False, 0)

        self.iast_button = Gtk.RadioButton.new_from_widget(self.hk_button)
        self.iast_button.set_label("IAST")
        hbox1.pack_start(self.iast_button, False, False, 0)

        self.dv_button2 = Gtk.RadioButton.new_from_widget(self.hk_button)
        self.dv_button2.set_label("Devanāgarī")
        hbox1.pack_start(self.dv_button2, False, False, 0)

        # Define o Método de Saída (Devanāgarī ou IAST)

        hbox2 = Gtk.Box(spacing=6)
        vbox.pack_start(hbox2, True, True, 0)

        tag2 = Gtk.Label()
        tag2.set_label('Saida')
        hbox2.pack_start(tag2, False, False, 0)

        self.dv_button = Gtk.RadioButton.new_with_label_from_widget(None, "Devanāgarī")
        hbox2.pack_start(self.dv_button, False, False, 0)

        self.iast_button2 = Gtk.RadioButton.new_from_widget(self.dv_button)
        self.iast_button2.set_label("IAST")
        hbox2.pack_start(self.iast_button2, False, False, 0)

        # Locais de Input e Output

        self.texto = Gtk.Entry()
        self.texto.set_text("Escolha o sistema de escrita da entrada e insira o texto.")
        vbox.pack_start(self.texto, True, True, 0)

        self.saida = Gtk.Entry()
        self.saida.set_text("Escolha o sistema de escrita de saída.")
        vbox.pack_start(self.saida, True, True, 0)

        # Botões de Operação

        self.botao = Gtk.Button(label="Conversor")
        self.botao.set_alignment(0.5, 0.5)
        self.botao.connect("clicked", self.conversor)
        vbox.pack_start(self.botao, False, False, 0)

        self.botao2 = Gtk.Button(label="Sobre")
        self.botao2.connect('clicked', self.sobre_clicked)
        vbox.pack_start(self.botao2, False, False, 0)

    # Engine

    def conversor(self, widget):
        entrada = self.texto.get_text()
        saida = None
        if self.hk_button.get_active():
            if self.dv_button.get_active():
                saida = hk_dv.conversor(entrada)
            elif self.iast_button2.get_active():
                saida = hk_iast.conversor(entrada)
        elif self.iast_button.get_active():
            if self.dv_button.get_active():
                saida = iast_dv.conversor(entrada)
            elif self.iast_button2.get_active():
                saida = "IAST >> IAST ?"
        elif self.dv_button2.get_active():
            if self.iast_button2.get_active():
                saida = dv_iast.conversor(entrada)
            elif self.dv_button.get_active():
                saida = "Devanāgarī >> Devanāgarī ?"
        self.saida.set_text(saida)

    # Define a abertura da janela 'Sobre'

    def sobre_clicked(self, widget):
        dialog = Sobre()
        dialog.run()
        dialog.destroy()

# Modelo da janela 'Sobre'


class Sobre(Gtk.AboutDialog):
    def __init__(self):
        Gtk.AboutDialog.__init__(self)
        self.set_border_width(20)
        self.set_program_name('Transliterador L-Oṃ')
        self.set_logo(GdkPixbuf.Pixbuf.new_from_file_at_size('logo/lom.png', 100, 100))
        self.set_version('0.3')
        self.set_license('Open Source e tal.')
        self.set_comments('Transliterador com os métodos:'
                          '\n\nHarvard-Kyoto >> Devanāgarī e IAST \nIAST >> Devanāgarī\nDevanāgarī >> IAST \n\n'
                          '~~~ Ainda com alguns bugs com relação ao uso de múltiplas linhas. \n'
                          'Converte o recuo em um caractere UTF-8, o qual '
                          'desaparece em editores de texto como Office. ~~~')
        self.set_copyright('\u00A9 Caio Borges Aguida Geraldes, 2017.')
        self.set_authors(['Caio Borges Aguida Geraldes'])
        self.show_all()




window = Janela()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
