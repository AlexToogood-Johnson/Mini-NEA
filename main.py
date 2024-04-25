# main.py
"""The Main file for the Mini-NEA project"""

########## IMPORTS & CONSTANTS ##########

import customtkinter as ctk

HEIGHT, WIDTH = 600, 900

########## CLASSES ##########

class App(ctk.CTk):
    """The GUI class"""
    def __init__(self, *args, **kwargs) -> None:
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("Classroom Seating Plan Program")
        self.geometry(f"{WIDTH}x{HEIGHT}")
        self.resizable(False, False)
