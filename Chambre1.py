import tkinter
from cProfile import label
from subprocess import call
from tkinter import *
from tkinter import ttk , Tk
from tkinter import messagebox
import mysql.connector
def Seconnecter() :
    nom = txtnomUtilisateur.get()
    mdp = txtmdp.get()
    if (nom=="" or mdp=='') :
        messagebox.showerror("","Il faut rentrer les donées")
        txtmdp.delete(0,END)
        txtnomUtilisateur.delete(0,END)
    elif (nom=="admin" and mdp=="admin") :
        messagebox.showinfo("","Bienvenue")
        txtnomUtilisateur.delete(0,END)
        txtmdp.delete(0,END)
        root.destroy()
        call(["python", "Chambre2.py"])
    else :
        messagebox.showwarning("","Erreur de Connexion")
        txtmdp.delete(0,END)
        txtnomUtilisateur.delete(0,END)

root = Tk()

root.title("FENÊTRE DE CONNEXION")
root.geometry("400x300+450+200")
root.resizable(True,False)
root.configure(background="#091821")

lbltitre = Label(root,borderwidth =3 , relief = SUNKEN ,height=0 ,width=0,
                 text = "Formulaire de connexion" , font = ("Arial",25),bg ='#000000',fg ="white")
lbltitre.place(x =0 , y= 0 , width =400)
lblnomUtilisateur = Label(root,text='Nom Utilisateur :', font=('Arial',14),bg='#091821',fg='white')
lblnomUtilisateur.place(x=5 , y=100 , width =150)
txtnomUtilisateur = Entry(root,borderwidth=5,font=("Arial",13))
txtnomUtilisateur.place(x=150,y=100,width=200,height=30)

lblmdp = Label (root,text="Mot de Passe   :",font=('Arial',14),bg="#091821",fg="white")
lblmdp.place(x=-20,y=150,width=200,height=30)
txtmdp = Entry(root,show="*",bd=4 , font=("Arial",13))
txtmdp.place(x=150,y=150,width=200,height=30)

btnenregistrer = Button(root , text = "Connexion" , font=('Arial',16),bg="#FF4500",fg='white',command=Seconnecter)
btnenregistrer.place(x=150,y=200,width=200)


root.mainloop()