class Rectangle:
    
    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, w):
        self.width = w
    
    def set_height(self, h):
        self.height = h
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return self.width * 2 + self.height * 2
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        
        # Error Check
        if self.height > 50 or self.width > 50:
          return 'Too big for picture.'
        
        # Draw Rect
        return_str = ''
        for h in range(self.height):
            for w in range(self.width):
                return_str += '*'
            return_str += '\n'
        
        # Return Value
        return return_str
        
    def get_amount_inside(self, rect):
        
        # get_area()
        temp1 = self.get_area()
        temp2 = rect.get_area()
        
        # Return Value
        return temp1 // temp2
        
class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, w):
        self.width = w
        self.height = w
    
    def set_height(self, h):
        self.height = h
        self.height = h
    