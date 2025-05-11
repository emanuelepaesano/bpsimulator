class Partita:
    def __init__(self, numero_giocatori):
        self.numero = numero_giocatori
        self.giocatori = []
        self.punti = [0] * numero_giocatori
        self.turno = 0
        
