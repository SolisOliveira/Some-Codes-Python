from tkinter import *
from tkinter import messagebox
from pytube import YouTube
import os

root = Tk()
root.geometry("400x200+200+200")
root.resizable(False, False)
root.title("YouTubeToMp3")

label = Label(root, text='URL:')
label.place(x=10, y=10)

field = Entry(root)
field.place(x=10, y=28, width=350)

def YouTubeToMp3():
	url = field.get()
	yt = YouTube(url)
	video = yt.streams.filter(only_audio=True).first()
	out_file = video.download()
	base, ext = os.path.splitext(out_file)
	new_file = base + ".mp3"
	os.rename(out_file, new_file)

	field.delete(0, END)
	messagebox.showinfo("YouTubeToMp3", "Download realizado com Sucesso.")

	

btn = Button(root, text='Baixar', width=30, command=YouTubeToMp3)
btn.place(x=53, y=65)

root.mainloop()

