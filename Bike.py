class Bike:
    def __init__(self,c,p,e):
        self.company = c
        self.price = p
        self.engine = e

obj1 = Bike('jupiter',1000000,120)
obj2 = Bike('access',90000,110)
obj3 = Bike('honda',150000,120)
obj4 = Bike('hero',95000,115)
obj5 = Bike('duet',2000000,120)

Bike_list = []
Bike_list.append(obj1)
Bike_list.append(obj2)
Bike_list.append(obj3)
Bike_list.append(obj4)
Bike_list.append(obj5)
Bike_list.append(obj1)

for obj in Bike_list:
    if obj.company == 'jupiter':
        print(obj.price,obj.engine)
    
    if obj.price>1000000:
        print(obj.company,obj.engine)



   

