from tkinter import *
from tkinter import ttk , Tk
from tkinter import messagebox
import mysql.connector


def Ajouter() :

    nom = txtnom.get()
    prenom = txtprenom.get()
    sexe = valeurSexe.get()
    classe = comboClasse.get()
    matiere = txtmatiere.get()
    note = txtnote.get()

    maBase = mysql.connector.connect(host='localhost',user='root',password='ay08m0a1',database='note_eleve')
    conn = maBase.cursor()

    try :
        sql = 'INSERT INTO note (nom , prenom ,sexe , classe , matiere , notes) VALUES ( %s , %s ,%s ,%s , %s , %s)'
        val = ( nom , prenom , sexe , classe , matiere , note)
        conn.execute(sql,val)
        maBase.commit()
        messagebox.showinfo('INFORMATION','NOTE AJOUTEE')
        for i in table.get_children() :
            table.delete(i)
        conn.execute("SELECT * FROM Note")
        for row in conn:
            table.insert("", END, value=row)

    except Exception as e :
        print(e)
        messagebox.showinfo("ERREUR","NOTE NON AJOUTEE")
        maBase.rollback()
        maBase.close()

def Modifier() :
    code = (tuple(table.item(table.selection())["values"])[0])
    dico = {'nom':txtnom.get(),'prenom':txtprenom.get(),'sexe':valeurSexe.get(),'classe':comboClasse.get(),'matiere':txtmatiere.get(),'notes':txtnote.get()}

    maBase = mysql.connector.connect(host='localhost', user='root', password='ay08m0a1', database='note_eleve')
    conn = maBase.cursor()

    try :
        for champ , valeur in dico.items() :
            if valeur != "" :
               sql =( "update note set {0} = %s where code = %s".format(champ))
               val = (valeur,code)
               conn.execute(sql,val)

        maBase.commit()
        messagebox.showinfo('INFORMATION','NOTE MODIFIEE')

        for i in table.get_children() :
            table.delete(i)
        conn.execute("SELECT * FROM Note")
        for row in conn:
            table.insert("", END, value=row)
    except Exception as e :
        print(e)
        messagebox.showinfo("ERREUR","INFORMATIONS NON MODIFIEES")
        maBase.rollback()
        maBase.close()

def Supprimer() :
    balise = 0
    for item in table.selection() :
        values = (tuple(table.item(item)["values"])[0],)
        selected_item = item
        maBase = mysql.connector.connect(user='root',password='ay08m0a1',database='note_eleve',host='localhost')
        conn = maBase.cursor()
        try :
            conn.execute("DELETE FROM NOTE WHERE code= %s",values)
            maBase.commit()
            table.delete(selected_item)
            balise = balise +1
        except :
            maBase.rollback()
            maBase.close()
    if balise> 0 :
        messagebox.showinfo('INFORMATION', 'NOTE SUPPRIMEE(S)')

root =  Tk()

root.title("MENU PRINCIPAL")
root.geometry("1350x700+0+0")
root.resizable(False,False)
root.configure(background="#091821")

lbltitre = Label(root,bd=3,relief=SUNKEN,text="GESTION DES NOTES DES ETUDIANTS", font =("Sans Serif",25),bg="#2f4f4f",fg="#FFFAFA")
lbltitre.place(x=0 , y =0 , width = 1350 ,height =150)


lblnom = Label(root,text='NOM', font=("Arial",18),bg='#091821',fg="white")
lblnom.place(x=70,y=200,width=150)
txtnom= Entry(root,bd=4 , font=('Arial',14))
txtnom.place(x=250,y=200,width=300)

lblprenom = Label(root, text = 'PRENOM', font = ('Arial',18) , bg ='#091821',fg='white')
lblprenom.place(x=70 , y=250 , width =150 )
txtprenom = Entry(root,bd=4 , font = ('Arial',14))
txtprenom.place (x=250 , y=250 , width =300)

valeurSexe = StringVar()
lblsexe = Label(root,text='SEXE',font=('Arial',14),bg='#091821',fg='white')
lblsexe.place(x=100,y=300)

lblSexeMasculin = Radiobutton(root,text='MASCULIN',value='M',variable=valeurSexe,indicatoron=0,font=('Arial',14),bg='#091821',fg='#696969')
lblSexeMasculin.place(x=250,y=300,width=130)
txtSexeFeminin = Radiobutton(root,text='FEMININ',value='F',variable=valeurSexe , indicatoron =0 , font =('Arial',14),bg='#091821',fg='#696969')
txtSexeFeminin.place(x=420,y=300,width=130)

lblClasse = Label(root,text='NIVEAU',font=('Arial',18),bg='#091821',fg='white')
lblClasse.place(x=70,y=350,width=150)

comboClasse = ttk.Combobox(root,font=('Arial',14))
comboClasse['values'] = ['I','II','III','IV','V']
comboClasse.place(x=250,y=350,width=130)

lblmatiere = Label(root,text='MATIERE',font=('Arial',18),bg='#091821',fg='white')
lblmatiere.place(x=70,y=400,width=150)
txtmatiere = Entry(root,bd=4,font=('Arial',14))
txtmatiere.place(x=250,y=400,width=300)

lblnote = Label(root,text='NOTE',font=('Arial',18),bg='#091821',fg='white')
lblnote.place(x=70,y=450,width=150)
txtnote = Entry(root,bd=4,font=('Arial',14))
txtnote.place(x=250,y=450,width=200)

btnenregistrer = Button(root,text="Enregistrer",font=('Arial',16),bg="#02691E",fg='white',command=Ajouter)
btnenregistrer.place(x=250,y=500,width=200)

btnmodifier = Button(root,text='Modifier',font=('Arial',16),bg="#02691E",fg='white',command=Modifier)
btnmodifier.place(x=250,y=550,width=200)

btnSupprimer = Button(root,text='Supprimer',font=('Arial',16),bg='#02691E',fg='white',command=Supprimer)

btnSupprimer.place(x=250 , y=600 , width=200)


table = ttk.Treeview(root,columns =(1,2,3,4,5,6,7),height=5 , show = "headings",selectmode="extended")
table.place(x=560 , y=150 , width =790 , height =450)
vscrl = ttk.Scrollbar(root,orient=VERTICAL,command=table.yview)
vscrl.place(x=1335,y=150,height=450)
table.configure(yscrollcommand=vscrl.set)
table.heading(1,text='MAT')
table.heading(2,text='NOM')
table.heading(3,text='PRENOM')
table.heading(4,text='SEXE')
table.heading(5,text='CLASSE')
table.heading(6,text='MATIERE')
table.heading(7,text='NOTE')

table.column(1,width=50)
table.column(2,width=150)
table.column(3,width=150)
table.column(4,width=100)
table.column(5,width=50)
table.column(6,width=100)
table.column(7,width=50)

maBase = mysql.connector.connect(host='localhost',user='root',password='ay08m0a1',database='note_eleve')
conn = maBase.cursor()
conn.execute("SELECT * FROM Note")
for row in conn :
      table.insert("",END,value=row)

maBase.close()

root.mainloop()
