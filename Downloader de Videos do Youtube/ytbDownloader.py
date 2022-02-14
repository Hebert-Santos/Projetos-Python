from pytube import YouTube
import tkinter as tk
import ffmpeg
from pathlib import Path
import os

# TO DO - Resolver o problema da conversão dos arquivos para um só arquivo,
# usando o ffmpeg
#
# Comentar o código para futuras aprimorações
#

def consulta():
    urltext = url.get('1.0', 'end')

    if url.get('1.0', '1.5') == '':
        print('Erro de URL - Consulta')
        status.config(state='normal')
        status.delete('1.0', 'end')
        status.insert('1.0', 'Campo de URL Vazio - https')
        status.config(state='disabled')
        return 0

    else:
        yt = YouTube(urltext)

        title.config(state='normal')
        title.delete('1.0', 'end')
        title.insert('1.0', yt.title)
        title.config(state='disabled')

        thumb.config(state='normal')
        thumb.delete('1.0', 'end')
        thumb.insert('1.0', yt.thumbnail_url)
        thumb.config(state='disabled')

        author.config(state='normal')
        author.delete('1.0', 'end')
        author.insert('1.0', yt.author)
        author.config(state='disabled')

        summary.config(state='normal')
        summary.delete('1.0', 'end')
        summary.insert('1.0', yt.description)
        summary.config(state='disabled')

        key.config(state='normal')
        key.delete('1.0', 'end')
        key.insert('1.0', yt.keywords)
        key.config(state='disabled')

        # Segundos para minutos
        secs = int(yt.length) / 60
        time.config(state='normal')
        time.delete('1.0', 'end')
        time.insert('1.0', '             {:.2f} minutos'.format(round(secs, 2)))
        time.config(state='disabled')

        publish.config(state='normal')
        publish.delete('1.0', 'end')
        publish.insert('1.0', yt.publish_date)
        publish.config(state='disabled')

        rating.config(state='normal')
        rating.delete('1.0', 'end')
        rating.insert('1.0', yt.rating)
        rating.config(state='disabled')

        views.config(state='normal')
        views.delete('1.0', 'end')
        views.insert('1.0', f' {yt.views:,} visualizações')
        views.config(state='disabled')

        status.config(state='normal')
        status.delete('1.0', 'end')
        status.insert('1.0', 'Consulta realizada com sucesso')
        status.config(state='disabled')

def download():
    urltext = url.get('1.0', 'end')

    if url.get('1.0', '1.5') == '':
        print('Erro de URL - Download')
        status.config(state='normal')
        status.delete('1.0', 'end')
        status.insert('1.0', 'Campo de URL Vazio - https')
        status.config(state='disabled')
        return 0

    else:
        consulta()
        print(urltext)
        yt = YouTube(urltext)
        if resol.get('1.0', '1.4') == '720p':
            print('Resolução : 720p')
            yt.streams.filter(res='720p', progressive=True).first().download()
            print('Download realizado')
            status.config(state='normal')
            status.delete('1.0', 'end')
            status.insert('1.0', 'Download realizado com sucesso')
            status.config(state='disabled')
        elif resol.get('1.0', '1.4') == '480p':
            print('Resolução : 480p')
            yt.streams.filter(only_audio=True).first().download(filename=f'{yt.title}')
            yt.streams.filter(res='480p').first().download(filename=yt.title, filename_prefix='1')
            print("Donwload realizado")
            status.config(state='normal')
            status.delete('1.0', 'end')
            status.insert('1.0', 'Download realizado com sucesso')
            status.config(state='disabled')
        elif resol.get('1.0', '1.4') == '360p':
            print('Resolução : 360p')
            yt.streams.filter(res='360p', progressive=True).first().download()
            print('Download realizado')
            status.config(state='normal')
            status.delete('1.0', 'end')
            status.insert('1.0', 'Download realizado com sucesso')
            status.config(state='disabled')
        elif resol.get('1.0', '1.4') == '240p':
            print('Resolução : 240p')
            yt.streams.filter(res='240p', progressive=True).first().download()
            print('Download realizado')
            status.config(state='normal')
            status.delete('1.0', 'end')
            status.insert('1.0', 'Download realizado com sucesso')
            status.config(state='disabled')
        elif resol.get('1.0', '1.4') == '144p':
            print('Resolução : 144p')
            yt.streams.get_lowest_resolution().download()
            print('Download realizado')
            status.config(state='normal')
            status.delete('1.0', 'end')
            status.insert('1.0', 'Download realizado com sucesso')
            status.config(state='disabled')
        else:
            print('Erro de Resolução - Download')
            status.config(state='normal')
            status.delete('1.0', 'end')
            status.insert('1.0', 'Sem resolução ou resolução não suportada ')
            status.config(state='disabled')


def musica():
    urltext = url.get('1.0', 'end')

    if url.get('1.0', '1.5') == '':
        print('Erro de URL - Musica')
        status.config(state='normal')
        status.delete('1.0', 'end')
        status.insert('1.0', 'Campo de URL Vazio - https')
        status.config(state='disabled')
        return 0
    else:
        consulta()
        yt = YouTube(urltext)
        yt.streams.filter(only_audio=True).first().download()
        arquivo = Path(f'{yt.streams.filter(only_audio=True).first().default_filename}')
        arquivo.rename(arquivo.with_suffix('.mp3'))
        print("Download concluido - Música")

def abrir_explorer():
    os.system("explorer .")

root = tk.Tk()
root.title(' YouTube Video Downloader - by H1dr4')
root.geometry('800x750')

# URL
spaceLabel = tk.Label(root, text='')
spaceLabel.pack()
URLlabel = tk.Label(root, text='Insira a URL aqui')
URLlabel.pack()

url = tk.Text(root, height='1', width='90')
url.pack()

# Resolução
resLabel = tk.Label(root, text='Insira a resolução (MAX 720p)')
resLabel.pack()

resol = tk.Text(root, height='1', width='40')
resol.pack()

# Dados
spaceLabel = tk.Label(root, text='')
spaceLabel.pack()
infoLabel = tk.Label(root, text='|-------------------- Informações --------------------|')
infoLabel.pack()
spaceLabel = tk.Label(root, text='')
spaceLabel.pack()

titleLabel = tk.Label(root, text='Titulo')
titleLabel.pack()
title = tk.Text(root, height='1', width='90')
title.config(state='disabled', bg="#dddddd")
title.pack()

thumbLabel = tk.Label(root, text='Url da thumbnail')
thumbLabel.pack()
thumb = tk.Text(root, height='1', width='90')
thumb.config(state='disabled', bg="#dddddd")
thumb.pack()

authorLabel = tk.Label(root, text='Autor')
authorLabel.pack()
author = tk.Text(root, height='1', width='90')
author.config(state='disabled', bg="#dddddd")
author.pack()

summaryLabel = tk.Label(root, text='Descrição')
summaryLabel.pack()
summary = tk.Text(root, height='4', width='90')
summary.config(state='disabled', bg="#dddddd")
summary.pack()

keyLabel = tk.Label(root, text='Palavras-Chave')
keyLabel.pack()
key = tk.Text(root, height='4', width='90')
key.config(state='disabled', bg="#dddddd")
key.pack()

timeLabel = tk.Label(root, text='Duração (em minutos)')
timeLabel.pack(padx=(1, 400))
time = tk.Text(root, height='1', width='40')
time.config(state='disabled', bg="#dddddd")
time.pack(padx=(1, 400))

publishLabel = tk.Label(root, text='Data de publicação')
publishLabel.pack(padx=(1, 400))
publish = tk.Text(root, height='1', width='40')
publish.config(state='disabled', bg="#dddddd")
publish.pack(padx=(1, 400))

ratingLabel = tk.Label(root, text='Avaliação')
ratingLabel.pack(padx=(1, 400))
rating = tk.Text(root, height='1', width='40')
rating.config(state='disabled', bg="#dddddd")
rating.pack(padx=(1, 400))

viewsLabel = tk.Label(root, text='Visualizações')
viewsLabel.pack(padx=(1, 400))
views = tk.Text(root, height='1', width='40')
views.config(state='disabled', bg="#dddddd")
views.pack(padx=(1, 400))

statusLabel = tk.Label(root, text='Status')
statusLabel.pack(padx=(1, 400))
status = tk.Text(root, height='1', width='40')
status.config(state='disabled', bg="#dddddd")
status.pack(padx=(1, 400))

spaceLabel = tk.Label(root, text='')
spaceLabel.pack()

btn = tk.Button(root, text='Consultar video', command=consulta, width='15')
btn.place(relx=1, x=-300, y=550, anchor='s')

btex = tk.Button(root, text='Abrir arquivos', command=abrir_explorer, width='15')
btex.place(relx=1, x=-150, y=550, anchor='s')

btnd = tk.Button(root, text='Baixar video', command=download, width='15')
btnd.place(relx=1, x=-300, y=630, anchor='s')

btnm = tk.Button(root, text='Baixar como audio', command=musica, width='15')
btnm.place(relx=1, x=-150, y=630, anchor='s')

root.mainloop()

# video = input("Insira a url do video : ")
# yt = YouTube(video)

# print("O titulo desse video é {}".format(yt.title))

# tream = yt.streams.get_highest_resolution()

# print(stream)
