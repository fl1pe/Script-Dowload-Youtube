from pytube import YouTube, Playlist
from pytube.cli import on_progress
from time import sleep
import cor
import os


class Download:
    def __init__(self, url):
        self.url = url

    def musica(self):
        musica = YouTube(self.url, on_progress_callback=on_progress)
        print(f'Pesquisando...\n')
        print(f'Título:{cor.red}+{musica.title}+{cor.reset}')
        sleep(0.5)
        stream = musica.streams.get_by_itag(139).download(output_path='Downloads/Música')
        # Renomear o arquivo
        nome_arquivo, extensao = os.path.splitext(stream)
        novo_nome = nome_arquivo + '.mp3'
        os.rename(stream, novo_nome)
        # Arquivo renomeado
        print(cor.red+ f'\nDOWNLOAD FINALIZADO!' +cor.reset)

    def video(self):
        video = YouTube(self.url, on_progress_callback=on_progress)
        print(f'Pesquisando...\n')
        stream = video.streams.get_by_itag(22).download(output_path='Downloads/Video')
        print(f'Título: {video.title}')
        sleep(0.5)
        print(cor.red+ f'\nDOWNLOAD FINALIZADO!' +cor.reset)


    def playlist_musica(self):
        playlist = Playlist(self.url)
        print(f'PESQUISANDO...')
        for i in playlist.video_urls:
            sleep(0.5)
            musica = YouTube(i, on_progress_callback=on_progress)
            print(f'\nTítulo: {musica.title}')
            stream = musica.streams.get_by_itag(139).download(output_path='Downloads/Música')
            nome_arquivo, extensao = os.path.splitext(stream)
            novo_nome = nome_arquivo + '.mp3'
            os.rename(stream, novo_nome)
        print(cor.red+ f'\nDOWNLOAD FINALIZADO!' +cor.reset)


    def playlist_video(self):
        playlist = Playlist(self.url)
        for i in playlist.video_urls:
            video = YouTube(i, on_progress_callback=on_progress)
            stream = video.streams.get_by_itag(22).download(output_path='Downloads/Video')
            print(f'\nTÍTULO: {video.title}')
            sleep(0.5)
        print(cor.red+ f'\nDOWNLOAD FINALIZADO!' +cor.reset)


    def playlist_ambos(self):
        playlist = Playlist(self.url)
        for i in playlist.video_urls:
            yt = YouTube(i, on_progress_callback=on_progress)
            print(f'\nTÍTULO: {yt.title}')
            stream = yt.streams.get_by_itag(139).download(output_path='Downloads/Música')
            nome_arquivo, extensao = os.path.splitext(stream)
            novo_nome = nome_arquivo + '.mp3'
            os.rename(stream, novo_nome)
            
            for j in playlist.video_urls:
                #yt = YouTube(i, on_progress_callback=on_progress)
                stream = yt.streams.get_by_itag(22).download(output_path='Downloads/Video')
        print(cor.red+ f'\nDOWNLOAD FINALIZADO!' +cor.reset)
