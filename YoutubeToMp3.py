from tkinter import *
from tkinter import messagebox, filedialog
import os
import threading
import yt_dlp

# Variável para armazenar a pasta de destino
output_path = ""

def select_folder():
    global output_path
    output_path = filedialog.askdirectory(title="Escolha a pasta de destino")
    if output_path:
        folder_label.config(text=f"Pasta: {output_path}", fg="green")
    else:
        folder_label.config(text="Nenhuma pasta selecionada", fg="red")

def YouTubeToMp3():
    url = field.get().strip()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    if not output_path:
        messagebox.showerror("Erro", "Selecione uma pasta para salvar o arquivo.")
        return

    btn.config(state=DISABLED)
    status_label.config(text="Baixando...", fg="blue")

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        field.delete(0, END)
        status_label.config(text="Download concluído!", fg="green")
        messagebox.showinfo("Sucesso", "Download finalizado!")

    except Exception as e:
        status_label.config(text="Erro no download", fg="red")
        messagebox.showerror("Erro", f"Falha no download: {e}")

    finally:
        btn.config(state=NORMAL)

# Criar janela
root = Tk()
root.geometry("450x250")
root.resizable(False, False)
root.title("YouTube to MP3 Downloader")

Label(root, text='URL do Vídeo:', font=("Arial", 10)).place(x=10, y=10)

field = Entry(root, width=55)
field.place(x=10, y=35)

folder_btn = Button(root, text="Selecionar Pasta", command=select_folder)
folder_btn.place(x=10, y=65)

folder_label = Label(root, text="Nenhuma pasta selecionada", fg="red", font=("Arial", 9))
folder_label.place(x=120, y=68)

status_label = Label(root, text="", fg="black", font=("Arial", 10))
status_label.place(x=10, y=160)

btn = Button(root, text='Baixar MP3', width=40, command=lambda: threading.Thread(target=YouTubeToMp3).start())
btn.place(x=85, y=130)

root.mainloop()
