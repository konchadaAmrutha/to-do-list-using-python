from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root=root
        self.root.title('To-Do-List-App')
        self.root.geometry('650x410+300+150')
        self.label1=Label(self.root , text='To-Do-List',
                                     font='Times 25 bold italic',
                                     width=10,
                                     bd=5,
                                     bg='green',
                                     fg='white')
        self.label1.pack(side='top', fill=BOTH)

        self.label2=Label(self.root , text='Add-Task',
                                     font='Times 18 bold italic',
                                     width=10,
                                     bd=5,
                                     bg='green',
                                     fg='white')
        self.label2.place(x=40,y=55)

        self.label3=Label(self.root , text='Tasks',
                                     font='Times 18 bold italic',
                                     width=10,
                                     bd=5,
                                     bg='green',
                                     fg='white')
        self.label3.place(x=320,y=55)

        self.main_text = Listbox(self.root, height=9 ,
                         font='Arial 20 italic bold',
                         width=23,
                         bd=5,
                         fg='black')
        self.main_text.place(x=280, y=100)

        self.search_box = Text(self.root, height=2 ,
                         font='Arial 10 bold',
                         width=30,
                         bd=5,
                         fg='black')
        self.search_box.place(x=20, y=100)

#----------------------------------------add task-----------------------------------------------------
        def add():
            content=self.search_box.get(1.0, END)
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.search_box.delete(1.0, END)
#---------------------------------------delete task---------------------------------------------------
         
        def delete():
            del_ = self.main_text.curselection()
            if not del_:
                return

    # Delete the selected item from the file
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for index, line in enumerate(new_f):
                    if index not in del_:
                        f.write(line)
                f.truncate()

    # Delete the selected item from the main_text widget
            for index in reversed(del_):  # Delete in reverse to avoid shifting indices
                self.main_text.delete(index)
    
    #------------------------------------------------task done---------------------------------------------
        
        def mark_done():
            task_index = self.main_text.curselection()
            if task_index:
                self.main_text.itemconfig(task_index, {'fg': 'green'})
                save_tasks()


        
        

                    
#-----------------------------------------------------------------------------------------------------
        with open('data.txt', 'r') as file:
            read=file.readlines()
            for i in read:
                ready=i.split()
                self.main_text.insert(END,ready)
            file.close()
        

        self.button1=Button(self.root , text='Add',
                                     font='Times 20 bold italic',
                                     width=10,
                                     bd=5,
                                     bg='green',
                                     fg='white',
                                     command=add)
        self.button1.place(x=30, y=150)


        self.button2=Button(self.root , text='Remove',
                                     font='Times 20 bold italic',
                                     width=10,
                                     bd=5,
                                     bg='green',
                                     fg='white',
                                     command=delete)
        self.button2.place(x=30, y=230)

        self.button3 = Button(self.root, text='Mark Task',
                              font='Times 20 bold italic',
                              width=12,
                              bd=5,
                              bg='green',
                              fg='white',
                              command=mark_done)
        self.button3.place(x=30, y=310)







def main():
    root=Tk()
    ui=todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
