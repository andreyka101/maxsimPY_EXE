from tkinter import *


def clicer():
    text.configure(text=lang.get())
    if (lang.get() == "pythonT"):
        window.configure(bg = '#ff0a0a')
    if (lang.get() == "javascriptT"):
        window.configure(bg = '#bf00ff')
    if (lang.get() == "javaT"):
        window.configure(bg = '#ffee00')


window = Tk()
window.title("clicker")
window.configure(bg = '#33c5ff')
window.geometry('400x250')

lang = StringVar(value="javascriptT")

# button = Button(text="0", command=clicer)
# button.place(h=61 , w=61 , x=170 , y = 95)

text = Label(text=lang.get())
text.place(h=11 , x=0 , y = 120)

python_btn = Radiobutton(window , text="python" , value="pythonT" , variable=lang, command=clicer)
# python_btn.pack(**position)
python_btn.place(x=0 , y = 0)

javascript_btn = Radiobutton(text="javascript", value="javascriptT", variable=lang, command=clicer)
javascript_btn.place(x=0 , y = 40)
 
java_btn = Radiobutton(text='java', value="javaT", variable=lang, command=clicer)
java_btn.place(x=0 , y = 80)

window.mainloop()

