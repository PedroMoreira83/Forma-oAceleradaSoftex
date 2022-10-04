class InterfaceGalinha:
    print("Galinha não pode ser pato")
    def faz_cocorico(self):
        pass

class InterfacePato: #Adaptee
    def faz_quaqua(self, pato):
        print("Mas um pato pode ser galinha, pelo menos na lógica")
        pato.faz_quaqua()
        pass

class AdaptadorPato(InterfacePato): #Adapter
    def __init__(self, galinha):
        self.galinha = galinha

    def faz_quaqua(self):
        self.galinha.faz_cocorico()

def main():
    galinha = InterfaceGalinha()
    pato = InterfacePato()
    adaptador_pato = AdaptadorPato(galinha)
    pato.faz_quaqua(adaptador_pato)


if __name__ == "__main__":
    main()
