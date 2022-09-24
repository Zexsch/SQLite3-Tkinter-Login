from tkinter import *
from tkinter import ttk

def success_window(i: int):
    success_root = Toplevel()
    success_root.title('Success!')
    
    success_frame = ttk.Frame(success_root)
    success_frame.grid(column=0, row=0, sticky=(N, W, E, S))
    
    if i == 0: ttk.Label(success_frame, text='Successfully logged in.').grid(column=0, row=0, sticky=(W,E))
    else: ttk.Label(success_frame, text='Successfully signed up.').grid(column=0, row=0, sticky=(W,E))
    
    ttk.Button(success_frame, text='Success!', command=success_root.destroy).grid(column=0, row=1, sticky=(W,E,N,S))
    
    for child in success_frame.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    
    success_root.mainloop()