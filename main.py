import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IDE")
        self.attributes("-fullscreen", 1)

        def update_clock():
            current_time = time.strftime("%H:%M:%S")
            self.label_status.config(text=current_time)
            self.after(1000, update_clock)
        def newProject():
            self.frame_newProject = ttk.LabelFrame(self.frame_project, text="Create a new project")
            self.frame_newProject.grid(row=0, column=0, sticky="nwes", padx=50, pady=50)
            self.label_name = ttk.Label(self.frame_newProject, text="Project name")
            self.label_name.grid(row=2, column=0, padx=5, pady=5, sticky="w")
            self.entry_name = ttk.Entry(self.frame_newProject)
            self.entry_name.grid(row=2, column=1, padx=5, pady=5)
            self.label_run = ttk.Label(self.frame_newProject, text="Run command")
            self.label_run.grid(row=3, column=0, padx=5, pady=5, sticky="w")
            self.entry_run = ttk.Entry(self.frame_newProject)
            self.entry_run.grid(row=3, column=1, padx=5, pady=5)
            self.label_debug = ttk.Label(self.frame_newProject, text="Debug command")
            self.label_debug.grid(row=4, column=0, padx=5, pady=5, sticky="w")
            self.entry_debug = ttk.Entry(self.frame_newProject)
            self.entry_debug.grid(row=4, column=1, padx=5, pady=5)
            self.button_create = ttk.Button(self.frame_newProject, text="Create!")
            self.button_create.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        self.frame_menubar = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_menubar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.grid_columnconfigure(0, weight=1)
        self.button_newProject = ttk.Button(self.frame_menubar, text="New Project", command=newProject)
        self.button_newProject.grid(row=0, column=0, padx=2, pady=2)
        self.button_openProject = ttk.Button(self.frame_menubar, text="Open Project")
        self.button_openProject.grid(row=0, column=1, padx=2, pady=2)

        self.frame_project = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_project.grid(row=1, column=0, sticky="nwes", padx=5, pady=5)
        self.grid_rowconfigure(1, weight=1)

        self.frame_status = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_status.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.label_status = ttk.Label(self.frame_status)
        self.label_status.grid(row=0, column=0, padx=2, pady=2)
        update_clock()

if __name__ == "__main__":
    app = App()
    app.mainloop()