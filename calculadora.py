
# importar tudo da biblioteca tkinter
from tkinter import *         
from tkinter import ttk

# mudar cores
cor1 = '#000000'    #preto
cor2= '#FFFFFF'     #branco
cor3= '#084B99'     #azul escuro
cor4= '#8F8F8F'     #cinza
cor5= '#D4520D'     #laranja



# criar uma janela
janela= Tk()
janela.title('calculadora')
janela.geometry('235x310')
janela.configure(bg=cor1)

# dividindo a janela
Frame_tela= Frame(janela, width=235, height=50, bg=cor3)      # <---- width= comprimento/  height= altura
Frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)   # row= animação de cima para baixo
frame_corpo.grid(row=1, column=0)


#variavel
todos_valores=''


valor_texto= StringVar()  # variavel para aparecer o resultado na tela 



# resultado=variavel/ def= função                     #### etapa final depois de terminar os botões

# função para aparecer num. na tela
def entrar_valores(event):

    global todos_valores                      #variavel global= toda alteração que fizer na variavel será somado com o anterior

    todos_valores= todos_valores + str(event)
    

   

    # passar o valor para a tela
    valor_texto.set(todos_valores) 

#função para calcular
def calcular():
    global todos_valores
    resultado= eval(todos_valores)
   
    valor_texto.set(str(resultado))


# função deletar
def deletar():
    global todos_valores
    todos_valores= ''
    valor_texto.set('')



# criar label       # anchor/justify= deixar o numero mais a direita                         # bg= cor de fundo   fg= cor da letra

                                                               
app_label = Label(Frame_tela, textvariable= valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)     #bold= negrito              # padx= tamanho da exibição dentro do frame     realief= estilo da label     FLAT= estilo liso
app_label.place(x=0, y=0)







# criar botões
b_1= Button(frame_corpo, command=deletar, text='C', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    # raised= puxar o botão p/ frente    #overrelief= animação de passar o mouse por cima do botão                                                
b_1.place(x=0, y=0)          # x= horizontal   y= vertical
b_2= Button(frame_corpo, command=lambda:entrar_valores('%'), text='%', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_2.place(x=118, y=0)                     
b_3= Button(frame_corpo, command=lambda:entrar_valores('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_3.place(x=175, y=0) 

b_4= Button(frame_corpo, command=lambda:entrar_valores('7'), text='7', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_4.place(x=0, y=52)                     
b_5= Button(frame_corpo, command=lambda:entrar_valores('8'), text='8', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_5.place(x=59, y=52) 
b_6= Button(frame_corpo, command=lambda:entrar_valores('9'), text='9', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_6.place(x=118, y=52) 
b_7= Button(frame_corpo, command=lambda:entrar_valores('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_7.place(x=175, y=52) 

b_8= Button(frame_corpo, command=lambda:entrar_valores('4'), text='4', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_8.place(x=0, y=104)                     
b_9= Button(frame_corpo, command=lambda:entrar_valores('5'), text='5', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_9.place(x=59, y=104) 
b_10= Button(frame_corpo, command=lambda:entrar_valores('6'), text='6', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_10.place(x=118, y=104) 
b_11= Button(frame_corpo, command=lambda:entrar_valores('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_11.place(x=175, y=104) 

b_12= Button(frame_corpo, command=lambda:entrar_valores('1'), text='1', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_12.place(x=0, y=156)                     
b_13= Button(frame_corpo, command=lambda:entrar_valores('2'), text='2', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_13.place(x=59, y=156) 
b_14= Button(frame_corpo, command=lambda:entrar_valores('3'), text='3', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_14.place(x=118, y=156) 
b_15= Button(frame_corpo, command=lambda:entrar_valores('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_15.place(x=175, y=156) 

b_16= Button(frame_corpo, command=lambda:entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    # raised= puxar o botão p/ frente    #overrelief= animação de passar o mouse por cima do botão                                                
b_16.place(x=0, y=208)          # x= horizontal   y= vertical
b_17= Button(frame_corpo, command=lambda:entrar_valores('.'), text='.', width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_17.place(x=118, y=208)                     
b_18= Button(frame_corpo, command= calcular, text='=', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)    
b_18.place(x=175, y=208) 







janela.mainloop()


