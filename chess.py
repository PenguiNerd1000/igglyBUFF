class Piece: 
    def __init__(self, position, promotion, value, representation): 
        self.position = position
        self.promotion = promotion
        self.value = value
        self.representation = representation
        
    def moveVector(pos1, pos2, pos3, pos4):
        conversionLib = {
        1: "a"
        2: "b"
        3: "c"
        4: "d"
        5: "e"
        6: "f"
        7: "g"
        8: "h"
}
        vector = []
        return vector
        
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
