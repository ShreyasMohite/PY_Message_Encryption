from tkinter import *
import onetimepad

class Message_Encrypt:
    def __init__(self,root):
        self.root=root
        self.root.title("Message Encryption")
        self.root.geometry("400x475")
        self.root.iconbitmap("logo535.ico")
        self.root.resizable(0,0)


        def on_enter1(e):
            but_encrypt['background']="black"
            but_encrypt['foreground']="cyan"
  
        def on_leave1(e):
            but_encrypt['background']="SystemButtonFace"
            but_encrypt['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        
        def clear():
            text_encrypt.delete('1.0',"end")
            text_encrypt_output.delete('1.0',"end")


        def encrypt():
            x=onetimepad.encrypt(text_encrypt.get('1.0','end'),'random')
            text_encrypt_output.insert('end',x)




#===========frame==================================#

        mainframe=Frame(self.root,width=400,height=475,relief="ridge",bd=4)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=393,height=207,relief="ridge",bd=4)
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=393,height=207,relief="ridge",bd=4)
        secondframe.place(x=0,y=207)

        thirdframe=Frame(mainframe,width=393,height=52,relief="ridge",bd=4,bg="gray77")
        thirdframe.place(x=0,y=415)

#===================firstframe==============================#
        
        scol=Scrollbar(firstframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text_encrypt=Text(firstframe,height=10,width=45,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text_encrypt.place(x=0,y=0)
        scol.config(command=text_encrypt.yview)

#====================secondframe============================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text_encrypt_output=Text(secondframe,height=10,width=45,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text_encrypt_output.place(x=0,y=0)
        scol.config(command=text_encrypt_output.yview)

#==================third====================================#

        but_encrypt=Button(thirdframe,text="Encrypt",width=13,font=('times new roman',14),cursor="hand2",command=encrypt)
        but_encrypt.place(x=20,y=3)
        but_encrypt.bind("<Enter>",on_enter1)
        but_encrypt.bind("<Leave>",on_leave1)

        but_clear=Button(thirdframe,text="Clear",width=13,font=('times new roman',14),cursor="hand2",command=clear)
        but_clear.place(x=235,y=3)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


if __name__ == "__main__":
    root=Tk()
    Message_Encrypt(root)
    root.mainloop()
