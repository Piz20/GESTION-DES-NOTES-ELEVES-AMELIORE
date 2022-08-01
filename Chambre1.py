from subprocess import call
from tkinter import *
from tkinter import  Tk
from tkinter import messagebox


class Connexion(Tk) :

    def __init__(self):
        Tk.__init__(self)

        self.title("FENÊTRE DE CONNEXION")
        self.geometry("400x300+450+200")
        self.resizable(True,False)
        self.configure(background="#091821")

        lbltitre = Label(self,borderwidth =3 , relief = SUNKEN ,height=0 ,width=0,
                 text = "Formulaire de connexion" , font = ("Arial",25),bg ='#000000',fg ="white")
        lbltitre.place(x =0 , y= 0 , width =400)
        lblnomUtilisateur = Label(self,text='Nom Utilisateur :', font=('Arial',14),bg='#091821',fg='white')
        lblnomUtilisateur.place(x=5 , y=100 , width =150)
        self.txtnomUtilisateur = Entry(self,borderwidth=5,font=("Arial",13))
        self.txtnomUtilisateur.place(x=150,y=100,width=200,height=30)

        lblmdp = Label (self,text="Mot de Passe   :",font=('Arial',14),bg="#091821",fg="white")
        lblmdp.place(x=-20,y=150,width=200,height=30)
        self.txtmdp = Entry(self,show="*",bd=4 , font=("Arial",13))
        self.txtmdp.place(x=150,y=150,width=200,height=30)

        btnenregistrer = Button(self , text = "Connexion" , font=('Arial',16),bg="#FF4500",fg='white',command=self.Seconnecter)
        btnenregistrer.place(x=150,y=200,width=200)



    def Seconnecter(self):
            nom = self.txtnomUtilisateur.get()
            mdp = self.txtmdp.get()

            if (nom == "" or mdp == ''):
                messagebox.showerror("", "Il faut rentrer les donées")
                self.txtmdp.delete(0, END)
                self.txtnomUtilisateur.delete(0, END)

            elif (nom == "admin" and mdp == "admin"):
                messagebox.showinfo("", "Bienvenue")
                self.txtnomUtilisateur.delete(0, END)
                self.txtmdp.delete(0, END)
                self.destroy()
                call(["python", "Chambre2.py"])


            else:
                messagebox.showwarning("", "Erreur de Connexion")
                self.txtmdp.delete(0, END)
                self.txtnomUtilisateur.delete(0, END)
Connexion().mainloop()
