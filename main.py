import musics

while True:
        print("""
                1 - Choram as Rosas
                2 - Pau no Gato
                3 - Brasilia Amarela
                4 - Hino Nacional
                5 - Nona Sinfonia
                7 - Asa Branca
                7 - Sair
        """)

        
        o = int(input('Digite o número da música: '))
        
        if o == 1:
                musics.choramAsRosas()
        elif o == 2:
                musics.pauNoGato()
        elif o == 3:
                musics.brasiliaAmarela()
        elif o == 4:
                musics.hinoNacional()
        elif o == 5:
                musics.nonaSinfonia()
        elif o == 6:
                musics.asaBranca()
        elif o == 7:
                break
        else:
                print('Opção inválida')

        print('Música finalizada')