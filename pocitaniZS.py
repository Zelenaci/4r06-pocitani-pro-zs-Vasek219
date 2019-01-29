#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:57:33 2019

@author: lov35174
"""

import tkinter as tk
from tkinter import Label,Radiobutton, IntVar, Entry, LabelFrame
from random import randint

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
        
        self.v = IntVar()
        self.v.set(1)
        
        self.rdbplus = Radiobutton(self, text = u'+', variable=self.v, value=1 , font='Arial 18', command=self.plus)
        self.rdbplus.pack(anchor='w')
        
        self.rdbminus = Radiobutton(self, text = u'-', variable=self.v, value=2, font='Arial 18', command=None)
        self.rdbminus.pack(anchor='w')
        
        self.rdbkrat = Radiobutton(self, text = u'*', variable=self.v, value=3 , font='Arial 18', command=None)
        self.rdbkrat.pack(anchor='w')
        
        self.rdbdeleno = Radiobutton(self, text = u'/', variable=self.v, value=4 , font='Arial 18', command=None)
        self.rdbdeleno.pack(anchor='w')
        
        
        
        ######Entry
        
        self.lblfr = LabelFrame(self, text='Příklad')
        self.lblfr.pack(anchor='w')
        
        self.entcisloa = Entry(self.lblfr,state='readonly', text=None, width=5)
        self.entcisloa.grid(row=1, column=1)
        
        self.entznam = Entry(self.lblfr,state='readonly', text=None, width=5)
        self.entznam.grid(row=1, column=2)
        
        self.entcislob = Entry(self.lblfr,state='readonly', text=None, width=5)
        self.entcislob.grid(row=1, column=3)
        
        
        self.prkButton = tk.Button(self, text='Priklad', command=self.priklad)
        self.prkButton.pack()
        
        self.vypButton = tk.Button(self, text='Výpočet', command=self.vypocet)
        self.vypButton.pack()
        
        #####ESC
        self.bind("<Escape>", self.quit)
        
    def plus(self):
        self.x = randint(1,99)
        self.y = randint(0,100-self.x)
        self.vys = self.x + self.y
        self.entznam.insert
        self.entznam.insert(tk.END,'+')
            
    def minus(self):
        self.x = randint(1,99)
        self.y = randint(0,self.x)
        self.vys = self.x - self.y
        
    def krat(self):
        self.x = randint(1,9)
        self.y = randint(1,9)
        self.vys = self.x * self.y
        
    def deleno(self):
        self.vys = randint(1,9)
        self.y = randint(1,9)
        self.x = self.vys * self.y

    def vypocet(self):
        operace = (self.plus, self.minus, self.krat, self.deleno)
        nahoda = randint(0,3)
        funkce = operace[nahoda]
        funkce()
        print(self.x,funkce.__name__ ,self.y,'=', self.vys)
    
    def priklad(self):
        self.entcisloa.get(self.x)
    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()


