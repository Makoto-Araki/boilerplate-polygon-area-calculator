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
        //
#class Square:
