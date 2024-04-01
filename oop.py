# 1.class,object
# 2.inheritance
# 3.encapsulation
# 4.abstract class
# 5.polymorphism
# 6. constructor
# 7.instance attribute   
# 8.composition
# 9.decorator
# 10.getter_setter
# 11.inner_function
# 12.override
# 13.staticattribute


# class
class phone:
    price =10000
    color="blue"
    brand="samsung"
# object
my_phone=phone()
print(my_phone)    
print(my_phone.color)
print(my_phone.brand)

class calculator:
    name="casio Es_999fx"
    def add(self,n1,n2):
        add=n1+n2
        return add
my_calculator=calculator()
print(my_calculator.add(3,4))


# constructor
class phone1:
    manufactured="China"
    def __init__(self,owner,brand,price):
        self.owner=owner
        self.brand=brand
        self.price=price
    def send_sms(self,phone,sms):
        text=f"sedning to sms {phone} in text {sms}" 
        print(text)

my_phone1=phone1('mohabbat','oppo',10000)
print(my_phone1.owner,my_phone1.brand,my_phone1.price)
my_phone1.send_sms('01788939870','Hello, this is a test message!')
# method 
# firstly printed from object 
# just printed object instructions

# instance attributes
class shop:
    shapping_mall="jumuna_mall"
    def __init__(self,buyer) -> None:
        self.buyer = buyer
        self.chart=[]
        
    # or
    # chart=[] #class attribute
    # def __init__(self,buyer):
    #     self.buyer=buyer
    def add_to_chart(self,item):
        self.chart.append(item)

buyer_person=shop("ezekiel")
buyer_person.add_to_chart('shoes')
buyer_person.add_to_chart('shirt')
print(f"{buyer_person} puchess {buyer_person.chart} in {buyer_person.shapping_mall}")

# self.name=attributes,name=parameters

# representaion
# __repr__(self) -> str:: This is a special method in Python classes. It stands for “representation” and is used to define how an object of the class should be represented as a string when printed. When you call print(ali) in your code, Python will look for the __repr__ method to determine what string representation to display.
# redability,debugging.consistancy 
class stuedent:
    def __init__(self,name,cls,id):
        self.name=name
        self.cls=cls
        self.id=id

    def __repr__(self)->str:
        return f'student name: {self.name},class: {self.cls},id: {self.id}'

ali=stuedent('mehmed',10,1)
print(ali)

# school
class shopping:

    def __init__(self,name):
        self.name=name
        self.chart=[]

    def add_to_chart(self,item,price,quantity):
        product={'item':item,'price':price,'quantity':quantity}
        self.chart.append(product)

    def remove_item(self,item_name):
        for item in self.chart:
            if item['item'] == item_name: #item['item']=item name
                self.chart.remove(item_name)
                print(f'{item_name} removed from the chart.')
                return 
            print(f'{item_name} not found in the chart.')

    def checkout(self,amount):
        total=0
        for item in self.chart:
            total+=item['price']*item['quantity']
        print('tatal price:',total)
        if(amount<total):
            print(f'please provide {total-amount} more.')
        else:
            extra=amount-total
            print(f'herer are your item and extra money: {extra}')
            self.chart.clear()

ezekiel=shopping("ezekiel")
ezekiel.add_to_chart('alu',59,6)
ezekiel.add_to_chart('kodu',60,2)
ezekiel.add_to_chart('law',87,9)
print(ezekiel.chart)

ezekiel.checkout(600)
# [{'item': 'alu', 'price': 50, 'quantity': 6}, {'item': 'dim', 'price': 50, 'quantity': 6}, {'item': 'rice', 'price': 50, 'quantity': 6}]  
# Total price: 900
# Please provide 300 more.


# abstract base class
# Abstract base classes are used to define a common interface for a group of related classes.
        # It has a constructor (__init__) that takes a name argument.
        # It calls the parent class’s constructor using super().__init__().

from abc import ABC,abstractmethod
class animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    def move(self):
        pass

class monkey(animal):
    def __init__(self) -> None:
        self.name="monkey"
        super().__init__()

    def eat(self):
        print("Eating banana")


# encapsulation
#encapsulation used for information hiding,public,ptotected & private accessing

class bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name
        self._branch="banani"
        self.__balance=initial_deposit
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        print(f'Your current balance: {self.balance}')

    def get_balance(self):
        return self.__balance
    
mehmed=bank("mehmed",100000)
print(mehmed._bank__balance)    


# inheritance
# Types of Inheritance:
# Single Inheritance: A child class inherits from a single parent class.
# Multiple Inheritance: A child class inherits from multiple parent classes.
# Multilevel Inheritance: A child class inherits from another child class (forming a chain).
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of the above types.

class device:
    def __init__(self,brand,price,color):
        self.brand=brand
        self.price=price
        self.color=color

    def run(self):
        return f'Running'

class laptop:
    def __init__(self,memory):
        self.memory=memory

    def coding(self):
        return f'learnig oop with python'

class phone(device):
    def __init__(self,brand,price,color,dual_sim):
        self.dual_sim=dual_sim
        super().__init__(brand,price,color)

    def phone_call(self,number,text):
        return f'Sending sms to:{number} with {text}'


my_phone=phone('apple',12000000,'black',True)
print(my_phone.brand)


# multilevel

class vehicle:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def move(self):
        pass
    def __repr__(self) -> str:
        return f'from vehicle' 

class bus(vehicle):
    def __init__(self, name, price,set):
        self.set=set
        super().__init__(name, price)       

    def __repr__(self) -> str:
        return f'from bus'
    

class ac_bus(bus):
    def __init__(self, name, price,set,temp):
        self.temp=temp
        super().__init__(name, price,set)

    def __repr__(self) -> str:
        return super().__repr__()

hanif=ac_bus("dhaka_bus",1000,50,28)
print(hanif)            

# polimorphism
# deffrent class in same function name but access seperatly
class Animal:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_sound(self):
        print('Animal making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('meow meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def make_sound(self):
        print('woof woof')

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Local Shepard')
shepard.make_sound()



# composition
# It has two instance variables:
# self.engine: An instance of the Engine class (composition).
# self.driver: An instance of the Driver class (composition).
# It provides a start() method:
# Calls the start() method of the Engine object (composition).

class Engine:
    def __init__(self) -> None:
        pass
    def start(self):
        return f'Engine started'
    
class Driver:
    def __init__(self):
        pass

class Car:
    def __init__(self):
        self.engine=Engine()
        self.driver=Driver()
    def start(self):
        self.engine.start()



#decorator 
# logging,timing,authorizations,caching,validation
# build in decorator @staticmethod,@classmethod,@property
# How Decorators Work:
# A decorator takes a function (or method) as an argument and returns a modified version of that function.
# The modified function can have additional behavior before or after the original function is called.
# Decorators are applied using the @decorator_name syntax just above the function definition.

def timer(func):
    def inner_fun(*args):
        print("inside timer inner fun")
        func(*args)
    return inner_fun

@timer
def get_factorial(n):
    print("factorial",n)
get_factorial(5)


# gretter_setter
# In Python, a setter method is used to set the value of an attribute (property) within a class.
# It allows you to customize how an attribute is modified when its value is updated.
class User:
    def __init__(self,name,age,money) -> None:
        self.name=name
        self._age=age
        self.__money=money

    @property
    def age(self):
        return self._age
    @property
    def salary(self):
        return self.__money

    @salary.setter
    def salary(self,value):
        if value <0:
            return 'salary cannot be negative'
        self.__money +=value

sami=User('sami',21,1200)
print(sami.age,sami.salary)
sami.salary=45748737
print(sami.salary)


#inner function like nested loap
# Corrected duble_decker function
def duble_decker():
    print("starting the duble decker")
    # 1.starting the duble decker

    def inner_fun():
        print("inside the inner function")
        # 2.inside the inner function
        return 3000

    return inner_fun

print(duble_decker()())  # Output will be "starting the duble decker", "inside the inner function", and then 3000

# Corrected do_sumthing function
def do_sumthing(work):
    print("work started")
    # 5.work started
    work()  # Invoking the function object passed as argument
    # 6.sleeping
    print("work ended")
    # 7.work ended

do_sumthing(lambda: print("sleeping"))  # Output will be "work started", "sleeping", and then "work ended"



# override_overlap
class person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("rice, vegetables, food")

class cricket(person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):
        print('beef')  # Corrected eat method to override the eat method in the person class
        
sakib = cricket("sakib", 34, 6, 60, "bd")
sakib.eat()  # Output will be "beef"

mushfiq = cricket("mushfiq", 33, 5, 53, "bd")

# Now, if you want to get the sum of ages, you don't need to define a special method. You can just access the age attribute directly.
total_age = sakib.age + mushfiq.age
print(total_age)  # Output will be the sum of ages, which is 67 in this case


# static attribute
# A class method is bound to the class itself (not an instance) and can be called on the class directly.
# A static method is not bound to the class or any instance. 

class shopping:
    def __init__(self,name,location):
        self.name = name

    @classmethod
    def purchase(self,item):
        print("Purchasing item:",item)

    @staticmethod
    def multiply(a,b):
        print(a*b)

shopping.purchase("phone")
shopping.multiply(10,20)
