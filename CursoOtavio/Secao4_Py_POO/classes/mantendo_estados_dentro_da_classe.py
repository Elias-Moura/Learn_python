# coding=utf8
# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = False

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando.')
            return

        print(f'{self.nome} está filmando')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return

        self.filmando = False
        print(f'{self.nome} parou de filmar.')


    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando.')
            return

        print(f'{self.nome} está fotografando...')



c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()
c1


