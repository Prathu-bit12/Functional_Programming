class Bottle:
    def __init__(self,c,m):
        self.capacity = c
        self.material = m
        

obj1 = Bottle(1000,'steel')
obj2 = Bottle(750,'copper')
obj3 = Bottle(350,'plastic')
obj4 = Bottle(500,'aluminium')
obj5 = Bottle(800,'glass')

Bottle_list = []
Bottle_list.append(obj1)
Bottle_list.append(obj2)
Bottle_list.append(obj3)
Bottle_list.append(obj4)
Bottle_list.append(obj5)

for obj in Bottle_list:
    if obj.material == 'steel':
        print(obj.capacity)


   

