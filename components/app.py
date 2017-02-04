from tkinter import *
from tkinter.ttk import *


class App(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.msg = Message(master, width=700, text="Please enter your python line of code to analyse.", pady=10,
                           padx=10)
        self.msg.config(font=('times', 16, 'italic'))
        self.msg.pack()
        self.form = Form(self)
        self.form.pack()
        self.sep = Separator(orient=HORIZONTAL)
        self.sep.pack()
        self.outbox = Output(self)
        self.outbox.pack()


# FIXME Currently text box allows new line, need to remove this.
class Form(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.input = Text(self, height=1, wrap=NONE, pady=10, padx=10)
        self.input.pack()
        self.button = Button(self,
                             text="Read",
                             command=self.read_input)
        self.button.pack()

    def read_input(self):
        # TODO Add parsing system and get returned text.
        self.master.outbox.updateoutput(self.input.get("1.0", '2.0'))  # Reads first line of textbox only.


class Output(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.outputtext = StringVar()
        self.outboxFrame = LabelFrame(self, text="Output", labelanchor="n")
        self.outboxFrame.pack()
        self.s = Label(self.outboxFrame, textvariable=self.outputtext, width=125)
        self.s.pack()

    def updateoutput(self, outputtext):
        self.outputtext.set(outputtext)
