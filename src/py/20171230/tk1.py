import tkinter as t

tk = t.Tk()
tk.title("title")
tk.geometry("640x480")

x = t.Label(text="label")
x.pack()

x = t.Entry()
x.pack()

x = t.Button(text="button")
x.bind("<Button-1>", lambda self: print("hello, world"))
x.pack()

true = t.BooleanVar()
true.set(True)
x = t.Checkbutton(text="checkbutton", variable=true)
x.pack()

tk.mainloop()
