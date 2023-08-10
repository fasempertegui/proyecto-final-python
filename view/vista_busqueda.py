import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

from view.vista_principal_eventos import VistaPrincipalEventos


class VistaBusqueda(VistaPrincipalEventos):

    def __init__(self, master=None, controlador=None):

        super().__init__(master, controlador)

        self.master = master

        titulo_fuente = Font(size=13, weight="bold")
        self.titulo = ttk.Label(
            self, text="Buscar eventos", font=titulo_fuente)
        self.titulo.pack(padx=10, pady=5)

        self.label_frame = ttk.LabelFrame(self)
        self.label_frame["text"] = "Buscar por"

        OPCIONES = [
            "Nombre",
            "Artista",
            "Genero"
        ]

        # Con value=OPCIONES[0] la primera opcion (nombre) estara marcada por default
        self.opcion_elegida = tk.StringVar(value=OPCIONES[0])

        # Crear los radio buttons de manera dinamica
        for index, opcion in enumerate(OPCIONES):
            ttk.Radiobutton(
                self.label_frame,
                text=opcion,
                value=opcion,
                variable=self.opcion_elegida,
                command=self.actualizar_eventos
            ).grid(row=0, column=index, padx=3, pady=3)

        self.label_frame.pack()

        self.frame_entry_box = ttk.Frame(self)

        self.entry_box = ttk.Entry(self.frame_entry_box)
        # Placeholder para el campo de busqueda
        self.entry_box.insert(0, "Buscar")
        # Limpiar el campo cuando se hace focus en el
        self.entry_box.bind("<FocusIn>", self.limpiar_campo)
        self.entry_box.pack(side='left', padx=5)

        self.boton_busqueda = ttk.Button(
            self.frame_entry_box,
            text="Buscar",
            command=self.buscar_eventos
        )
        self.boton_busqueda.pack(side='right', padx=5)

        self.frame_entry_box.pack(pady=5)

        # Listbox en la clase padre
        self.listbox.pack(padx=10, pady=5)

        self.actualizar_eventos()

        self.boton_atras = ttk.Button(
            self, text="Volver", command=self.regresar
        )
        self.boton_atras.pack(padx=10, pady=5)
        
    def buscar_eventos(self):
        criterio = self.opcion_elegida.get().lower()
        texto_busqueda = self.entry_box.get().lower()
        # Filtra la lista de todos los eventos
        eventos_filtrados = self.controlador.buscar_eventos(criterio, texto_busqueda)
        # Actualiza la lista de eventos con los resultados de la busqueda
        self.listbox.delete(0, tk.END)
        for evento in eventos_filtrados:
            self.listbox.insert(tk.END, evento.nombre)

    # Elimina cualquier texto que pueda contener el campo (placeholder o texto ingresado)
    def limpiar_campo(self, *args):
        self.entry_box.delete(0, "end")