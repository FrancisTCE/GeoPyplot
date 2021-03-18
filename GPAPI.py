import tkinter as tk

def getScreenWidthPadded(root,pad):
    return str(root.winfo_screenwidth() * pad).split('.')[0]


def getScreenHeightPadded(root,pad):
    return str(root.winfo_screenheight() * pad).split('.')[0]
