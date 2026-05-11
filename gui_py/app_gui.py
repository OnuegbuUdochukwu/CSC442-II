import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import src.db as db

MICROSCOPE_CHOICES = [
    ('Light Microscope (40x)', 40.0),
    ('Compound Microscope (100x)', 100.0),
    ('Electron Microscope (1000x)', 1000.0),
    ('Scanning EM (20000x)', 20000.0)
]

UNIT_CHOICES = ['nm', 'um', 'mm', 'cm', 'm']
UNIT_CONVERSIONS = {'nm':1e6,'um':1e3,'mm':1.0,'cm':0.1,'m':0.001}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Microscope Specimen Size Calculator (GUI)')
        db.init_db()
        self.create_widgets()

    def create_widgets(self):
        frm = ttk.Frame(self, padding=10)
        frm.grid()

        ttk.Label(frm, text='Username').grid(column=0, row=0)
        self.username = ttk.Entry(frm)
        self.username.grid(column=1, row=0)

        ttk.Label(frm, text='Image').grid(column=0, row=1)
        self.img_path = ttk.Entry(frm, width=40)
        self.img_path.grid(column=1, row=1)
        ttk.Button(frm, text='Browse', command=self.browse_image).grid(column=2, row=1)

        ttk.Label(frm, text='Measured (mm)').grid(column=0, row=2)
        self.measured = ttk.Entry(frm)
        self.measured.grid(column=1, row=2)

        ttk.Label(frm, text='Microscope Type').grid(column=0, row=3)
        self.mscope = ttk.Combobox(frm, values=[m[0] for m in MICROSCOPE_CHOICES], state='readonly')
        self.mscope.current(0)
        self.mscope.grid(column=1, row=3)

        ttk.Label(frm, text='Output Unit').grid(column=0, row=4)
        self.unit = ttk.Combobox(frm, values=UNIT_CHOICES, state='readonly')
        self.unit.current(2)
        self.unit.grid(column=1, row=4)

        ttk.Button(frm, text='Calculate', command=self.calculate).grid(column=1, row=5)

        self.result_var = tk.StringVar()
        ttk.Label(frm, textvariable=self.result_var).grid(column=0, row=6, columnspan=3)

        ttk.Button(frm, text='View History', command=self.view_history).grid(column=0, row=7)

    def browse_image(self):
        p = filedialog.askopenfilename(filetypes=[('Images','*.png;*.jpg;*.jpeg;*.bmp;*.gif')])
        if p:
            self.img_path.delete(0, tk.END)
            self.img_path.insert(0, p)

    def calculate(self):
        username = self.username.get().strip()
        if not username:
            messagebox.showerror('Error','Username required')
            return
        try:
            measured_mm = float(self.measured.get().strip())
        except Exception:
            messagebox.showerror('Error','Measured value invalid')
            return
        idx = self.mscope.current()
        mag = MICROSCOPE_CHOICES[idx][1]
        unit = self.unit.get()
        real_mm = measured_mm / mag
        converted = real_mm * UNIT_CONVERSIONS[unit]
        self.result_var.set(f'{converted:.6g} {unit} (real: {real_mm:.6g} mm)')
        db.insert_record(username, self.img_path.get() or None, measured_mm, real_mm, unit)
        messagebox.showinfo('Saved','Calculation saved to database')

    def view_history(self):
        rows = db.list_records()
        win = tk.Toplevel(self)
        win.title('History')
        lb = tk.Listbox(win, width=100)
        lb.pack()
        for r in rows:
            lb.insert(tk.END, f"{r[0]} | {r[1]} | measured={r[3]}mm | real={r[4]:.6g}mm | unit={r[5]} | {r[6]}")

if __name__ == '__main__':
    app = App()
    app.mainloop()
