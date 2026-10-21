class Pen:
    def __init__(self,c,p):
        self.color = c
        self.price = p
        

obj1 = Pen('black',10)
obj2 = Pen('red',20)
obj3 = Pen('blue',10)
obj4 = Pen('blue',40)
obj5 = Pen('black',45)

Pen_list = []
Pen_list.append(obj1)
Pen_list.append(obj2)
Pen_list.append(obj3)
Pen_list.append(obj4)
Pen_list.append(obj5)

for obj in Pen_list:
    if obj.color == 'black':
        print(obj.price)


   

