import Tkinter as tk
import tkFileDialog

print "selecciona el blah1.txt"

root = tk.Tk()
root.withdraw()
filename = tkFileDialog.askopenfilename()
filebase = filename[:-5]

text = ""
fileno = 1
while True:
    filename = "{}{}.txt".format(filebase, fileno)
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except:
        break
    text += data + '\n'    
    fileno += 1

filename = "{}_concat.txt".format(filebase)
with open(filename, 'w') as f:
    f.write(text)

print "listo, {} generado".format(filename)
