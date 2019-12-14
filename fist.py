from subprocess import call
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import fisrt_support
from sys import exit

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = main_from (root)
    fisrt_support.init(root, top)
    root.mainloop()

w = None
def create_main_from(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = main_from (w)
    fisrt_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_main_from():
    global w
    w.destroy()
    w = None



class main_from:
    def emngBtn_Click(self):
        call(["python","seconddd.py"])
    def train_btn_Click(self):
        call(["python","face_trainer.py"])
    def atendbtn_Click(self):
        call(["python","detector.py"])
    def repbtn_click(self):
        call(["python","report.py"])
    def exitbtn_click(self):
        msg=messagebox.askyesno("Quiting","Cancel Face Recogniton System?")
        if(msg):
            exit()
    def aboutbtn_click(self):
        messagebox.showinfo("Developer","Umesh KH and SriVatsa N Overseen by Rashmi CR(Asst Prof Dept of CSE,CIT)")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1006x560+514+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Main System")
        top.configure(background="#b6b9fc")

        self.emngBtn = tk.Button(top)
        self.emngBtn.place(relx=0.089, rely=0.214, height=173, width=256)
        self.emngBtn.configure(activebackground="#ececec")
        self.emngBtn.configure(activeforeground="#000000")
        self.emngBtn.configure(background="#d9d9d9")
        self.emngBtn.configure(disabledforeground="#a3a3a3")
        self.emngBtn.configure(foreground="#000000")
        self.emngBtn.configure(highlightbackground="#d9d9d9")
        self.emngBtn.configure(highlightcolor="black")
        self.emngBtn.configure(pady="0")
        self.emngBtn.configure(text='''Employee Manegement''')
        self.emngBtn.configure(command=self.emngBtn_Click)

        self.train_btn = tk.Button(top)
        self.train_btn.place(relx=0.388, rely=0.214, height=173, width=256)
        self.train_btn.configure(activebackground="#ececec")
        self.train_btn.configure(activeforeground="#000000")
        self.train_btn.configure(background="#d9d9d9")
        self.train_btn.configure(disabledforeground="#a3a3a3")
        self.train_btn.configure(foreground="#000000")
        self.train_btn.configure(highlightbackground="#d9d9d9")
        self.train_btn.configure(highlightcolor="black")
        self.train_btn.configure(pady="0")
        self.train_btn.configure(command=self.train_btn_Click,text='''Train System''')

        self.atend_btn = tk.Button(top)
        self.atend_btn.place(relx=0.089, rely=0.607, height=173, width=256)
        self.atend_btn.configure(activebackground="#ececec")
        self.atend_btn.configure(activeforeground="#000000")
        self.atend_btn.configure(background="#d9d9d9")
        self.atend_btn.configure(disabledforeground="#a3a3a3")
        self.atend_btn.configure(foreground="#000000")
        self.atend_btn.configure(highlightbackground="#d9d9d9")
        self.atend_btn.configure(highlightcolor="black")
        self.atend_btn.configure(pady="0")
        self.atend_btn.configure(command=self.atendbtn_Click,text='''Autometic Attendence System''')

        self.report_btn = tk.Button(top)
        self.report_btn.place(relx=0.696, rely=0.214, height=173, width=256)
        self.report_btn.configure(activebackground="#ececec")
        self.report_btn.configure(activeforeground="#000000")
        self.report_btn.configure(background="#d9d9d9")
        self.report_btn.configure(disabledforeground="#a3a3a3")
        self.report_btn.configure(foreground="#000000")
        self.report_btn.configure(highlightbackground="#d9d9d9")
        self.report_btn.configure(highlightcolor="black")
        self.report_btn.configure(pady="0")
        self.report_btn.configure(command=self.repbtn_click,text='''Attendence Report''')

        self.about_btn = tk.Button(top)
        self.about_btn.place(relx=0.388, rely=0.607, height=173, width=256)
        self.about_btn.configure(activebackground="#ececec")
        self.about_btn.configure(activeforeground="#000000")
        self.about_btn.configure(background="#d9d9d9")
        self.about_btn.configure(disabledforeground="#a3a3a3")
        self.about_btn.configure(foreground="#000000")
        self.about_btn.configure(highlightbackground="#d9d9d9")
        self.about_btn.configure(highlightcolor="black")
        self.about_btn.configure(pady="0")
        self.about_btn.configure(command=self.aboutbtn_click,text='''About Developer''')

        self.exit_btn = tk.Button(top)
        self.exit_btn.place(relx=0.696, rely=0.607, height=173, width=256)
        self.exit_btn.configure(activebackground="#ececec")
        self.exit_btn.configure(activeforeground="#000000")
        self.exit_btn.configure(background="#d9d9d9")
        self.exit_btn.configure(disabledforeground="#a3a3a3")
        self.exit_btn.configure(foreground="#000000")
        self.exit_btn.configure(highlightbackground="#d9d9d9")
        self.exit_btn.configure(highlightcolor="black")
        self.exit_btn.configure(pady="0")
        self.exit_btn.configure(command=self.exitbtn_click,text='''Exit''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.219, rely=0.054, height=36, width=532)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(state='active')
        self.Label1.configure(text='''Face Recognition Attendence System''')

if __name__ == '__main__':
    vp_start_gui()





