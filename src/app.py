import cor
import os
from download import Download


def cabecalho():
    print('Formato do arquivo:\n1-Mp4\n2-Mp3\n3-Ambos')
    print('=-' * 20)
    opcao_formato = int(input('Selecione uma opção: '))
    print('=-' * 20)
    if opcao_formato == 1:
        yt = Download(input('COLE O LINK AQUI: '))
        yt.video()
    elif opcao_formato == 2:
        yt = Download(input('COLE O LINK AQUI: '))
        yt.musica()

    else:
        yt = Download(input('COLE O LINK AQUI: '))
        yt.video()
        yt.musica()
        

if __name__ == '__main__':
    while True:
        print('=-' * 20)
        print('1-BAIXAR VIDEO\n2-BAIXAR DE UMA PLAYLIST')
        print('=-' * 20)
        pergunta = int(input('Seleciona uma opção: '))
        os.system('clear')
        
        if pergunta == 1:
           cabecalho()
                
        else:
            print('Formato do arquivo:\n1-Mp4\n2-Mp3\n3-Ambos')
            print('=-' * 20)
            opcao_formato = int(input('Selecione uma opção: '))
            if opcao_formato == 1:
                yt = Download(input('COLE O LINK AQUI: '))
                yt.playlist_video()
            elif opcao_formato == 2:
                yt = Download(input('COLE O LINK AQUI: '))
                yt.playlist_musica()

            else:
                yt = Download(input('COLE O LINK AQUI: '))
                yt.playlist_ambos()

        continuar =  input('\nDeseja sair? Digite q ou Enter para continuar.\n')
        if (continuar == 'q'):
            break