#!/usr/bin/python

import Tkinter

class Tkapp(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()


        track_button = Tkinter.Button(self,text=u"Track",
                command=lambda: self.ButtonClick("track; $ra; $dec"))
        track_button.grid(column=0,row=0,sticky="W")

        posn_button = Tkinter.Button(self,text=u"Posn",
                command=lambda: self.ButtonClick("posn; $ra; $dec"))
        posn_button.grid(column=1,row=0,sticky="W")

        park_button = Tkinter.Button(self,text=u"Park",
                command=lambda: self.ButtonClick("park"))
        park_button.grid(column=2,row=0,sticky="W")

        wait_sec_button = Tkinter.Button(self,text=u"Wait Sec",
                command=lambda: self.ButtonClick("wait; sec; $seconds"))
        wait_sec_button.grid(column=0,row=1,sticky="W")

        wait_lst_button = Tkinter.Button(self,text=u"Wait LST",
                command=lambda: self.ButtonClick("wait; lst; $lst"))
        wait_lst_button.grid(column=1,row=1,sticky="W")

        frb_button = Tkinter.Button(self,text=u"FRB Search",
                command=lambda: self.ButtonClick("fb; $type; $name; $ra; $dec; $tmax"))
        frb_button.grid(column=0,row=2,sticky="W")



        tb_button = Tkinter.Button(self,text=u"indiv",
                command=lambda: self.ButtonClick("tb; $type; $tmax"))
        tb_button.grid(column=0,row=3,sticky="W")

        modtb_button = Tkinter.Button(self,text=u"modtb",
                command=lambda: self.ButtonClick("modtb; $type; $tmax"))
        modtb_button.grid(column=1,row=3,sticky="W")

        fold_button = Tkinter.Button(self,text=u"fold",
                command=lambda: self.ButtonClick("fold; $jname; $tmax"))
        fold_button.grid(column=2,row=3,sticky="W")

        


        add_button = Tkinter.Button(self,text=u"add",
                command=self.flush)
        add_button.grid(column=10,row=4,sticky="W")

        remove_button = Tkinter.Button(self,text=u"Remove last",
                command=self.remove_last)
        remove_button.grid(column=11,row=4,sticky="W")


        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=0,row=4,columnspan=5,sticky="EW")
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"")


        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                anchor="w",fg="white",bg="blue",justify=Tkinter.LEFT)
        label.grid(column=0,row=5,columnspan=5,sticky="EW")
        self.labelVariable.set(u"")



#        self.grid_columnconfigure(1,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+" (Clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def ButtonClick(self,txt=""):
        self.entryVariable.set(txt)
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self,event):
        self.labelVariable.set(self.entryVariable.get()+" (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def flush(self):
        if self.entryVariable.get():
            cleaned = self.labelVariable.get()+"\n"+self.entryVariable.get()
            cleaned = cleaned.rstrip("\n").lstrip("\n")
            self.labelVariable.set(cleaned)

    def remove_last(self):
        tmp = self.labelVariable.get().split("\n")[:-1]
        updated = ""
        for i in tmp:
            updated += i+"\n"
        self.labelVariable.set(updated.rstrip("\n"))

if __name__ == "__main__":
    app = Tkapp(None)
    app.title('Automatic Mode GUI')
    app.mainloop()
