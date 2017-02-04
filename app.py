from components.app import *

root = Tk()
root.title(string="QHacks Python Reader")
root.iconbitmap("favicon.ico")
root.minsize(width=800, height=300)
root.resizable(width=False, height=False)
app = App(root)
app.pack()
root.mainloop()
