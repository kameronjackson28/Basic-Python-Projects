import tkinter as tk
from tkinter import *
from tkinter import messagebox

import FT_func
import FT_main

def load_gui(self):

    self.txt_source = tk.Entry(self.master,text='Source Directory')
    self.txt_source.grid(row=0,column=0,ipadx=200,ipady=2,sticky=N+W)
    self.txt_destination = tk.Entry(self.master,text='Destination Directory')
    self.txt_destination.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)


    self.btn_browse = tk.Button(self.master,width=12,height=2,text='Browse',command=lambda: FT_func.Browse(self))
    self.btn_browse.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_select = tk.Button(self.master,width=12,height=2,text='Select',command=lambda: FT_func.onSelect(self))
    self.btn_select.grid(row=9,column=0,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_transfer = tk.Button(self.master,width=12,height=2,text='Transfer',command=lambda: FT_func.Transfer(self))
    self.btn_transfer.grid(row=8,column=2,padx=(15,0),pady=(45,10),sticky=W)


 
