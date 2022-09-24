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
            
            if len(username) != 0 and len(email) != 0 and len(password) != 0:
                if re.search(regex, email):
                    if len(username) >=3:
                        if len(password) >= 6:
                            user = cur.execute('SELECT username FROM Login WHERE username=?', (username,)).fetchone()
                            if type(user) == NoneType:
                                cur_email = cur.execute('SELECT email FROM Login WHERE email = ?', (email,)).fetchone()
                                if type(cur_email) == NoneType:
                                    cur.execute('INSERT INTO Login(username, password, email) VALUES(?,?,?)', (username, password, email))
                                    success_window(1)
                                else: print('Email already exists.')
                            else: print('Username is already taken.')
                        else: print('Password must be atleast 6 Characters long.')
                    else: print('Username must be atleast 3 Characters long.')
                else: print('Invalid email.')
            else: print('Username, Password and Email are required.')
            
    ttk.Button(mainframe, text='Submit', command=submit_values).grid(column=4, row=2, sticky=(W,E))
    
    for child in mainframe.winfo_children(): 
        child.grid_configure(padx=5, pady=5)
    
    root.mainloop()