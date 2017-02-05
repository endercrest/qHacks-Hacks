from tkinter import *
from tkinter.ttk import *
from helpers.py2face import pythontoenglish

class App(Frame): # calling a bunch of classes in the main app frame
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.msg = Message(master, width=600, text="Please enter your python line of code to analyse.", pady=10,
                           padx=10)
        self.msg.config(font=('times', 16, 'italic'))
        self.msg.pack()      
        self.form = Form(self)
        self.form.pack()
        self.sep = Separator(orient=HORIZONTAL)
        self.sep.pack()
        self.outbox = Output(self)
        self.outbox.pack()
        self.answerLabels = answerLabels(self)
        self.answerLabels.pack(side=TOP)
        self.userOutput = answerbox(self)
        self.userOutput.pack()


class Form(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.input = Text(self, height=1, wrap=NONE, pady=10, padx=10) 
        self.input.bind('<Return>', self.read_input) #bind user input to return and reads it
        self.input.pack()
        self.button = Button(self, text="Read", command=self.read_input) #button reads user input
        self.button.bind('<Return>', self.read_input)
        self.button.pack(side=LEFT)
        self.clr = Button(self, text="Clear", command = self.clearbox)#clear button
        self.clr.pack(side=RIGHT)
               
    def clearbox(self): #clears the text field
        self.input.delete('1.0', 'end')
 
    def read_input(self, event = None): #read and update return statement from input
        # TODO Add parsing system and get returned text.
        self.master.outbox.updateoutput(pythontoenglish(self.input.get("1.0", '2.0')))
        #self.master.outbox.updateoutput(self.input.get("1.0", '2.0'))
        return "break"

        
            
class Output(Frame): #returns user input under the 'output' frame 
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.outputtext = StringVar()
        self.outboxFrame = LabelFrame(self, text="Output", labelanchor="n")
        self.outboxFrame.pack()
        self.s = Label(self.outboxFrame, textvariable=self.outputtext, width=125)
        self.s.pack()
        
    def updateoutput(self, outputtext): #update output
        self.outputtext.set(outputtext)
    
    def Enterkey(self, outputtext): #create enter key shorcut
        self.outputtext.set(outputtext)



class answerLabels(Frame): #Labels for the answers
    def __init__(self, master, **kw):
        super().__init__(master, **kw)   
        self.label1 = Label(self, text="Computer Code\t\t\t\t\t\t\tAnswer")
        self.label1.pack()


class answerbox(Frame): #The user answer in terms of code and evaluated answer is printed here
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.LeftTextbox = Text(self, width = 45, height = 15) #create left textbox (code output)
        self.LeftTextbox.pack(side=LEFT)
        self.RightTextbox = Text(self, width = 45, height = 15) #create right textbox (evaluated output0
        self.RightTextbox.pack(side=RIGHT)
        
