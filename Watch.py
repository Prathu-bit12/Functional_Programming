class Watch:
    def __init__(self,c,com,b):
        self.color = c
        self.company = com
        self.belt = b

obj1 = Watch('black','Titan','Leather')
obj2 = Watch('red','apple','Leather')
obj3 = Watch('black','fastrack','rubber')
obj4 = Watch('yellow','signature','metal')
obj5 = Watch('white','Titan','Leather')

Watch_list = []
Watch_list.append(obj1)
Watch_list.append(obj2)
Watch_list.append(obj3)
Watch_list.append(obj4)
Watch_list.append(obj5)

for obj in Watch_list:
    if obj.color == 'black':
        print(obj.company)


   

