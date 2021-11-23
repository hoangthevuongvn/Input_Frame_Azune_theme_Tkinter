from tkinter.constants import LEFT
from tkinter import *
import tkinter as tk
from tkinter import ttk

class CheckButton():

    def __init__(self, container):
        self.container = container
        self.create_widgets()

    def create_widgets(self):
        Checkbutton1 = IntVar()  
        Checkbutton2 = IntVar()  
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        
        Button1 = Checkbutton(self.container, text = "Option 1", 
                            variable = Checkbutton1,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)
        
        Button2 = Checkbutton(self.container, text = "Option 2",
                            variable = Checkbutton2,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)
        
        Button3 = Checkbutton(self.container, text = "Option 3",
                            variable = Checkbutton3,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)
        Button4 = Checkbutton(self.container, text = "Option 4",
                            variable = Checkbutton4,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)
        
        Button1.grid(row=0, padx=(10,15), pady=(10,10))
        Button2.grid(row=1, padx=(10,15), pady=(10,10))
        Button3.grid(row=2, padx=(10,15), pady=(10,10))
        Button4.grid(row=3, padx=(10,15), pady=(10,10))


class RadioButton():

    def __init__(self, container):
        self.container = container
        self.create_widgets()

    def create_widgets(self):

        Radiobutton1 = IntVar()
        Radiobutton2 = IntVar()
        Radiobutton3 = IntVar()

        Button1 = Radiobutton(self.container, text="Option 1", variable=Radiobutton1, value=1, width = 10)
        Button2 = Radiobutton(self.container, text="Option 2", variable=Radiobutton2, value=1)
        Button3 = Radiobutton(self.container, text="Option 3", variable=Radiobutton3, value=1)
        
        Button1.grid(row=0, column=0, padx=(10,15), pady=(10,10))
        Button2.grid(row=1, column=0, padx=(10,15), pady=(10,10))
        Button3.grid(row=2, column=0, padx=(10,15), pady=(10,15))

class ButtonFrame2():
    is_on = ''
    n1 = ''
    def __init__(self, container):
        self.container = container
        self.create_widgets()
    
    def create_widgets(self):

        E = ttk.Entry(self.container, width=15)
        E.insert(0, 'Entry')
        E.grid(row=0, column=0, padx=(10,10), pady=8)

        #Spinbox
        SP = ttk.Spinbox(
        self.container,
        from_=0,
        to=5,
        textvariable='',
        wrap=True,
        width=15)
        SP.insert(0, "Spin box")
        SP.grid(row=1, column=0, padx=(10,10), pady=15)

        #Combobox
        ButtonFrame2.n1 = tk.StringVar()
        Combo = ttk.Combobox(self.container, width = 15, textvariable = ButtonFrame2.n1)
        # Adding combobox drop down list
        months = ('Jan', 'Fed', 'Mar', 'Apr', 'May', 'Jun', 'Aug', 'Sep', 'Now', 'Now', 'Dec', 'Combobox')
        Combo['values'] = months
        Combo['state'] = 'readonly'
        Combo.current(11)
        Combo.grid(column = 0, row = 2, pady=15, padx=(10,10))
        
        #MenuButton
        mb1 =  ttk.Menubutton(self.container, text="Menu Button", width = 13)
        mb1.grid(row=3, column=0, padx=(10,10), pady=15)

        mb2 =  ttk.Menubutton(self.container, text="Option Menu", width = 13)
        mb2.grid(row=4, column=0, padx=(10,10), pady=15)

        #Button
        B1 = ttk.Button(self.container, text = "Button", width=15)
        B1.grid(row=5,column=0, padx=(15,15), pady=15)

        B2 = ttk.Button(self.container, text = "Accent Button", width=15, style='Accent.TButton' )
        B2.grid(row=6,column=0, padx=(10,10), pady=15)

        B3 = ttk.Button(self.container, text = "Toggle Button", style='Toggle.TButton', width=15)
        B3.grid(row=7,column=0, padx=(10,10), pady=15)
        
        print(B1.winfo_class())
        s = ttk.Style()
        s.configure('Accent.TButton', background='green')
        # B4 = Check
        def button_mode():
            #Determine it is on or off
            if ButtonFrame2.is_on:
                on_.config(image=off)
                ButtonFrame2.is_on = False
                print(ButtonFrame2.is_on)
            else:
                on_.config(image = on)
                ButtonFrame2.is_on = True
                print(ButtonFrame2.is_on)
        on = PhotoImage(file ="on-accent.png")
        off = PhotoImage(file ="off-basic.png")
        on_= Button(self.container ,image =on,bd =0,command = button_mode, text="Switch")
        on_.grid(row=8,column=0, padx=(10,10), pady=8, sticky=W)
        
# class Theme():

#     def __init__(self, container):
#         self.container = container
#         self.create_widgets()
    
#     def create_widgets(self):
#         self.container.selected_theme = tk.StringVar()
#         theme_frame = ttk.LabelFrame(self.container, text='Themes')
#         theme_frame.grid(padx=10, pady=10, ipadx=20, ipady=20, sticky='w')

#         for theme_name in self.container.style.theme_names():
#             rb = ttk.Radiobutton(
#                 theme_frame,
#                 text=theme_name,
#                 value=theme_name,
#                 variable=self.container.selected_theme,
#                 command=lambda : self.container.style.theme_use(self.container.selected_theme.get())
#             rb.pack(expand=True, fill='both')

class Treev():

    def __init__(self, container):
        self.container = container
        self.create_widgets()

    def create_widgets(self):

        
        scrollbar = ttk.Scrollbar(self.container)
        # scrollbar.grid(row=0, column=1, sticky=NE)
        scrollbar.pack(side="right", fill="y")

        treev = ttk.Treeview(
            self.container,
            selectmode="browse",
            yscrollcommand=scrollbar.set,
            columns=(1, 2),
            height=10,
        )
        treev.pack(side="right", fill="y")
        scrollbar.config(command=treev.yview)

        

        treev.column("#0", anchor="w", width=120)
        treev.column(1, anchor="w", width=120)
        treev.column(2, anchor="w", width=120)

        treev.heading("#0", text="Column 1", anchor="center")
        treev.heading(1, text="Column 2", anchor="center")
        treev.heading(2, text="Column 3", anchor="center")

        treev_obj = [
            ("", 1, "Parent", ("Item 1", "Value 1")),
            (1, 2, "Child", ("Subitem 1.1", "Value 1.1")),
            (1, 3, "Child", ("Subitem 1.2", "Value 1.2")),
            (1, 4, "Child", ("Subitem 1.3", "Value 1.3")),
            (1, 5, "Child", ("Subitem 1.4", "Value 1.4")),
            ("", 6, "Parent", ("Item 2", "Value 2")),
            (6, 7, "Child", ("Subitem 2.1", "Value 2.1")),
            (6, 8, "Sub-parent", ("Subitem 2.2", "Value 2.2")),
            (8, 9, "Child", ("Subitem 2.2.1", "Value 2.2.1")),
            (8, 10, "Child", ("Subitem 2.2.2", "Value 2.2.2")),
            (8, 11, "Child", ("Subitem 2.2.3", "Value 2.2.3")),
            (6, 12, "Child", ("Subitem 2.3", "Value 2.3")),
            (6, 13, "Child", ("Subitem 2.4", "Value 2.4")),
            ("", 14, "Parent", ("Item 3", "Value 3")),
            (14, 15, "Child", ("Subitem 3.1", "Value 3.1")),
            (14, 16, "Child", ("Subitem 3.2", "Value 3.2")),
            (14, 17, "Child", ("Subitem 3.3", "Value 3.3")),
            (14, 18, "Child", ("Subitem 3.4", "Value 3.4")),
            ("", 19, "Parent", ("Item 4", "Value 4")),
            (19, 20, "Child", ("Subitem 4.1", "Value 4.1")),
            (19, 21, "Sub-parent", ("Subitem 4.2", "Value 4.2")),
            (21, 22, "Child", ("Subitem 4.2.1", "Value 4.2.1")),
            (21, 23, "Child", ("Subitem 4.2.2", "Value 4.2.2")),
            (21, 24, "Child", ("Subitem 4.2.3", "Value 4.2.3")),
            (19, 25, "Child", ("Subitem 4.3", "Value 4.3")),
        ]

        for item in treev_obj:
            treev.insert(
                parent=item[0], index="end", iid=item[1], text=item[2], values=item[3]
            )
            if item[0] == "" or item[1] in {8, 21}:
                treev.item(item[1], open=True) 

        
        

class Notebooks():
    scale_var = ""
    def __init__(self, container):
        self.container = container
        self.create_widgets()

    def create_widgets(self):
     
        notebook = ttk.Notebook(self.container)
        notebook.grid(row=1,column=0, pady=8, sticky=W)

        # Tab #1
        tab1 = ttk.Frame(notebook)
        for i in [0, 1]:
            tab1.columnconfigure(i, weight=1)
            tab1.rowconfigure(i, weight=1)
        notebook.add(tab1, text="Tab 1")

        Notebooks.scale_var = tk.DoubleVar(value=75.0)
         # Scale
        scale = ttk.Scale(
            tab1,
            from_=100,
            to=0,
            length=175,
            variable=Notebooks.scale_var,
            command=lambda event: Notebooks.scale_var.set(scale.get()),
        )
        scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 20))

         # Progressbar
        progress = ttk.Progressbar(
            tab1, value=0, variable=Notebooks.scale_var, mode="determinate", length=175
        )
        progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 20))

        # Theme
        label = ttk.Label(
            tab1,
            text="Azure theme for ttk",
            justify="center",
            font=("-size", 15, "-weight", "bold"),
        )
        label.grid(row=1, column=0, pady=(20, 50), columnspan=2)

        # Tab 2
        tab2 = ttk.Frame(notebook)
        for i in [0, 1]:
            tab2.columnconfigure(i, weight=1)
            tab2.rowconfigure(i, weight=1)
        notebook.add(tab2, text="Tab 2")

         # Tab 2
        tab3 = ttk.Frame(notebook)
        for i in [0, 1]:
            tab3.columnconfigure(i, weight=1)
            tab3.rowconfigure(i, weight=1)
        notebook.add(tab3, text="Tab 3") 
 



       


    
        

class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('1000x1000')
        self.resizable(0,0)
        self.title('BT')
        self.create_widgets()
        self.call("source", "azure.tcl")
        self.call("set_theme", "dark")
        # self.style = ttk.Style(self)
    
    def create_widgets(self):
        #Create Frame
        Frame1 = ttk.LabelFrame(self, text="Check Button")
        Frame1.grid(row=0, column=0, padx=(20, 20), pady=(10,10), sticky=NW)

        S = ttk.Separator(self, orient='horizontal')
        S.grid(row=1,column=0, padx=(10,10), pady=(20,10), sticky=EW)

        Frame2 = ttk.LabelFrame(self, text="Radio Button")
        Frame2.grid(row=2, column=0, padx=(20, 20), pady=(10,10), sticky=NW)

        Frame3 = ttk.Frame(self)
        Frame3.grid(row=0, column=1, rowspan=3, padx=(20, 20), pady=(10,10), sticky=NW)

        Frame4 = ttk.Frame(self)
        Frame4.grid(row=0, column=2, rowspan=3, padx=(20,20), pady=(18,20), sticky=NW)

        Frame5 = ttk.Frame(self)
        Frame5.grid(row=1, column=2, rowspan=2, padx=(20,20), pady=20, sticky=NW)

        #Create Widgets
        F1 = CheckButton(Frame1)
      
        F2 = RadioButton(Frame2)

        F3 = ButtonFrame2(Frame3)

        F4 = Treev(Frame4)

        F5 = Notebooks(Frame5)
   
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
        









        

        