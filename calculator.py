from tkinter import *

root = Tk()
root.title('calculator')
root.geometry('320x380')
root.resizable(0,0)
root.configure(background = 'black')

result_label= Label(root,text=0,bg='black',fg ='white')
result_label.grid(row=0,column=0,pady=(50,25))
result_label.config(font=('verdana',30,'bold'))

btn7 =Button(root,text ='7',bg = '#00a65a',fg='white',width=5,height=2)
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8 =Button(root,text ='8',bg = '#00a65a',fg='white',width=5,height=2)
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9 =Button(root,text ='9',bg = '#00a65a',fg='white',width=5,height=2)
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_add =Button(root,text ='+',bg = '#00a65a',fg='white',width=5,height=2)
btn_add .grid(row=1,column=3)
btn_add .config(font=('verdana',14))

root.mainloop()
