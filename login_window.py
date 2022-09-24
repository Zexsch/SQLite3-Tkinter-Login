import sqlite3
from tkinter import *
from tkinter import ttk
from signup_window import signup_window
from success_window import success_window

def login_window():
    root = Tk()
    root.title('Login')
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    ttk.Label(mainframe, text='Username').grid(column=1, row=1, sticky=(W, E))
    ttk.Label(mainframe, text='Password').grid(column=2, row=1, sticky=(W, E))
    
    username_entry = StringVar()
    password_entry = StringVar()
    ttk.Entry(mainframe, width=20, textvariable=username_entry).grid(column=1, row=2, sticky=(W,E))
    ttk.Entry(mainframe, width=20, textvariable=password_entry).grid(column=2, row=2, sticky=(W,E))
    
    with sqlite3.connect('LoginDB.db') as con:
        cur = con.cursor()
        
        try: cur.execute('CREATE TABLE Login(id integer PRIMARY KEY, username, password, email)')
        except sqlite3.OperationalError: pass
        
    def select_pass_user():
        with sqlite3.connect('LoginDB.db') as con:
            cur = con.cursor()
            pass_user = cur.execute('SELECT username, password FROM Login WHERE username = ? AND password = ?', (username_entry.get(), password_entry.get())).fetchone()
            
            if pass_user == None: print('Invalid Username or Password')
            else: success_window(0)
    
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    
    ttk.Button(mainframe, text='Submit', command=select_pass_user).grid(column=3, row=2, sticky=(W,E))
    ttk.Button(mainframe, text='Sign Up', command=signup_window).grid(column=3, row=1, sticky=(W,E))
    root.mainloop()