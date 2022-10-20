class Rectangle:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
class Square:
