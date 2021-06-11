import tkinter as tk
from tkinter import filedialog as fd 
from tkinter import ttk
import math


LARGE_FONT= ("Verdana", 12)
SMALL_FONT=("Verdana", 10)

class PdfMergePage(ttk.Frame):
    def __init__(self, parent, controller, bg=None):
        bg_override = None


        ttk.Frame.__init__(
            self,
            parent,
            bg=(bg if bg_override is None else bg_override)
        )

        page_title = ttk.Label(self, text="PDF Merge", font=LARGE_FONT)
        page_title.grid(row = 0, column = 1, columnspan=2)

        self.content_frame = self.create_content_frame()
        self.content_frame.grid_propagate(0)

        self.file_label = ttk.Label(self.content_frame, text="Select a file below...", font=SMALL_FONT, width=100)
        self.file_label.grid(row = 0, column = 2, columnspan=2)

        # file_button = FileButton(self)

        # file_button.grid(row = 3, column = 2, columnspan=1)

    def create_content_frame(self):
        content_frame = ttk.Frame(self, borderwidth=5, width=800, height=200, relief="ridge")
        content_frame.grid(column=0, row=5, columnspan=4)

        return content_frame


    def qf(self, quickPrint):
        print(quickPrint)

    def file_button_command(self):
        file_name = fd.askdirectory()
        self.file_label.configure(text=file_name)
        print(file_name)


class FileButton(ttk.Button):

    def __init__(self, parent):
        super(FileButton, self).__init__(
            parent,
            text="Select Directory",
            width=50,
            command=parent.file_button_command
        )

