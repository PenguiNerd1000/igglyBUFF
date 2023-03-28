class Piece: 
    def __init__(self, position, promotion, value, representation): 
        self.position = position
        self.promotion = promotion
        self.value = value
        self.representation = representation
        
    def moveVector(posx1, posy1, posx2, posy2):
        conversionLibLetter = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
}
        conversionLibNumber = {
        1: 8,
        2: 7,
        3: 6,
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 1
}
        y = conversionLibNumber[posy2] - conversionLibNumber[posy1]
        x = conversionLibLetter[posx2] - conversionLibNumber[posx1]
        vector = [x,y]
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
