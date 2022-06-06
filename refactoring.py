from abc import *
from dataclasses import dataclass
import sys

class PersonInitException(Exception):
    def __init__(self):
        super().__init__("[usage] Person(이름->문자열,현재 가진 돈->0이상의 정수, 임금->1이상의 정수)")


# Person ---------------------------------------------------------------- 

class Person():

    def __init__(self, input_name, input_money=0, input_wage=10):
        # if (input_money < 0) or (input_wage <= 0):
        #     raise PersonInitException
        # try: 
        #예외 처리로 만들기
 
        self.__name = input_name
        self.__money = input_money
        self.__wage = input_wage

    # getter & setter =====================
    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @property
    def wage(self):
        return self.__wage

    # ======================================

    def make_money(self, work_days): #work_hours
    # 새로운 버전 들어갈 곳
        pass
    # 구버전 --> 새버전 넣고 구버전은 지우셔도 됩니댜
        # if work_hours > 0:
        #     income = work_hours * self.wage
        #     print(f'[사람] {self.name}은 {self.wage}시간을 일해서 {income}원을 벌었습니다.')
        #     self.money = self.money + income
        #     print(f'[사람] 현재 {self.money}원을 갖고 있습니다.\n')
        # else:
        #     print('[사람] 일한 시간은 0시간 보다 커야 합니다.\n')

    def change_wage(self, input_wage):
        if self.__wage > 0:
            print(f'[사람] {self.__name}의 임금이 {self.__wage}원에서 {input_wage}원으로 바뀌었습니다.\n')
            self.__wage = input_wage
        else:
            print('[사람] 변경하고자 하는 임금은 0보다 큰 정수여야 합니다.\n')


class Customer(Person):
    __customer_num = 0

    def __init__(self, input_name, input_money=0, input_wage=100):
        super().__init__(input_name, input_money, input_wage)
        self.__point = 0
        self.__item_list = {}
        Customer.__customer_num += 1
        self.__membership_num = Customer.__customer_num

    # getter & setter =====================
    @property
    def point(self):
        return self.__point

    @property
    def item_list(self):
        return self.__item_list

    @property
    def membership_num(self):
        return self.__membership_num

    #setter


    # ======================================

    @classmethod
    def customer_num(cls):
        return cls.__customer_num


    def add_item_to_itemlist(self,item, num):
        self.item_list.setdefault(item.name, 0)
        self.item_list[item.name] += num

    def purchase(self, cost):
        if (self.point + self.money) < cost:
            return False

        while True:
            payment = input('''======== 결제 수단 선택 ========
1) 포인트(포인트 차감 후, 부족한 차액은 현금으로 결제됩니다.)
2) 현금
===========================
>> 원하는 결제 수단을 입력하세요: ''')
            if payment in ['포인트', '현금', '1', '2']:
                break
            print('[사람] 메뉴를 잘못 입력했습니다. 다시 입력하세요.')

        if payment in ['포인트', '1']:
            self.point -= cost
            if self.point > 0:
                return True
            cost = -self.point
            self.point = 0

        self.money -= cost
        point_rate = 0.1
        self.point += int(cost * point_rate) #10퍼센트를 포인트로 적립(소수점은 내림)

        return True

    def buy_item(self, item: Item, num):
        if self.purchase(item.price * num):
            self.add_item_to_itemlist(item, num)
            print(f'[사람] {self.name}은 {item.name}을(를) {num}개 구매하였습니다.')
            return True
        print(f'[사람] {self.name}은 잔액이 부족합니다.\n')
        return False



# Item -------------------------------------------------------------------- 

@dataclass
class Item:
    """물건 클래스."""
    name: str
    full_price: int    #정가
    price: int         #판매가(할인률 적용된 가격)
    quantity: int
    discount_rate: float

# ConvenientStore --------------------------------------------------------- 

class ConvenientStore(AbstractConvenientStore):
    """편의점 클래스."""
    __convenient_stores = []

    def __init__(self, input_branch_name):
        self.__branch_name = input_branch_name
        self.__customers = {}
        self.__inventory = {}
        self.__revenue = 0
        ConvenientStore.__convenient_stores.append(self.__branch_name)
        # print(f'[편의점] 새로운 매장 {self.__branch_name}점이 생겼습니다.\n')

    # getter & setter =====================

    @property
    def branch_name(self):
        return self.__branch_name

    @property
    def customers(self):
        return self.__customers

    @property
    def inventory(self):
        return self.__inventory


    @property
    def revenue(self):
        return self.__revenue

    # ======================================

    @classmethod
    def get_convenient_stores(cls):
        return cls.__convenient_stores


    def add_customer(self, customer): #add_new_customer
        self.customers[customer.membership_num] = customer

    def print_customers(self):
        print('======== 고객 목록 ========')
        print('회원번호\t|\t 성함')
        print('-------------------------')
        for membership_num, customer in self.customers.items():
            print(f"{membership_num}\t:\t{customer.name} 님")
        print('=========================\n')

    def search_customer(self, membership_num):
        if membership_num in self.customers:
            print(self.customers[membership_num])
        else:
            print('[편의점] 존재하지 않는 회원입니다.\n')


    def add_item(self, item_name, num):
        if item_name not in self.inventory:
            while True:
                price = input(f'>>{item_name}의 가격을 입력하세요: ')
                if price.isdigit():
                    break
                print('가격을 잘못 입력했습니다. 다시 입력하세요.')

            price = int(price)
            self.inventory[item_name] = Item(item_name, price, price, num, 0)
        else:
            item = self.inventory[item_name]
            item.quantity += num
        print(f'[편의점] {item_name}이 {num}개 입고되었습니다.\n')

    def remove_item(self, item_name, num):
        self.inventory[item_name].quantity -= num


    def print_inventory(self):
        print('======== 재고 현황 ========')
        for name in self.inventory:
            print(f"{name}\t:\t{self.get_item_info(name).quantity}개")
        print('=========================\n')


    def get_item_info(self, item_name):
        if item_name in self.inventory:
            return self.inventory[item_name]
        return None


    def sell_item(self, customer, item_name, num):

        item = self.get_item_info(item_name)
        if (item is None) or (item.quantity < num):
            print('[편의점] 재고가 부족합니다.\n')
            return

        if customer.membership_num not in self.customers:
            self.add_customer(customer)

        if customer.buy_item(item, num):
            self.remove_item(item.name, num)
            self.revenue += item.price * num
            print(f'[편의점] {item.name}을 {num}개 판매했습니다.\n')
        return


    def print_revenue(self):
        print(f'[편의점] 현재까지의 수입은 {self.revenue}입니다.\n')


    def change_discount_rate(self, item_name, input_discount_rate):
        if (item := self.get_item_info(item_name)):
            item.discount_rate = input_discount_rate
            item.price *= input_discount_rate
