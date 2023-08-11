from view.vista_principal import VistaPrincipal

import tkinter as tk
from tkinter import ttk


class VistaReviews(VistaPrincipal):
    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.titulo_label["text"] = "Reviews de usuarios"
        self.titulo_label.pack(**self.default_padding)

        self.frame_reviews = ttk.Frame(self)

        hbar = tk.Scrollbar(self.frame_reviews, orient="horizontal")
        hbar.pack(side="bottom", fill="x")
        vbar = tk.Scrollbar(self.frame_reviews, orient="vertical")
        vbar.pack(side="right", fill="y")

        self.texto = tk.Text(self.frame_reviews, width=35, height=12, wrap='none', xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.texto.pack(side="top", fill="x")

        hbar.config(command=self.texto.xview)
        vbar.config(command=self.texto.yview)

        self.frame_reviews.pack()

        self.boton_atras.pack(side='bottom', **self.default_padding)

    def _recuperar_reviews(self, evento):
        # Habilito la edicion del widget de texto
        self.texto.config(state="normal")
        # Borro el contenido del widget de texto
        self.texto.delete("1.0", tk.END)
        texto = self.controlador.recuperar_reviews(evento)
        self.texto.insert(tk.END, texto)
        # Deshabilito la edicion del widget de texto   
        self.texto.config(state="disabled")
    
    def set_evento(self, evento):
        self._recuperar_reviews(evento)