# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '15/11/2018 10:48 AM'

import tkinter as tk

import os,time

time.sleep(10)

window=tk.Tk()
window.title("program_start")
window.geometry("400x300")
LINE_STRING="python app.py"
os.system(LINE_STRING)
window.mainloop()