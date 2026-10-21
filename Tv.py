class Tv:
    def __init__(self,ss,n):
        self.size = ss
        self.name = n
        

obj1 = Tv(32,'sony')
obj2 = Tv(64,'samsung')
obj3 = Tv(42,'haier')
obj4 = Tv(50,'xiamoi')
obj5 = Tv(32,'LG')

Tv_list = []
Tv_list.append(obj1)
Tv_list.append(obj2)
Tv_list.append(obj3)
Tv_list.append(obj4)
Tv_list.append(obj5)

for obj in Tv_list:
    if obj.name == 'haier':
        print(obj.size)


   

