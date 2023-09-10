import tkinter as tk
from tkinter import *
import os
import tkinter.messagebox as messagebox
# 创建窗口：实例化一个窗口对象。

class MyApp(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text="静态网站配置")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="启动",command=self.Open)
        self.quitButton.pack()
        self.quitButton = Button(self,text="端口",command=self.Port)
        self.quitButton.pack()
    def Open(self):
        os.system("start server.exe")
    def Port(self):
        window = tk.Tk()
        window.geometry("350x350")
        t = tk.Text(window,height=4)
        t.pack()
        e = tk.Entry(window)
        e.pack()
        
        mytxtfile ="./port.ini"
        def in_f_txt():
            if os.path.exists(mytxtfile):
                a = open(mytxtfile, 'r', encoding='utf-8')
                for id_names in a:
                    t.insert('insert', id_names)
                a.close()
            
 
        c = tk.Button(window, text="查看当前端口", command=in_f_txt)
        c.pack()
        def add():
            var_id = e.get()
            h = open(mytxtfile, 'w+', encoding='utf-8')
            h.write(var_id + '\n') #添加到文件夹中的txt
            h.close()
 
        b2 = tk.Button(window, text="写入端口", command=add)
        b2.pack()
        

        



# 创建窗口：实例化一个窗口对象。
root = Tk()
 
# 窗口大小
root.geometry("600x450")


myapp = MyApp()
myapp.master.title('py快速静态网页启动器')
myapp.mainloop()