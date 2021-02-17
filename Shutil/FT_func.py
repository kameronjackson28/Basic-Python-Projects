import time
import os
import shutil
from tkinter import filedialog, messagebox
import FT_main
import FT_gui


def Browse(self): 
    dirpath = filedialog.askdirectory()

    self.txt_source.insert(0,dirpath) 
        
def onSelect(self): 
    dirpath = filedialog.askdirectory()

    self.txt_destination.insert(0,dirpath)
    
def Transfer(self):
    

    SECONDS_IN_DAY = 24 * 60 * 60



    now = time.time()
    before = now - SECONDS_IN_DAY

    src_path = self.txt_source.get()
    dst_path = self.txt_destination.get()
    

    for fname in os.listdir(src_path):
        src_fname = os.path.join(src_path, fname)
        last_mod_time = os.path.getmtime(src_fname)
        if last_mod_time > before:
            shutil.move(src_fname, dst_path)
    
    
