import tkinter as tk
from pages.HomePage import HomePage
from pages.OrganizePage import OrganizePage
from pages.PdfMergePage import PdfMergePage
from pages.Test import Test
from tkinter import ttk

LARGE_FONT= ("Verdana", 12)

class Window(tk.Tk):

    def __init__(self, apps, start_page, default_bg, w=500, h=500, *args, **kwargs,):
        tk.Tk.__init__(self, *args, **kwargs)

        # self.tk.call(
        #     'lappend', 
        #     'auto_path', 
        #     r'C:\Users\chunt\OneDrive\Desktop\Projects\CSD Tkinter\theme\ttk-Breeze-master'
        #     )
        # self.tk.call('package', 'require', 'Breeze')
        self.tk.call(
            'source', 
            r'C:\Users\chunt\OneDrive\Desktop\Projects\CSD Tkinter\theme\ttk-Breeze-master\breeze.tcl')

        sto = ttk.Style()

        sto.theme_use("Breeze")    

        self.geometry(f'{w}x{h}')
        self.resizable(False, False)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.registered_apps = {}

        for app_name, app in apps:

            frame = app(container, self)
            self.registered_apps[app_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")


            
        self._setup_menu()
        self.show_app(start_page)


    def _setup_menu(self):
        menubar = tk.Menu(self)

        menubar.add_cascade(label="File", menu=self._init_file_menu(menubar))
        menubar.add_cascade(label="Apps", menu=self._init_apps_menu(menubar))
        
        self.config(menu=menubar)

    def _init_apps_menu(self, menubar):
        apps_menu = tk.Menu(menubar, tearoff=0)

        for app_name, app in self.registered_apps.items():
            apps_menu.add_command(label=app_name,
                command = self._build_lambda(app_name)
            )

        return apps_menu

    def _build_lambda(self, app_name):
        return lambda: self.show_app(app_name)

    def _init_file_menu(self, menubar):
        file_menu = tk.Menu(menubar, tearoff=0)

        # Defining commands
        exit_command = lambda: self.destroy()

        file_menu.add_command(label="Exit", command=exit_command)

        return file_menu


    def show_app(self, app_name):

        frame = self.registered_apps[app_name]
        frame.tkraise()


# Each new page is added here by registereing it with it's name
# The name given here will be used in menus and buttons throughout
# the whole program

apps = [
    ("Home", HomePage),
    ("Organize", OrganizePage),
    ("Merge PDF", PdfMergePage),
    ("Test", Test)
]

# App window size is defaulted to 500x500
app = Window(apps=apps, start_page="Merge PDF", w=800, h=800, default_bg="#222C3D")
app.mainloop()