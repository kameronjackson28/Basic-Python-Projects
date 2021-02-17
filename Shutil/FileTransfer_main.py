from tkinter import *
import tkinter as tk


#Be sure to import our other modules
# so we can have access to them.
import FT_gui
import FT_func
# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,500) #(Height,Width)
        self.master.maxsize(500,500)
        #This CenterWindow method will center our app on the user's screen
        self.master.title("Build Your Own Page")
        self.master.configure(bg="#F0F0F0")

        #load in the GUI widgets from a separate module.
        #keeping in your compartmentalized and clutter free
        FT_gui.load_gui(self)



        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
