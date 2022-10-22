# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main

'''
rect1 = shape_calculator.Rectangle(10, 20)  # 長方形1(幅:10 高さ:20)
rect2 = shape_calculator.Rectangle(10, 10)  # 長方形2(幅:10 高さ:10)
print(rect1.get_amount_inside(rect2))       # 長方形1内に包含可能な長方形2の数
square1 = shape_calculator.Square(20)       # 正方形1(幅:20 高さ:20)
square2 = shape_calculator.Square(10)       # 正方形2(幅:10 高さ:10)
print(square1.get_amount_inside(square2))   # 正方形1内に包含可能な正方形2の数
'''

''' __str__
rect = shape_calculator.Rectangle(5, 3)
print(rect)
'''

''' get_amount_inside
rect1 = shape_calculator.Rectangle(10, 20)
rect2 = shape_calculator.Rectangle(5, 5)
print(rect1.get_amount_inside(rect2))
'''

''' get_picture
rect = shape_calculator.Rectangle(5, 3)
print(rect.get_picture())
'''

''' Original Code
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
'''

# Run unit tests automatically
main(module='test_module', exit=False)