import sqlite3, re
from tkinter import *
from tkinter import ttk
from types import NoneType
from success_window import success_window

def signup_window():
    root = Toplevel()
    root.title('Sign Up')
    
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    ttk.Label(mainframe, text='Username').grid(column=1, row=1, sticky=(W,E))
    ttk.Label(mainframe, text='Password').grid(column=2, row=1, sticky=(W,E))
    ttk.Label(mainframe, text='Email').grid(column=3, row=1, sticky=(W,E))
    
    username_get = StringVar()
    email_get = StringVar()
    password_get = StringVar()
    
    ttk.Entry(mainframe, width=20, textvariable=username_get).grid(column=1, row=2, sticky=(W,E))
    ttk.Entry(mainframe, width=20, textvariable=password_get).grid(column=2, row=2, sticky=(W,E))
    ttk.Entry(mainframe, width=20, textvariable=email_get).grid(column=3, row=2, sticky=(W,E))
    
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    
    def submit_values():
        with sqlite3.connect('LoginDB.db') as con:
            cur = con.cursor()
            
            username = username_get.get()
            email = email_get.get()
            password = password_get.get()
            
            if len(username) == 0 or len(email) == 0 or len(password) == 0:
                print('Username, Password and Email are required.')
                return

            if re.search(regex, email) is None:
                print('Invalid email.')
                return

            if len(username) < 3:
                print('Username must be atleast 3 Characters long.')
                return
            
            if len(password) < 6:
                print('Password must be atleast 6 Characters long.')
                return
            
            user = cur.execute('SELECT username FROM Login WHERE username=?', (username,)).fetchone()

            if type(user) != NoneType:
                print('Username is already taken.')
                return
            
            cur_email = cur.execute('SELECT email FROM Login WHERE email = ?', (email,)).fetchone()
            
            if type(cur_email) != NoneType:
                print('Email already exists.')
                return
            
            cur.execute('INSERT INTO Login(username, password, email) VALUES(?,?,?)', (username, password, email))
            success_window(1)
            
    ttk.Button(mainframe, text='Submit', command=submit_values).grid(column=4, row=2, sticky=(W,E))
    
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    
    root.mainloop()