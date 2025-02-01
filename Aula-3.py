from tkinter import *

root = Tk()
root.title("Colors")

azul='#00caff'
vermelho='#c77373'
amarelo='#e2d934'
verde='#59974c'

root.geometry('500x600')
root.wm_resizable(width=False, height=False)
root.configure(bg=azul)

def fundo1():
    root.configure(background=azul)
    lt1.configure(text='Azul', background=azul)

def fundo2():
    root.configure(background=vermelho)
    lt1.configure(text='Vermelho', background=vermelho)

def fundo3():
    root.configure(background=amarelo)

def fundo4():
    root.configure(background=verde)


lt1 = Label(root, text='Escolha', font='Arial 14 bold', background=azul)
lt1.place(width=200, height=100, x=150, y=400)

bt1 = Button(root, text='Azul', font='Arial 14 bold', command=fundo1)
bt1.place(width=200, height=160, x=40, y=20)

bt2 = Button(root, text='Vermelho', font='Arial 14 bold', command=fundo2)
bt2.place(width=200, height=160, x=260, y=20)

bt3 = Button(root, text='Amarelo', font='Arial 14 bold', command=fundo3)
bt3.place(width=200, height=160, x=40, y=200)

bt4 = Button(root, text='Verde', font='Arial 14 bold', command=fundo4)
bt4.place(width=200, height=160, x=260, y=200)


root.mainloop()