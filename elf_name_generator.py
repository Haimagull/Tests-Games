#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: haimagull

This code generates a name with elfic sounds for each of you !
The background image was made with AI chat GPT.
"""

"""
Definition of language functions
"""
def simple (word): # this function simplifies the typography
    word = word.replace(" ","")
    word = word.replace("-","") 
    word = word.replace("'","") 
    word = word.replace("é","e") 
    word = word.replace("è","e") 
    word = word.replace("É","e") 
    word = word.replace("È","e") 
    return word
    print(word)
    
def elfic (word): # this function mimics an elfic translation
    #double letters
    word = word.replace("nn","n")
    word = word.replace("rr","r")
    word = word.replace("tt","t")
    word = word.replace("pp","p")
    word = word.replace("ss","s")
    word = word.replace("dd","d")
    word = word.replace("ff","f")
    word = word.replace("gg","g")
    word = word.replace("ll","l")
    word = word.replace("mm","m")
    word = word.replace("bb","b")
    #nasal sounds (especially for french)
    word = word.replace("On","O")
    word = word.replace("on","o")
    word = word.replace("ont","o")
    word = word.replace("An","a")
    word = word.replace("an","a")
    word = word.replace("ant","a")
    word = word.replace("En","e")
    word = word.replace("ent","e")
    word = word.replace("In","I")
    word = word.replace("in","i")
    word = word.replace("int","i")
    word = word.replace("Ain","a")
    word = word.replace("ain","a")
    word = word.replace("aint","a")
    #vowels
    word = word.replace("A","u")
    word = word.replace("e","ir")
    word = word.replace("u","i")
    word = word.replace("U","Nu")
    word = word.replace("H","Di")
    word = word.replace("h","l")
    word = word.replace("O","A")
    word = word.replace("Y","U")
    word = word.replace("y","u")

    return word
    print(word)

"""
Algorythm
"""
import tkinter as tk
from tkinter import simpledialog, ttk
from PIL import Image, ImageTk

def generate_elfname():
    name = simpledialog.askstring("Input", "What is you middle name ?", parent=root)
    if not name:
        return
    name = elfic(name)
    name = simple(name)
    name = name.capitalize()
    
    mom = simpledialog.askstring("Input", "What is you mother's name ?", parent=root)
    if not mom:
        return
    mom = elfic(mom)
    mom = simple(mom)
    mlist = [] #initializing lists, letters
    for i in range(len(mom)): #transforming forename -> list of letters
        mlist.append(mom[i])
    head = mlist[:len(mlist)//2] # separating list in two
    tail = mlist[len(mlist)//2:]
    
    city = simpledialog.askstring("Input", "In which city were you born ?", parent=root)
    if not city :
        return
    city = elfic(city)
    city = simple(city)
    dlist = city.split() #changing str -> list
    body = dlist #just for the fun of it
    
    sfnlist = head + body + tail #creating the elfic name as a list
    elfname = ''.join(sfnlist) #turning list back into str
    elfname = elfname.capitalize() #Everything lowercase except the first one
    
    # Display new name in the label
    result_label.config(text=f"Welcome to the wonderful elfic world : {name} {elfname}")
  
"""
Visual interface
"""
   
#Config
root = tk.Tk()
root.title("Elf name generator")

#Uploading background image
try:
    bg_image = Image.open("/Applications/Documents/Codes/IA_bg_elfname.jpg")  # Calling image
    bg_image = bg_image.resize((1400, 800))  # Resizing according to window size
    bg_photo = ImageTk.PhotoImage(bg_image)
    # creating canvas
    canvas = tk.Canvas(root, width=1000, height=500)
    canvas.pack()
    # add background image to canva
    root.bg_photo=bg_photo # to not delete the image (save it in root)
    canvas.create_image(0, 0, anchor="nw", image=root.bg_photo)

except Exception as e:
    print("Display error", e) #if error to display background image
    
# Styles
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="white", foreground="#004d00", font=("Arial", 12))
style.map("TButton", background=[("active", "lightgrey")])
# Main label
label = ttk.Label(root, text="Enter elfic world", font=("Arial", 14), background="#004d00", foreground="#004d00")
label.pack(pady=20)
# Button to start
btn_generate = ttk.Button(root, text="Get my elfic name", command=generate_elfname)
btn_generate.pack(pady=10)
# Results label
result_label = ttk.Label(root, text="", font=("Arial", 12), background="#004d00", foreground="#004d00")
result_label.pack(pady=20)
# Start app
root.mainloop()
