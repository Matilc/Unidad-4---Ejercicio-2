import tkinter as tk
from tkinter import messagebox
class Aplicacion():
    def __init__(self):
        self.__ventana=tk.Tk()
        self.__precio=tk.StringVar()
        self.__IVA=tk.IntVar()
        self.__IVAporc=tk.StringVar()
        self.__precioIVA=tk.StringVar()
        self.__ventana.title('Calculadora de IVA')
        opts = { 'ipadx': 10, 'ipady': 10 , 'sticky': 'nswe' }
        self.__ventana.config()
        label_a=tk.Label(self.__ventana,text= "Cálculo de IVA", bg='light steel blue')
        label_a.grid(column=0,row=0,columnspan=6,ipady=12,ipadx=15,sticky="nswe")
        label_b=tk.Label(self.__ventana,text="Precio sin IVA")
        label_b.grid(row=1, column=0,columnspan=2,padx=20)
        entryprec=tk.Entry(self.__ventana,width=18,relief=tk.SOLID,textvariable=self.__precio,bd=1)
        entryprec.grid(row=1,column=3,columnspan=2,ipady=5,ipadx=5,pady=20,padx=20,sticky="ns")
        radioiva1=tk.Radiobutton(self.__ventana,text='IVA 21%', variable=self.__IVA,value=1)
        radioiva1.grid(row=2,column=0, ipadx= 10, padx=30, sticky= 'nsw')
        radioiva2=tk.Radiobutton(self.__ventana,text='IVA 10.5%', variable=self.__IVA,value=2)
        radioiva2.grid(row=3,column=0, ipadx= 10, padx=30, sticky= 'nsw')
        label_c=tk.Label(self.__ventana,text="IVA")
        label_c.grid(row=4, column=0,columnspan=2,**opts)
        labeliva=tk.Label(self.__ventana,width=15,relief=tk.SOLID,textvariable=self.__IVAporc,background="white",bd=1)
        labeliva.grid(row=4,column=3,columnspan=2,ipady=5,ipadx=5,pady=15,padx=20,sticky="ns")
        label_d=tk.Label(self.__ventana,text="Precio con IVA")
        label_d.grid(row=5, column=0,columnspan=2,**opts)
        labelpreiva=tk.Label(self.__ventana,width=15,relief=tk.SOLID,textvariable=self.__precioIVA,background="white",bd=1)
        labelpreiva.grid(row=5,column=3,columnspan=2,ipady=5,ipadx=5,padx=20)
        calcularbutton=tk.Button(self.__ventana,text="Calcular",command=self.calculariva,bg='PaleGreen1',relief=tk.SOLID,highlightbackground="black",highlightthickness=2)
        calcularbutton.grid(row=6,column=0,ipadx=15,ipady=5,padx=40,columnspan=2,pady=20)
        salirbutton=tk.Button(self.__ventana,text="Salir",command=self.__ventana.destroy,relief=tk.RIDGE,bg='pink1',highlightcolor='brown1',bd=2)
        salirbutton.grid(row=6,column=4,columnspan=4,padx=20,ipadx=35,ipady=5)
        self.__ventana.mainloop()
    
    def calculariva(self):
        try:
            precio=float(self.__precio.get())
            if self.__IVA.get()==1:
                self.__IVAporc.set('21%')
                iva=0.21
                precioiva=precio*iva+precio
                self.__precioIVA.set(precioiva)
            elif self.__IVA.get()==2:
                self.__IVAporc.set('10.5%')
                iva=0.105
                precioiva=precio*iva+precio
                self.__precioIVA.set(precioiva)
        except ValueError:
            messagebox.showerror(title='Error de valor', message='Debe ingresar valores numéricos en el precio')