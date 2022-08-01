from tkinter import *
from tkinter import ttk , Tk
from tkinter import messagebox

import mysql.connector



class DashBoard(Tk) :

    def __init__(self):
        Tk.__init__(self)

        self.title("MENU PRINCIPAL")
        self.geometry("1350x700+0+0")
        self.resizable(False,False)
        self.configure(background="#091821")


        lbltitre = Label(self,bd=3,relief=SUNKEN,text="GESTION DES NOTES DES ETUDIANTS", font =("Sans Serif",25),bg="#2f4f4f",fg="#FFFAFA")
        lbltitre.place(x=0 , y =0 , width = 1350 ,height =150)

        lblnom = Label(self,text='NOM', font=("Arial",18),bg='#091821',fg="white")
        lblnom.place(x=70,y=200,width=150)
        self.txtnom = Entry(self,bd=4 , font=('Arial',14))
        self.txtnom.place(x=250,y=200,width=300)

        lblprenom = Label(self, text = 'PRENOM', font = ('Arial',18) , bg ='#091821',fg='white')
        lblprenom.place(x=70 , y=250 , width =150 )
        self.txtprenom = Entry(self,bd=4 , font = ('Arial',14))
        self.txtprenom.place (x=250 , y=250 , width =300)

        self.valeurSexe = StringVar()
        lblsexe = Label(self,text='SEXE',font=('Arial',14),bg='#091821',fg='white')
        lblsexe.place(x=100,y=300)
        lblSexeMasculin = Radiobutton(self,text='MASCULIN',value='M',variable=self.valeurSexe,indicatoron=0,font=('Arial',14),bg='#091821',fg='#696969')
        lblSexeMasculin.place(x=250,y=300,width=130)

        lblSexeFeminin = Radiobutton(self,text='FEMININ',value='F',variable=self.valeurSexe , indicatoron =0 , font =('Arial',14),bg='#091821',fg='#696969')
        lblSexeFeminin.place(x=420,y=300,width=130)

        lblClasse = Label(self,text='NIVEAU',font=('Arial',18),bg='#091821',fg='white')
        lblClasse.place(x=70,y=350,width=150)

        self.comboClasse = ttk.Combobox(self,font=('Arial',14))
        self.comboClasse['values'] = ['I','II','III','IV','V']
        self.comboClasse.place(x=250,y=350,width=130)

        lblmatiere = Label(self,text='MATIERE',font=('Arial',18),bg='#091821',fg='white')
        lblmatiere.place(x=70,y=400,width=150)
        self.comboMatiere = ttk.Combobox(self,font=('Arial',14))
        self.comboMatiere['values'] =['INFORMATIQUE','ROBOTIQUE','ALGEBRE','MECANIQUE','ELECTRONIQUE','ANALYSE']
        self.comboMatiere.place(x=250,y=400,width=150)

        lblnote = Label(self,text='NOTE',font=('Arial',18),bg='#091821',fg='white')
        lblnote.place(x=70,y=450,width=150)
        self.comboNote = ttk.Combobox(self,font=('Arial',14))
        self.comboNote['values'] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        self.comboNote.place(x=250,y=450,width=200)

        btnenregistrer = Button(self,text="Enregistrer",font=('Arial',16),bg="#02691E",fg='white',command=self.Ajouter)
        btnenregistrer.place(x=250,y=500,width=200)

        btnmodifier = Button(self,text='Modifier',font=('Arial',16),bg="#02691E",fg='white',command=self.Modifier)
        btnmodifier.place(x=250,y=550,width=200)

        btnSupprimer = Button(self,text='Supprimer',font=('Arial',16),bg='#02691E',fg='white',command=self.Supprimer)

        btnSupprimer.place(x=250 , y=600 , width=200)


        self.table = ttk.Treeview(self,columns =(1,2,3,4,5,6,7),height=5 , show = "headings",selectmode="extended")
        self.table.place(x=560 , y=150 , width =790 , height =450)
        vscrl = ttk.Scrollbar(self,orient=VERTICAL,command=self.table.yview)
        vscrl.place(x=1335,y=150,height=450)

        self.table.configure(yscrollcommand=vscrl.set)
        self.table.heading(1,text='MAT')
        self.table.heading(2,text='NOM')
        self.table.heading(3,text='PRENOM')
        self.table.heading(4,text='SEXE')
        self.table.heading(5,text='CLASSE')
        self.table.heading(6,text='MATIERE')
        self.table.heading(7,text='NOTE')

        self.table.column(1,width=50)
        self.table.column(2,width=150)
        self.table.column(3,width=150)
        self.table.column(4,width=100)
        self.table.column(5,width=50)
        self.table.column(6,width=100)
        self.table.column(7,width=50)

        self.maBase = mysql.connector.connect(host='localhost', user='root', password='ay08m0a1', database='note_eleve')
        self.conn = self.maBase.cursor()
        self.conn.execute("SELECT * FROM Note")
        for row in self.conn:
             self.table.insert("", END, value=row)
        self.maBase.close()


    def Ajouter(self):

            nom = self.txtnom.get()
            prenom = self.txtprenom.get()
            sexe = self.valeurSexe.get()
            classe = self.comboClasse.get()
            matiere = self.comboMatiere.get()
            note = self.comboNote.get()

            self.maBase = mysql.connector.connect(host='localhost', user='root', password='ay08m0a1', database='note_eleve')
            self.conn = self.maBase.cursor()

            try:
                sql = 'INSERT INTO note (nom , prenom ,sexe , classe , matiere , notes) VALUES ( %s , %s ,%s ,%s , %s , %s)'
                val = (nom, prenom, sexe, classe, matiere, note)
                self.conn.execute(sql, val)
                self.maBase.commit()
                messagebox.showinfo('INFORMATION', 'NOTE AJOUTEE')
                for i in self.table.get_children():
                    self.table.delete(i)
                self.conn.execute("SELECT * FROM Note")
                for row in self.conn:
                    self.table.insert("", END, value=row)

            except Exception as e:
                print(e)
                messagebox.showinfo("ERREUR", "NOTE NON AJOUTEE")
                self.maBase.rollback()
                self.maBase.close()

    def Modifier(self):
            code = (tuple(self.table.item(self.table.selection())["values"])[0])
            dico = {'nom': self.txtnom.get(), 'prenom': self.txtprenom.get(), 'sexe': self.valeurSexe.get(),
                    'classe': self.comboClasse.get(), 'matiere': self.comboMatiere.get(), 'notes': self.comboNote.get()}

            self.maBase = mysql.connector.connect(host='localhost', user='root', password='ay08m0a1', database='note_eleve')
            self.conn = self.maBase.cursor()

            try:
                for champ, valeur in dico.items():
                    if valeur != "":
                        sql = ("update note set {0} = %s where code = %s".format(champ))
                        val = (valeur, code)
                        self.conn.execute(sql, val)

                self.maBase.commit()
                messagebox.showinfo('INFORMATION', 'NOTE MODIFIEE')

                for i in self.table.get_children():
                    self.table.delete(i)
                self.conn.execute("SELECT * FROM Note")

                for row in self.conn:
                    self.table.insert("", END, value=row)

            except Exception as e:
                print(e)
                messagebox.showinfo("ERREUR", "INFORMATIONS NON MODIFIEES")
                self.maBase.rollback()
                self.maBase.close()

    def Supprimer(self):
            balise = 0
            for item in self.table.selection():
                values = (tuple(self.table.item(item)["values"])[0],)
                selected_item = item
                self.maBase = mysql.connector.connect(user='root', password='ay08m0a1', database='note_eleve',
                                                 host='localhost')
                self.conn = self.maBase.cursor()

                try:
                    self.conn.execute("DELETE FROM NOTE WHERE code= %s", values)
                    self.maBase.commit()
                    self.table.delete(selected_item)
                    balise = balise + 1
                except:
                    self.maBase.rollback()
                    self.maBase.close()
            if balise > 0:
                messagebox.showinfo('INFORMATION', 'NOTE SUPPRIMEE(S)')


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
                DashBoard().mainloop()

            else:
                messagebox.showwarning("", "Erreur de Connexion")
                self.txtmdp.delete(0, END)
                self.txtnomUtilisateur.delete(0, END)
Connexion().mainloop()