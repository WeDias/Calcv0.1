#!/usr/bin/env python
# -*- coding: utf-8 -*-

# calculadora.pyw     
# Github:@WeDias

# MIT License

# Copyright (c) 2019-2020 Wesley Ribeiro Dias

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tkinter import *


# Função dos botões numericos para mostrar no painel e fazer a conta
def bt_def_num(num):
    if painel.get() == '0':
        painel.delete(first=0)
        painel.insert(len(painel.get()), num)
        if len(memoria['text']) == 1:
            memoria['text'] = f'{num}'
        else:
            memoria['text'] += f'{num}'
    else:
        painel.insert(len(painel.get()), num)
        memoria['text'] += f'{num}'


# Função dos botões operadores para mostrar no painel e fazer a conta
def bt_def_op(simb, nome):
    global op, num1
    if op is None:
        op = nome
        num1 = painel.get()
        painel.delete(first=0, last=len(painel.get()))
        memoria['text'] += simb


def bt0():
    bt_def_num(0)


def bt1():
    bt_def_num(1)


def bt2():
    bt_def_num(2)


def bt3():
    bt_def_num(3)


def bt4():
    bt_def_num(4)


def bt5():
    bt_def_num(5)


def bt6():
    bt_def_num(6)


def bt7():
    bt_def_num(7)


def bt8():
    bt_def_num(8)


def bt9():
    bt_def_num(9)


def btmais():
    bt_def_op('+', 'soma')


def btmenos():
    bt_def_op('-', 'sub')


def btdiv():
    bt_def_op('/', 'div')


def btmult():
    bt_def_op('*', 'mult')


def btexp():
    bt_def_op('^', 'exp')


def btres():
    global num1, resultado, op
    num1 = float(num1)
    num2 = float(painel.get())
    if op == 'soma':
        resultado = num1 + num2
        if resultado == 0:
            resultado = int(resultado)
    elif op == 'sub':
        resultado = num1 - num2
        if resultado == 0:
            resultado = int(resultado)
    elif op == 'div':
        resultado = num1 / num2
        if resultado == 0:
            resultado = int(resultado)
    elif op == 'mult':
        resultado = num1 * num2
        if resultado == 0:
            resultado = int(resultado)
    elif op == 'exp':
        resultado = num1 ** num2
        if resultado == 0:
            resultado = int(resultado)
    painel.delete(first=0, last=len(painel.get()))
    painel.insert(0, resultado)
    memoria['text'] = str(resultado)
    op = None
    resultado = 0


def btdec():
    valores_digitados = str(tuple(painel.get()))
    if valores_digitados.find('.') < 0:
        painel.insert(len(valores_digitados), '.')
        memoria['text'] += '.'
        if len(painel.get()) == 0:
            painel.insert(len(valores_digitados), '0')
            painel.insert(len(valores_digitados), '.')
            memoria['text'] += '0.'


def btdel():
    global op
    numeros = len(painel.get())
    if numeros > 0 and float(painel.get()) != 0:
        painel.delete(first=numeros-1, last=numeros)
        memoria['text'] = memoria['text'][:len(memoria['text'])-1]
        if len(painel.get()) == 0:
            painel.insert(0, 0)
            if op is None:
                memoria['text'] = '0'


def btdelall():
    global op
    numeros = len(painel.get())
    painel.delete(first=0, last=numeros)
    painel.insert(0, 0)
    memoria['text'] = '0'
    op = None


# Configuração da tela de informações
def btinfo():
    top = Toplevel()
    top.geometry('200x65')
    top.title('?')
    top.wm_iconbitmap('calculator.ico')
    top.resizable(False, False)
    Label(top, text='Calculadora Básica', justify='center').place(x=25, y=0)
    Label(top, text='Por: Wesley Dias', justify='center').place(x=25, y=20)
    Label(top, text='Github: WeDias', justify='center').place(x=25, y=40)
    top.grab_set()


# Configura o estilo dos (Botões numericos e Botões operadores) e seus comandos
def btconfignum(text, command, width):
    bt = Button(calculadora, width=width, text=f'{text}', font=('arial', 20), command=command, relief='groove', activebackground='gray')
    return bt


# Configura o estilo dos (Outros botões) e seus comandos
def btconfigout(text, command, width, font_size):
    bt = Button(calculadora, width=width, text=f'{text}', font=('arial', font_size), command=command, relief='groove', activebackground='gray')
    return bt


# variaveis
num1 = resultado = 0
op = None

# Janela principal
calculadora = Tk()
calculadora.wm_iconbitmap('calculator.ico')
calculadora.geometry('343x390')
calculadora.resizable(False, False)
calculadora.title('Calculadora V0.1')

# Painel da calculadora
painel = Entry(calculadora, width=20, font=('Agency FB', 30), fg='black', bg='#e2e2e2', justify='right', bd=3)
painel.place(x=8, y=0)
painel.insert(0, 0)
memoria = Label(calculadora, text='0', font=('Agency FB', 15))
memoria.place(x=8, y=58)

# Botões numericos
bt0 = btconfignum('0', bt0, 7)
bt0.place(x=0, y=280)
bt1 = btconfignum('1', bt1, 5)
bt1.place(x=0, y=224)
bt2 = btconfignum('2', bt2, 5)
bt2.place(x=90, y=224)
bt3 = btconfignum('3', bt3, 5)
bt3.place(x=180, y=224)
bt4 = btconfignum('4', bt4, 5)
bt4.place(x=0, y=169)
bt5 = btconfignum('5', bt5, 5)
bt5.place(x=90, y=169)
bt6 = btconfignum('6', bt6, 5)
bt6.place(x=180, y=169)
bt7 = btconfignum('7', bt7, 5)
bt7.place(x=0, y=115)
bt8 = btconfignum('8', bt8, 5)
bt8.place(x=90, y=115)
bt9 = btconfignum('9', bt9, 5)
bt9.place(x=180, y=115)

# Botões Operadores
btres = btconfignum('=', btres, 16)
btres.place(x=0, y=337)
btmais = btconfignum('+', btmais, 4)
btmais.place(x=195, y=280)
btmenos = btconfignum('-', btmenos, 4)
btmenos.place(x=270, y=280)
btmult = btconfignum('*', btmult, 4)
btmult.place(x=270, y=225)
btdiv = btconfignum('/', btdiv, 4)
btdiv.place(x=270, y=169)
btexp = btconfignum('^', btexp, 4)
btexp.place(x=270, y=115)

# Outros Botões
btdel = btconfigout('C', btdel, 9, 12)
btdel.place(x=179, y=83)
btdelall = btconfigout('Del', btdelall, 8, 12)
btdelall.place(x=270, y=83)
btdec = btconfigout('.', btdec, 4, 20)
btdec.place(x=120, y=280)
btinfo = btconfigout('?', btinfo, 5, 20)
btinfo.place(x=267, y=337)
calculadora.mainloop()
