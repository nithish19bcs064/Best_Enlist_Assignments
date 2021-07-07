import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

root = tk.Tk()

canvas1 = tk.Canvas(root, width=550, height=350, bg='gray95', relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Image Covertor GUI From JPEG To PNG')
label1.config(font=('helvetica', 20))
label2=tk.Label(root,text='Step1: First select the File you want to convert to png')
label2.config(font=('Timesnewroman',15))
label3=tk.Label(root,text='Step2: Click the button convert to png')
label3.config(font=('Timesnewroman',15))
canvas1.create_window(250,40, window=label1)
canvas1.create_window(280,80, window=label2)
canvas1.create_window(260,120, window=label3)


def getJPG():
    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)


browseButton_JPG = tk.Button(text="      Import JPG File     ", command=getJPG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(270, 200, window=browseButton_JPG)


def convertToPNG():
    global im1

    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    im1.save(export_file_path)


saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(270, 280, window=saveAsButton_PNG)

root.mainloop()