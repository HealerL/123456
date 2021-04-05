# 餐厅容纳人数，用于餐厅的属性
class Table():
    def __init__(self, number, volume):
        self.number = number
        self.volume = volume
        self.left = 20
    # 描述餐厅空间
    def describe_table(self):
        print('We have ' + str(self.number) + ' tables which can contain ' + str(self.volume) + ' people.')

# 判断是否有足够位置容纳新客户
    def judge(self, new_customer):
        if self.left < new_customer:
            print('No room for you guys.')
        else:
            self.left = self.left - new_customer
            print('We have enough seats.')



# 餐厅父类
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        # 类中设置初始值的话，不需要在提供相应的形参
        self.owner = 'hll'
        self.table = Table(5,4)
    
    # 描述餐厅信息
    def describe_restaurant(self):
        print("This restaurant is called " + self.restaurant_name.title() + " .")
        print("The cuisine here is " + self.cuisine_type + " .")
    
    # 表示餐厅已经开门
    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() +" is now open.")
    
    #餐厅更换主人
    def owner_update(self,new_owner):
        self.owner = new_owner

    # 服务过的顾客数量
    def set_number_served(self, customer_number):
        if customer_number >= self.number_served:
            self.number_served = customer_number
        else:
            print('customer served cant reduce.')
    # 定量增加服务过的顾客数量
    def increment_number_served(self, increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print('increment cant be minus.')






# 子类 冰淇淋店
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, favors):
        super().__init__(restaurant_name, cuisine_type)
        self.favors = favors
        
    
    # 描述冰淇淋口味
    def describe_favor(self):
        print('The favors are: ')
        for i in self.favors:
            print(i)
    


my_new_restaurant = IceCreamStand('xixi', 'icecream',['milk', 'chocolate'])
my_restaurant = Restaurant('hola','sushi')
my_restaurant.open_restaurant()

my_restaurant.owner_update('wjt')
print(my_restaurant.owner)


my_new_restaurant.describe_favor()

my_new_restaurant.table.describe_table()
