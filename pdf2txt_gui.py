import Tkinter as tk
import tkFileDialog
from pdf2txt_pypdf2 import pdf2txt

print "selecciona el pdf"

root = tk.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename()

filename = pdf2txt(filename)
print "el texto quedo en {}".format(filename)

