from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("800x400")
root.configure(bg = "blue")
root.title("Language Translator")

language = list(LANGUAGES.values())

title_label = Label(root, text = "Language Translator")
title_label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

input_label = Label(root, text = "Enter text")
input_label.place(relx = 0.02, rely = 0.2, anchor = W)

src_lang = ttk.Combobox(root, values = language, width = 22, state = "readonly")
src_lang.place(relx = 0.13, rely = 0.2, anchor = W)
src_lang.set('english')

output_label = Label(root, text = "Output")
output_label.place(relx = 0.81, rely = 0.2, anchor = E)

dest_lang = ttk.Combobox(root, values = language, width = 22, state = "readonly")
dest_lang.place(relx = 0.98, rely = 0.2, anchor = E)
dest_lang.set('choose output language')

input_text = Text(root, height = 11, wrap = WORD, padx = 5, pady =5, width = 50)
input_text.place(relx = 0.02, rely = 0.5, anchor = W)

output_text = Text(root, height = 11, wrap = WORD, padx = 5, pady =5, width = 50)
output_text.place(relx = 0.98, rely = 0.5, anchor = E)

def translate():
    translator = Translator()
    try:
        translatated = translator.translate(text = input_text.get(1.0, END), src = src_lang.get(), dest = dest_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
        
    except:
        print("Try Again")

button = Button(root, text = "Translate", command = translate)
button.place(relx = 0.5, rely = 0.85, anchor = CENTER)

footer_label = Label(root, text = "Created By : Suhasini")
footer_label.place(relx = 0.5, rely = 0.95, anchor = CENTER)

        
root.mainloop()
