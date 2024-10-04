def single_ton(cls):
    l=[]
    def inner (*args,**kwargs):
        if len(l)==0:
            l.append(cls())
        return l[0]
    return inner

@single_ton
class Hanuman:
    def __init__(self):
        self.tickets=60
    def booking(self):
        tickets=int(input('enter no of tickets'))
        if (self.tickets>=tickets):
            self.tickets-=tickets
            print('tickets booked successfully')
        else:
            print("tickets unavailable")
@single_ton
class kalki:
    def __init__(self):
        self.tickets=60
    def stalin(self):
        tickets=int(input('enter no of tickets'))
        if (self.tickets>=tickets):
            self.tickets-=tickets
            print('tickets booked successfully')
        else:
            print("tickets unavailable")
@single_ton
class daddy:
    def __init__(self):
        self.tickets=60
    def booking(self):
        tickets=int(input('enter no of tickets'))
        if (self.tickets>=tickets):
            self.tickets-=tickets
            print('tickets booked successfully')
        else:
            print("tickets unavailable")
@single_ton
class hello:
    def __init__(self):
        self.tickets=60
    def booking(self):
        tickets=int(input('enter no of tickets'))
        if (self.tickets>=tickets):
            self.tickets-=tickets
            print('tickets booked successfully')
        else:
            print("tickets unavailable")
@single_ton
class indra:
    def __init__(self):
        self.tickets=60
    def booking(self):
        tickets=int(input('enter no of tickets'))
        if (self.tickets>=tickets):
            self.tickets-=tickets
            print('tickets booked successfully')
        else:
            print("tickets unavailable")
def Multiplex():
    print('1)hanuman \n2)kalki \n3)daddy \n4)hello \n5)indra')
    option=int(input('choose an option '))
    if (option==1):
        h1=Hanuman()
        h1.booking()
    elif(option==2):
        i1=kalki()
        i1.booking()
    elif(option==3):
        t1=daddy()
        t1.booking()
    elif(option==4):
        d1=hello()
        d1.booking()
    elif(option==5):
        a1=indra()
        a1.booking()
    else:
        print("choose valid option")
while (True):
    Multiplex()