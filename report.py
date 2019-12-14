import sys
import mysql.connector
from tkinter import *

conn= mysql.connector.connect(host="127.0.0.1", user="root", password="tiger",database="employee")
cursor = conn.cursor()

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import report_support

def vp_start_gui():

    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    report_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):

    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    report_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def repshowbtn_click(self):
        cursor.execute("select *from attend")
        for i in cursor:
            self.Listbox1.insert(END,i)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.083, rely=0.156, relheight=0.811
                , relwidth=0.892)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Listbox1 = tk.Listbox(self.Frame1)
        self.Listbox1.place(relx=0.243, rely=0.027, relheight=0.899
                , relwidth=0.736)
        self.Listbox1.configure(background="white")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="-family {Courier New} -size 10")
        self.Listbox1.configure(foreground="#000000")

        self.repshowbtn = tk.Button(self.Frame1)
        self.repshowbtn.place(relx=0.019, rely=0.055, height=33, width=106)
        self.repshowbtn.configure(activebackground="#ececec")
        self.repshowbtn.configure(activeforeground="#000000")
        self.repshowbtn.configure(background="#d9d9d9")
        self.repshowbtn.configure(disabledforeground="#a3a3a3")
        self.repshowbtn.configure(foreground="#000000")
        self.repshowbtn.configure(highlightbackground="#d9d9d9")
        self.repshowbtn.configure(highlightcolor="black")
        self.repshowbtn.configure(pady="0")
        self.repshowbtn.configure(command=self.repshowbtn_click,text='''Show''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.3, rely=0.022, height=43, width=228)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(state='active')
        self.Label1.configure(text='''Attendence Report''')

if __name__ == '__main__':
    vp_start_gui()





