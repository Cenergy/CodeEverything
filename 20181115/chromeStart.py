# -*-coding:utf-8 -*-
__author__ = 'Cenergy'
__date__ = '15/11/2018 10:48 AM'

import tkinter as tk

import os,time

time.sleep(10)

window=tk.Tk()
window.title("chrome_start")
window.geometry("400x300")
CHROME_PATH="ios\Application\Google Chrome.app --kiosk --disable-pinch --disable-translate www.baidu.com"
os.system(CHROME_PATH)
window.mainloop()