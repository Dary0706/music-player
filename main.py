from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pygame
import time
import os
import shutil

pygame.mixer.init()

global musics
musics = list()

def song(song_name, r):
    playing = False
    song_name = song_name


    def pp():
        nonlocal playing
        nonlocal song_name
        playing = not playing

        pygame.mixer.music.load(f"audio\{song_name}")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()

        if playing:
            btn['text'] = "⏸"
            pygame.mixer.music.unpause()
        else:
            btn['text'] = "▶"
            pygame.mixer.music.pause()


    btn = Button(content_frame,text="▶", width=3, height=1, font="Arial 27 bold", relief="groove", borderwidth=4, command=pp)
    label = Label(content_frame,text=f"{song_name[:-4]}", font="Arial 15 bold")

    label.grid(row=r, column=2, pady=15)
    btn.grid(row=r, column=1, padx=20, pady=15)

def load_song():
    file_path = filedialog.askopenfilename(title="Выберите трек", filetypes=(("Аудиофайлы", "*.mp3 *.wav *.ogg *.flac *.m4a"), ("Все файлы", "*.*")))
    file_name = os.path.basename(file_path)
    destination_path = os.path.join('audio', file_name)
    shutil.move(file_path, destination_path)

    musics.append(file_name)

    for r in range(len(musics)):
        song(musics[r], r + 1)

    print(file_name)
    print(destination_path)

def dir_files():
    all_files = os.listdir('audio')
    for file in all_files:
        musics.append(file)

    for r in range(len(musics)):
        mus = musics[r].split(" ")
        song(musics[r], r + 1)


root = Tk()
root.title("KukuMusic")

root.geometry("437x600")
root.resizable(False, False)
icon = PhotoImage(file = "nota.png")
root.iconphoto(False, icon)

canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
content_frame = Frame(canvas)
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=content_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

load_btn = Button(content_frame, text="load", width=15, relief="groove", borderwidth=4, height=2, command=load_song)
load_btn.grid(row=0, column=1, columnspan=2, pady=7)

dir_files()

root.mainloop()