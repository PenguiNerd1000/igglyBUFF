class Piece: 
    def __init__(self, position, promotion, value, representation): 
        self.position = position
        self.promotion = promotion
        self.value = value
        self.representation = representation
        
    def moveInterpretation(pos1, pos2):
        pass
        
class King(Piece): 
    promotion = False
    
    def move(pos1, pos2):
        pass
        

class Queen(Piece):
    pass

class Rook(Piece):
    pass

class Bishop(Piece):
    pass

class Knight(Piece):
    pass

class Pawn(Piece):
    pass
