from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os
import validators




root = Tk()
root.geometry("370x150+200+200")
root.resizable(False, False)
root.title("YouTubeToMp3")
img = PhotoImage(file='youtube.gif')
root.tk.call('wm', 'iconphoto', root._w, img)



label = Label(root, text='Cole a URL no campo abaixo: ')
label.place(x=10, y=10)

field = Entry(root)
field.place(x=10, y=28, width=350)

def YouTubeToMp3():
	valid = validators.url(field.get())
	if field.get() == "":
		messagebox.showinfo("YouTubeToMp3", "Insira uma URL.")
	elif valid == False:
		messagebox.showinfo("YouTubeToMp3", "Insira uma URL válida.")
	else:	
		path = os.path.join('YouTubeToMp3')
		url = field.get()
		yt = YouTube(url)
		audio = yt.streams.filter(only_audio=True).first()
		out_file = audio.download(path)

		base, ext = os.path.splitext(out_file)
		new_file = base + '.mp3'
		os.rename(out_file, new_file)

		field.delete(0, END)
		messagebox.showinfo("YouTubeToMp3", "Download realizado com Sucesso.")

	

btn = Button(root, text='Baixar', width=30, command=YouTubeToMp3)
btn.place(x=53, y=65)

root.mainloop()
