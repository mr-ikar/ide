import ctypes
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time
import json
import os

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IDE")
        self.attributes("-fullscreen", 1)
        def log(message):
            self.label_log['text'] = time.strftime("%H:%M:%S")+" - "+message
        def update_clock():
            current_time = time.strftime("%H:%M:%S")
            self.label_status.config(text=current_time)
            self.after(1000, update_clock)
        def openProject():
            project_path = filedialog.askdirectory(title="Choose a project directory")
            if not project_path:
                log("Aborted opening project")
                return
            def init_tree(parent, path):
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    item_id = self.treeview_tree.insert(parent, "end", text=item, open=False)
                    if os.path.isdir(item_path):
                        init_tree(item_id, item_path)
            with open(os.path.join(project_path, "config.json"), 'r', encoding="utf-8") as config:
                config_content = json.load(config)
            self.labelframe_tree = ttk.LabelFrame(self.frame_tree, text=config_content['project_name'])
            self.labelframe_tree.grid(row=0, column=0, sticky="nwes", padx=10, pady=10)
            self.treeview_tree = ttk.Treeview(self.labelframe_tree)
            self.treeview_tree.grid(row=0, column=0, sticky="nwes", padx=5, pady=5)
            self.frame_tree.grid_rowconfigure(0, weight=1)
            self.labelframe_tree.grid_rowconfigure(0, weight=1)
            init_tree("", project_path)
            log("Opened project '"+config_content['project_name']+"' ("+project_path+")")
        def newProject():
            def createNewProject():
                project_path = filedialog.askdirectory(title="Choose a project directory")
                if not project_path:
                    log("Aborted project creation")
                    return
                config_content = json.dumps({'project_name': self.entry_name.get(), 'run_command': self.entry_run.get(), 'debug_command': self.entry_debug.get()}, indent=4)
                with open(os.path.join(project_path, "config.json"), 'w', encoding="utf-8") as config:
                    config.write(config_content)
                log("Successfully created a project at '"+project_path+"'!")
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
            self.button_create = ttk.Button(self.frame_newProject, text="Create!", command=createNewProject)
            self.button_create.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        self.frame_menubar = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_menubar.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.grid_columnconfigure(0, weight=1)
        self.button_newProject = ttk.Button(self.frame_menubar, text="New Project", command=newProject)
        self.button_newProject.grid(row=0, column=0, padx=2, pady=2)
        self.button_openProject = ttk.Button(self.frame_menubar, text="Open Project", command=openProject)
        self.button_openProject.grid(row=0, column=1, padx=2, pady=2)

        self.frame_project = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_project.grid(row=1, column=0, sticky="nwes", padx=5, pady=5)
        self.frame_tree = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_tree.grid(row=1, column=1, sticky="nwes", padx=5, pady=5)
        self.grid_rowconfigure(1, weight=1)

        self.frame_status = ttk.Frame(self, borderwidth=2, relief="sunken")
        self.frame_status.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
        self.label_status = ttk.Label(self.frame_status)
        self.label_status.grid(row=0, column=0, padx=2, pady=2)
        self.label_log = ttk.Label(self.frame_status)
        self.label_log.grid(row=0, column=1, padx=5, pady=2)
        update_clock()
        log("Loaded")

if __name__ == "__main__":
    app = App()
    app.mainloop()