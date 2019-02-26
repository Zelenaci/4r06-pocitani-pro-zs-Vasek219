#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:57:33 2019
@author: lov35174
"""

import tkinter as tk
from tkinter import Label,Radiobutton, IntVar, Entry, LabelFrame, Message, StringVar
from random import randint
from tkinter import messagebox

class Application(tk.Tk):
    name = 'ZS'
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth = 5)
        
        ######OPERACE
        self.lbloper=Label(self, text=u"Operace:", font='Arial 18')
        self.lbloper.pack(anchor='w')
        
        ######RADIOBUTTONS
        
        self.v = StringVar()
        self.v.set('+')
        
        self.intvys = StringVar()
        self.intvys.set('')

        self.inta = IntVar()
        self.inta.set('')
        
        self.intb = IntVar()
        self.intb.set('')
        
        self.intuzi = StringVar()
        self.intuzi.set('')
        
        self.intspr = IntVar()
        self.intspr.set(0)
        
        self.intspa = IntVar()
        self.intspa.set(0)
        
        self.rdbplus = Radiobutton(self, text = u'+', variable=self.v, value='+' , font='Arial 20', command=self.plus)
        self.rdbplus.pack(anchor='w')
        
        self.rdbminus = Radiobutton(self, text = u'-', variable=self.v, value='-', font='Arial 20', command=self.minus)
        self.rdbminus.pack(anchor='w')
        
        self.rdbkrat = Radiobutton(self, text = u'*', variable=self.v, value='*' , font='Arial 20', command=self.krat)
        self.rdbkrat.pack(anchor='w')
        
        self.rdbdeleno = Radiobutton(self, text = u'/', variable=self.v, value='/' , font='Arial 20', command=self.deleno)
        self.rdbdeleno.pack(anchor='w')
        
        self.rdbplus.invoke()
        
        ######Entry
        
        self.lblfr = LabelFrame(self, text='Příklad')
        self.lblfr.pack(anchor='w')
                
        self.entcisloa = Entry(self.lblfr,state='readonly', text=None, width=5, font='Arial 20', textvariable=self.inta)
        self.entcisloa.grid(row=1, column=1)
        
        self.znammess = Message(self.lblfr, font='Arial 20', textvariable=self.v)
        self.znammess.grid(row=1, column=2)
                
        self.entcislob = Entry(self.lblfr,state='readonly', text=None, width=5, font='Arial 20', textvariable=self.intb)
        self.entcislob.grid(row=1, column=3)
        
        self.rovmess = Message(self.lblfr, text=u'=', font='Arial 20')
        self.rovmess.grid(row=1, column=4)
                
        self.entcislob = Entry(self.lblfr,state='readonly', text=None, width=5, font='Arial 20', textvariable=self.intvys)
        self.entcislob.grid(row=1, column=5)
        
        self.prkButton = tk.Button(self, text='Nový příklad', command=self.priklad)
        self.prkButton.pack()
        
        self.vypButton = tk.Button(self, text='Výpočet', command=self.vypocet)
        self.vypButton.pack()
        
        self.entvys = Entry(self, text=None, width=5, font='Arial 20', textvariable=self.intuzi)
        self.entvys.pack()
        
        self.zkoButton = tk.Button(self, text='Zkontroluj výsledek', command=self.zkontroluj)
        self.zkoButton.pack()
        
        self.pormess = Message(self, text='', font='Arial 15')
        self.pormess.pack()
        
        self.lblfrstat = LabelFrame(self, text='Statistika', padx=30)
        self.lblfrstat.pack()
        
        self.sprmess = Message(self.lblfrstat, text='Správně:', font='Arial 18',pady=25)
        self.sprmess.grid(row=1,column=1)
        
        self.entvys = Entry(self.lblfrstat, text=None, width=3, font='Arial 20', textvariable=self.intspr, fg='white', bg='green')
        self.entvys.grid(row=1,column=2)
        
        self.spamess = Message(self.lblfrstat, text='Špatně:', font='Arial 18',pady=25)
        self.spamess.grid(row=1, column=3)
        
        self.entvys = Entry(self.lblfrstat, text=None, width=3, font='Arial 20', textvariable=self.intspa, fg='white', bg='red')
        self.entvys.grid(row=1,column=4)
        
        
        
        #####ESC
        self.bind("<Escape>", self.quit)
        self.bind("<Return>", self.zkontroluj)
        self.bind("<KP_Enter>", self.zkontroluj)
        
    def plus(self):
        self.intvys.set('')
        self.x = randint(1,99)
        self.y = randint(0,100-self.x)
        self.vys = self.x + self.y
        self.inta.set(self.x)
        self.intb.set(self.y)
            
    def minus(self):
        self.intvys.set('')
        self.x = randint(1,99)
        self.y = randint(0,self.x)
        self.vys = self.x - self.y
        self.inta.set(self.x)
        self.intb.set(self.y)
        
    def krat(self):
        self.intvys.set('')
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.vys = self.x * self.y
        self.inta.set(self.x)
        self.intb.set(self.y)
        
    def deleno(self):
        self.intvys.set('')
        self.vys = randint(1,9)
        self.y = randint(1,9)
        self.x = self.vys * self.y
        self.inta.set(self.x)
        self.intb.set(self.y)

    def vypocet(self):
        self.intvys.set(self.vys)
        
    def priklad(self):
        priklad = self.v.get()
        if priklad == "+":
            self.rdbplus.invoke()
        if priklad == "-":
            self.rdbminus.invoke()
        if priklad == "*":
            self.rdbkrat.invoke()
        if priklad == "/":
            self.rdbdeleno.invoke()
    
    def zkontroluj(self,event=None):
        self.intvys.set(self.vys)
        vys = self.intvys.get()
        uzivatel = self.intuzi.get()
        self.intuzi.set('')
        if vys == uzivatel:
            self.pormess.configure(text='Správný výsledek')
            spravne = self.intspr.get()
            spravne = spravne + 1
            self.intspr.set(spravne)
            self.prkButton.invoke()
        else:
            self.pormess.configure(text='Špatný výsledek')
            spatne = self.intspa.get()
            spatne = spatne + 1
            self.intspa.set(spatne)
            self.prkButton.invoke()

    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
