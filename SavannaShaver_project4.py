import turtle
import random 

t = turtle.Turtle()
t.shape("turtle")
turtle.setup(width=600, height=600)
t.speed(0)
turtle.speed(0)
x = 0
c = 0

amount_circles = 0
amount_stars = 0
turtle.title("Interactive Drawing")
positions = [0,1,10,20,30,40,50,75,100,150,175,200,225,250,275,300,-10,-20,-30,-40,-50,-75,-100,-150,-175,-200,-225,-250,-275,-300]
positive = [100,150,175,200,225,250,275,300,]
values = [1,10,20,30,40,50]
small_set = [2,4,6,8,10,12]

print("""
       ___  ___  __        __  ___         ___     __   __                    __  
| |\ |  |  |__  |__)  /\  /  `  |  | \  / |__     |  \ |__)  /\  |  | | |\ | / _` 
| | \|  |  |___ |  \ /~~\ \__,  |  |  \/  |___    |__/ |  \ /~~\ |/\| | | \| \__>                                                                                                            

""")
print("By: Savanna Shaver")
print()

print("You will be asked questions to create a cool art piece")
print("Rules: Make sure to not use capitals or add a space when you are entering in a answer")
print()


while True:
    ready_test = input("Lets Begin! You ready? Answer yes or no")
    if ready_test == ("no"):
        print("Okay")
        exit()
    elif ready_test != ("yes"):
        print("Invalid input")
        continue
    else:
        
        break
    

turtle_color =input("What color should the turtle be? You can write in basic colors or write a hex code in EX: #0510FF")
t.color(turtle_color)
print()

myscreen = turtle.Screen()
background_color =input("What color should the background be? You can write in basic colors or write a hex code in EX: #0510FF")
myscreen.bgcolor(background_color)
print()

num =input("How many spirals do you want? More than 100 but less than 1000 please")

if int(num) > 1000 or int(num) <100:
    num = input("You gave a invalid input. How many spirals do you want? More than 100 but less than 1000 please")
print()

colors = [
(1.00, 0.00, 0.00),(1.00, 0.03, 0.00),(1.00, 0.05, 0.00),(1.00, 0.07, 0.00),(1.00, 0.10, 0.00),(1.00, 0.12, 0.00),(1.00, 0.15, 0.00),(1.00, 0.17, 0.00),(1.00, 0.20, 0.00),(1.00, 0.23, 0.00),(1.00, 0.25, 0.00),(1.00, 0.28, 0.00),(1.00, 0.30, 0.00),(1.00, 0.33, 0.00),(1.00, 0.35, 0.00),(1.00, 0.38, 0.00),(1.00, 0.40, 0.00),(1.00, 0.42, 0.00),(1.00, 0.45, 0.00),(1.00, 0.47, 0.00),
(1.00, 0.50, 0.00),(1.00, 0.53, 0.00),(1.00, 0.55, 0.00),(1.00, 0.57, 0.00),(1.00, 0.60, 0.00),(1.00, 0.62, 0.00),(1.00, 0.65, 0.00),(1.00, 0.68, 0.00),(1.00, 0.70, 0.00),(1.00, 0.72, 0.00),(1.00, 0.75, 0.00),(1.00, 0.78, 0.00),(1.00, 0.80, 0.00),(1.00, 0.82, 0.00),(1.00, 0.85, 0.00),(1.00, 0.88, 0.00),(1.00, 0.90, 0.00),(1.00, 0.93, 0.00),(1.00, 0.95, 0.00),(1.00, 0.97, 0.00),
(1.00, 1.00, 0.00),(0.95, 1.00, 0.00),(0.90, 1.00, 0.00),(0.85, 1.00, 0.00),(0.80, 1.00, 0.00),(0.75, 1.00, 0.00),(0.70, 1.00, 0.00),(0.65, 1.00, 0.00),(0.60, 1.00, 0.00),(0.55, 1.00, 0.00),(0.50, 1.00, 0.00),(0.45, 1.00, 0.00),(0.40, 1.00, 0.00),(0.35, 1.00, 0.00),(0.30, 1.00, 0.00),(0.25, 1.00, 0.00),(0.20, 1.00, 0.00),(0.15, 1.00, 0.00),(0.10, 1.00, 0.00),(0.05, 1.00, 0.00),
(0.00, 1.00, 0.00),(0.00, 0.95, 0.05),(0.00, 0.90, 0.10),(0.00, 0.85, 0.15),(0.00, 0.80, 0.20),(0.00, 0.75, 0.25),(0.00, 0.70, 0.30),(0.00, 0.65, 0.35),(0.00, 0.60, 0.40),(0.00, 0.55, 0.45),(0.00, 0.50, 0.50),(0.00, 0.45, 0.55),(0.00, 0.40, 0.60),(0.00, 0.35, 0.65),(0.00, 0.30, 0.70),(0.00, 0.25, 0.75),(0.00, 0.20, 0.80),(0.00, 0.15, 0.85),(0.00, 0.10, 0.90),(0.00, 0.05, 0.95),
(0.00, 0.00, 1.00),(0.05, 0.00, 1.00),(0.10, 0.00, 1.00),(0.15, 0.00, 1.00),(0.20, 0.00, 1.00),(0.25, 0.00, 1.00),(0.30, 0.00, 1.00),(0.35, 0.00, 1.00),(0.40, 0.00, 1.00),(0.45, 0.00, 1.00),(0.50, 0.00, 1.00),(0.55, 0.00, 1.00),(0.60, 0.00, 1.00),(0.65, 0.00, 1.00),(0.70, 0.00, 1.00),(0.75, 0.00, 1.00),(0.80, 0.00, 1.00),(0.85, 0.00, 1.00),(0.90, 0.00, 1.00),(0.95, 0.00, 1.00)
]

while x < int(num):
    idx = int(c)
    color = colors[idx]
    turtle.color(color)
    turtle.forward(x)
    turtle.right(98)
    x += 1
    c += 0.1


t.penup()
 
def draw_circle(x,y,color_circles,radius):
      t.down()
      t.setposition(x,y)
      t.color(color_circles)
      t.circle(radius)
      t.penup()

print()

while True:
    get_circles = input("Do you want to add circles? yes or no")
    
    if get_circles == ("no"):
        print("Okay little boring")
        num_circles = 0
        break
     
    elif get_circles != ("yes"):
        print("Invalid input")
        continue
    else:
        
        color_circles = input("What color should they be?")
        num_circles =input( "How many circles should we add? Less than 1000 please")
        break




if int(num_circles) > 200:
    num_circles = input("How many circles do you want to add? Less than 1000 please.")
    print()
    color_circles = input("What color should they be?")


    
while amount_circles < int(num_circles):
             
             x = random.choice(positions)
             y = random.choice(positions)
             radius = random.choice(values)
             draw_circle(x,y,color_circles,radius)
           
             amount_circles += 1

             

fancy = input("We gotta add something else... give a color")
r = random.choice(values)
s = random.choice(small_set)
for i in range(s):
    t.color(fancy)
    t.circle(r * i) 
    t.up() 
    t.sety((r * i)*(-1)) 
    t.down() 



tri_color =input("You need some triangles they will be the same color as the last but what is the outline color.Give a color")
amount_triangles =input("How many should we draw? Less than 200 please")
p = random.choice(positive)
v = random.choice(positive)

t.pencolor(tri_color)
for i in range(int(amount_triangles)):
    #pendown()
    
    t.begin_fill()
    t.fd(p)
    t.lt(v)
    t.fd(p)
    t.lt(v)
    t.fd(p)
    t.end_fill()

print("Thanks for designing")
turtle.exitonclick()

                

