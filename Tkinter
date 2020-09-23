from tkinter import *
from tkinter import ttk, StringVar
import sqlite3
import tkinter.messagebox
import re



root = Tk()
root.geometry("700x620+200+200")
root.resizable(FALSE, FALSE)
root.configure(bg="#333333")
root.title("Controle de Tranportadoras")

#============= Conexão com o Banco ==============================#
conn = sqlite3.connect('portaria.db')
cursor = conn.cursor()

# Variables
transp = StringVar()
moto = StringVar()
cnh = StringVar()
nf = StringVar()
placa = StringVar()
data = StringVar()
buscar = StringVar()

#============= Funções ===========================================#
def salvar():
    transp = entTrasnp.get().upper()
    nf = entNf.get().upper()
    moto = entMoto.get().upper()
    cnh = entCnh.get().upper()
    placa = entPlaca.get().upper()
    data = entData.get().upper()

    conn = sqlite3.connect('portaria.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO cadastro (transp,nf,moto,cnh,placa,data) VALUES (?,?,?,?,?,?)'
                   , (transp, nf, moto, cnh, placa, data))

    if transp != "" and nf != "" and moto != "" and cnh != "" and placa != "" and data != "":
        tkinter.messagebox.showinfo("Controle de Transp.", "Registro Salvo com Sucesso.")

    else:
        conn.close()
        tkinter.messagebox.showwarning("Controle de Transp.", "Preencha os campos.")

    conn.commit()
    display()
    conn.close()

    entTrasnp.delete(0, END)
    entMoto.delete(0, END)
    entCnh.delete(0, END)
    entNf.delete(0, END)
    entPlaca.delete(0, END)
    entData.delete(0, END)



def display():
    conn = sqlite3.connect('portaria.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM cadastro')
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert('', 0, value=row)

    conn.commit()
    conn.close()


def selecionado(event):
    sel = tree.focus()
    contents = tree.item(sel)
    row = contents['values']
    transp.set(row[0])
    nf.set(row[1])
    moto.set(row[2])
    cnh.set(row[3])
    placa.set(row[4])
    data.set(row[5])


def update():
    transp = entTrasnp.get().upper()
    nf = entNf.get().upper()
    moto = entMoto.get().upper()
    cnh = entCnh.get().upper()
    placa = entPlaca.get().upper()
    data = entData.get().upper()

    conn = sqlite3.connect('portaria.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE cadastro SET transp=?, nf=?, moto=?, placa=?, data=? WHERE cnh=?'
                   , (transp, nf, moto, placa, data, cnh))

    if transp != "" and nf != "" and moto != "" and cnh != "" and placa != "" and data != "":
        tkinter.messagebox.showinfo("Controle de Transp.", "Registro Atualizado com Sucesso.")

    else:
        conn.close()
        tkinter.messagebox.showwarning("Controle de Transp.", "Selecione um registro.")

    conn.commit()
    display()
    conn.close()

    entTrasnp.delete(0, END)
    entMoto.delete(0, END)
    entCnh.delete(0, END)
    entNf.delete(0, END)
    entPlaca.delete(0, END)
    entData.delete(0, END)


def delete():
    transp = entTrasnp.get().upper()
    nf = entNf.get().upper()
    moto = entMoto.get().upper()
    cnh = entCnh.get().upper()
    placa = entPlaca.get().upper()
    data = entData.get().upper()

    conn = sqlite3.connect('portaria.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cadastro WHERE cnh=?", (cnh,))

    if transp != "" and nf != "" and moto != "" and cnh != "" and placa != "" and data != "":
        tkinter.messagebox.askyesno("Controle de Transp.", "Quer mesmo deletar registro?.")
    else:
        conn.close()
        tkinter.messagebox.showwarning("Controle de Transp.", "Selecione um registro.")

    conn.commit()
    display()
    conn.close()


def pesquisar():
    buscar = entBuscar.get().upper()

    conn = sqlite3.connect('portaria.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cadastro WHERE "+str(combo.get())+" LIKE '%"+str(buscar)+"%'")
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert('', 0, value=row)

    conn.commit()
    conn.close()

#================== Frames ============================================#
frameTop = Frame(root, width="685", height="250", bg="#00847b")
frameTop.place(x=10, y=10)

frameBottom = Frame(root, width="680", height="350", bg="#00847b")
frameBottom.place(x=10, y=265)

#================= Labels and Entries =================================#
txtTrasnp = Label(frameTop, text="Transportadora :", font=("Arial", 10), bg='#00847b')
txtTrasnp.place(x=10, y=10)
entTrasnp = Entry(frameTop, textvar=transp, width=35)
entTrasnp.focus_set()
entTrasnp.place(x=10, y=30)

txtNf = Label(frameTop, text="Nota Fiscal :", font=("Arial", 10), bg='#00847b')
txtNf.place(x=310, y=10)
entNf = Entry(frameTop, textvar=nf, width=35)
entNf.place(x=310, y=30)

txtMoto = Label(frameTop, text="Motorista:", font=("Arial", 10), bg='#00847b')
txtMoto.place(x=10, y=55)
entMoto = Entry(frameTop, textvar=moto, width=35)
entMoto.place(x=10, y=73)

txtCnh = Label(frameTop, text="CNH:", font=("Arial", 10), bg='#00847b')
txtCnh.place(x=310, y=55)
entCnh = Entry(frameTop, textvar=cnh, width=35)
entCnh.place(x=310, y=73)

txtPlaca = Label(frameTop, text="Placa:", font=("Arial", 10), bg='#00847b')
txtPlaca.place(x=10, y=100)
entPlaca = Entry(frameTop, textvar=placa, width=35)
entPlaca.place(x=10, y=120)

txtData = Label(frameTop, text="Data:", font=("Arial", 10), bg='#00847b')
txtData.place(x=310, y=100)
entData = Entry(frameTop, textvar=data, width=20)
entData.place(x=310, y=120)

txtFiltrar = Label(frameTop, text="Filtrar por :", font=("Arial", 10), bg='#00847b')
txtFiltrar.place(x=10, y=150)
combo = ttk.Combobox(frameTop, values=["transp", "nf", "moto", "cnh", "placa", "data"])
combo.place(x=10, y=170)

txtBuscar = Label(frameTop, text="Pesquisar :", font=("Arial", 10), bg='#00847b')
txtBuscar.place(x=210, y=150)
entBuscar = Entry(frameTop, textvar=buscar, width=25)
entBuscar.place(x=210, y=170)

#================= Buttons ========================================#
btnPesq = Button(frameTop, text="Pesquisar", font=("Arial", 10, "bold"), width=17, command=pesquisar)
btnPesq.place(x=430, y=165)

btnSave = Button(frameTop, text="Cadastrar", font=("Arial", 10, "bold"), width=20, command=salvar)
btnSave.place(x=10, y=210)

btnEdit = Button(frameTop, text="Editar", font=("Arial", 10, "bold"), width=20, command=update)
btnEdit.place(x=210, y=210)

btnDel = Button(frameTop, text="Excluir", font=("Arial", 10, "bold"), width=20, command=delete)
btnDel.place(x=410, y=210)

#================ TreeView ==========================================#
tree = ttk.Treeview(frameBottom, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5", "column6"), height=16, show='headings')

tree.column("column1", width=135, minwidth=100, stretch=NO)
tree.heading("#1", text="Transp.")

tree.column("column2", width=100, minwidth=100, stretch=NO)
tree.heading("#2", text="NF")

tree.column("column3", width=135, minwidth=100, stretch=NO)
tree.heading("#3", text="Motorista")

tree.column("column4", width=100, minwidth=100, stretch=NO)
tree.heading("#4", text="CNH")

tree.column("column5", width=100, minwidth=100, stretch=NO)
tree.heading("#5", text="Placa")

tree.column("column6", width=100, minwidth=100, stretch=NO)
tree.heading("#6", text="Data")

tree.bind("<ButtonRelease-1>", selecionado)
tree.grid(row=0, column=0)

#=============== ScrollBar ===========================================#
scrl = ttk.Scrollbar(frameBottom, orient='vertical', command=tree.yview)
scrl.grid(row=0, column=1, sticky='ns')
tree.configure(yscroll=scrl.set)

display()

root.mainloop()
