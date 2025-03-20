from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename

window=Tk()
window.title("text editer")
window.geometry("600x500")

window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

text_editer=Text(window)
frame_btn=Frame(window,relief=RAISED,bd=2)

def open_file():
    pass

def save_file():
    pass

btn_open=Button(frame_btn,text="open",command=open_file)
btn_save=Button(frame_btn,text="save",command=save_file)

text_editer.grid(row=0,column=1,sticky="ns")
frame_btn.grid(row=0,column=0,sticky="ns")
btn_open.grid(row=0,column=0,sticky="ns")
btn_save.grid(row=1,column=0,sticky="ns")
window.mainloop()