import turtle
import math 
turtle.shape("turtle")


walls_width = 200  # ширина стен
walls_height = 100  # высота стен
roof_height = 150  # высота крыши


roof_side = math.sqrt((walls_width / 2) ** 2 + roof_height ** 2)
print(roof_side)




for i in range(2):
	turtle.fd(walls_width)
	turtle.right(90)
	turtle.fd(walls_height)
	turtle.right(90)


