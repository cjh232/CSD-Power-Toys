import tkinter as tk
from .PdfMergePage import PdfMergePage
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class Test(ttk.Frame):
     
    def __init__(self, parent, controller, bg=None):
        bg_override = None


        ttk.Frame.__init__(
            self,
            parent,
            bg=(bg if bg_override is None else bg_override)
        )
        label = tk.Label(self, text ="Test Page", font = LARGE_FONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
  