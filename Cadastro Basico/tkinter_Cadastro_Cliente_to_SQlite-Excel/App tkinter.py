import tkinter as tk
from tkinter import  messagebox
import sqlite3 
import panda as pd
from tkinter import *



conexao = sqlite3.connect('cadastro_CLientes.db')
c = conexao.cursor()
c. execute(''' CREATE TABLE cliente (
    nome text,
    sobrenome text,
    email,
    telefone,
    )
  ''')

conexao.commit()

conexao.close()


  def validar(entradas):
     for entrada in entradas.keys():
        if not(entradas[entrada]):
            messagebox.showerror(
                'erro', f'Preencha corretamente o campo {entrada}!')

                return False
                return True

def cadastrar_cliente():
conexao =sqlite3.connect('cadastro_clientes.db')

c= conexao.cursor()
    from = {
    'nome': entry_nome.get(),
    'sobrenome': entry_sobrenome.get(),
    'email':entry_email,get(),
    'telefone': entry_telefone.get()
    }

if validar(form):
    c.execute(
        "INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)", form)

conexao.commit()
    
conexao.close()

entry_nome.delete(0, 'end')
entry_sobrenome.delete(0, 'end')
entry_email.delete(0, 'end')
entry_telefone.delete(0, 'end')

def exporta_clientes():
    conexao = sqlite3.connect('cadastro_clientes.db')

    c = conexao.cursor()

    c.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.dataframe(clientes_cadastrados, columns=[
                                        'nome', 'sobrenome', 'email', 'telefone', 'id_banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
conexao.commit()

conexao.close()


janela = tk.tk()
janela.title('cadastro de clientes')
janela.iconbitmap('cadastro_db_icon.ico')
janela['bg'] = '#d9d9d9' 
janela.resizable(width=false, height=false)

label_nome = tk.Label(janela, text='nome:', font='times' , bg= '#d9d9d9')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='sobrenome:', font='times' , bg= '#d9d9d9')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail:', font='times' , bg= '#d9d9d9')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone:', font='times' , bg= '#d9d9d9')
label_telefone.grid(row=3, column=0, padx=10, pady=10)

entry_nome = tk.Entry(janela, Text='nome', width=29)
entry_nome.grid(row=0, column=1, padx=15, pady=10)


entry_sobrenome = tk.Entry(janela, Text='sobrenome', width=29)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, Text='E-mail', width=29)
entry_email.grid(row=2, column=1, padx=10, pady=10)


entry_telefone = tk.Entry(janela, Text='Telefone', width=29)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)


botao_cadastrar = tk.Button(
    janela, text='Cadastar Cliente', command=Cadastrar_Cliente, font='times')
botao_cadastrar.grid(row=4, column=0, padx=10, pady=10, columnspan=2, ipadx=80)


botao_exportar = tk.Button(
    janela, text='Exportar para Excell', command=exporta_clientes, font='times')
botao_exportar.grid(row=5, column=0, padx=10, pady=10, columnspan=2, ipadx=80)

largura = 320 
altura = 290 

largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenwidth()

posx = largura_screen/2 - largura/1.8
posy = altura_screen/5 - altura/5


janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

janela.mainloop()


    
