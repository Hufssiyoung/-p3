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
        self.__total_work_days = 0

    # getter & setter =====================
    @property
    def name(self):
        return self.__name

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, input_money):
        self.__money = input_money

    @property
    def wage(self):
        return self.__wage

    @property
    def total_work_days(self):
        return self.__total_work_days

    @total_work_days.setter
    def total_work_days(self, new_days):
        self.__total_work_days = new_days

    # ======================================

    def make_money(self, work_days):
        if work_days > 0:
            income = work_days * self.__wage
            print(f'[사람] {self.__name}은 {work_days}일을 일해서 {income}원을 벌었습니다.')
            self.__money += income
            print(f'[사람] 현재 {self.__money}원을 갖고 있습니다.\n')
            self.__total_work_days += work_days
        else:
            print('[사람] 일한 시간은 0시간 보다 커야 합니다.\n')


    def change_wage(self, input_wage):
        if self.__wage > 0:
            print(f'[사람] {self.__name}의 임금이 {self.__wage}원에서 {input_wage}원으로 바뀌었습니다.\n')
            self.__wage = input_wage
        else:
            print('[사람] 변경하고자 하는 임금은 0보다 큰 정수여야 합니다.\n')



# Customer ---------------------------------------------------------------

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

    # ======================================

    @classmethod
    def customer_num(cls):
        return cls.__customer_num


    def add_item_to_itemlist(self,item, num):
        self.__item_list.setdefault(item.name, 0)
        self.__item_list[item.name] += num

    def purchase(self, cost):
        if (self.__point + self.__money) < cost:
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
            self.__point -= cost
            if self.__point > 0:
                return True
            cost = -self.__point
            self.__point = 0

        self.__money -= cost
        point_rate = 0.1
        self.__point += int(cost * point_rate) #10퍼센트를 포인트로 적립(소수점은 내림)

        return True

    def buy_item(self, item, num):
        if self.purchase(item.price * num):
            self.add_item_to_itemlist(item, num)
            print(f'[사람] {self.__name}은 {item.__name}을(를) {num}개 구매하였습니다.')
            return True
        print(f'[사람] {self.__name}은 잔액이 부족합니다.\n')
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

class AbstractConvenientStore(metaclass=ABCMeta):
    """편의점 추상 클래스."""
    __convenient_stores = '현재까지 개업한 편의점 지점들의 목록'

    def __init__(self, input_branch_name):
        branch_name = '지점명'
        inventory = '재고 목록'
        customers = '고객 명단'
        revenue = '수입'

    @abstractmethod
    def add_customer(self):
        print('고객 명단에 고객을 추가하는 메서드입니다.')
        
    @abstractmethod
    def add_item(self):
        print('재고를 재고 목록에 추가하는 메서드입니다.')

    @abstractmethod
    def sell_item(self):
        print('물건을 고객에게 파는 메서드입니다.')
        
    @abstractmethod
    def change_discount_rate(self):
        print('할인율을 변경하는 메서드입니다.')



class ConvenientStore(AbstractConvenientStore):
    """편의점 클래스."""
    __convenient_stores = []

    def __init__(self, input_branch_name):
        self.__branch_name = input_branch_name
        self.__customers = {}
        self.__inventory = {}
        self.__revenue = 0
        ConvenientStore.__convenient_stores.append(self.__branch_name)
        print(f'[편의점] 새로운 매장 {self.__branch_name}점이 생겼습니다.\n')

    # getter & setter ----------------------
    @property
    def branch_name(self):
        return self.__branch_name

    @property
    def revenue(self):
        return self.__revenue

    @classmethod
    def get_convenient_stores(cls): #아래의 property로 바꾸는 게 좋을 듯
        return cls.__convenient_stores

    # @classmethod
    # @property
    # def convenient_stores(cls): #property로 바꾸는 게 좋을 듯
    #     return cls.__convenient_stores
    # ======================================

    def add_customer(self, customer): #add_new_customer
        self.__customers[customer.membership_num] = customer

    def print_customers(self):
        print('======== 고객 목록 ========')
        print('회원번호\t|\t 성함')
        print('-------------------------')
        for membership_num, customer in self.__customers.items():
            print(f"{membership_num}\t:\t{customer.name} 님")
        print('=========================\n')

    def search_customer(self, membership_num):
        if membership_num in self.__customers:
            print(self.__customers[membership_num])
        else:
            print('[편의점] 존재하지 않는 회원입니다.\n')


    def add_item(self, item_name, num):
        if item_name not in self.__inventory:
            while True:
                price = input(f'>>{item_name}의 가격을 입력하세요: ')
                if price.isdigit():
                    break
                print('가격을 잘못 입력했습니다. 다시 입력하세요.')

            price = int(price)
            self.__inventory[item_name] = Item(item_name, price, price, num, 0)
        else:
            item = self.__inventory[item_name]
            item.quantity += num
        print(f'[편의점] {item_name}이 {num}개 입고되었습니다.\n')

    def remove_item(self, item_name, num):
        self.__inventory[item_name].quantity -= num


    def print_inventory(self):
        print('======== 재고 현황 ========')
        for name in self.__inventory:
            print(f"{name}\t:\t{self.get_item_info(name).quantity}개")
        print('=========================\n')


    def get_item_info(self, item_name):
        if item_name in self.__inventory:
            return self.__inventory[item_name]
        return None


    def sell_item(self, customer, item_name, num):

        item = self.get_item_info(item_name)
        if (item is None) or (item.quantity < num):
            print('[편의점] 재고가 부족합니다.\n')
            return

        if customer.membership_num not in self.__customers:
            self.add_customer(customer)

        if customer.buy_item(item, num):
            self.remove_item(item.name, num)
            self.__revenue += item.price * num
            print(f'[편의점] {item.name}을 {num}개 판매했습니다.\n')
        return


    def print_revenue(self):
        print(f'[편의점] 현재까지의 수입은 {self.__revenue}입니다.\n')


    def change_discount_rate(self, item_name, input_discount_rate):
        if (item := self.get_item_info(item_name)):
            item.discount_rate = input_discount_rate
            item.price *= input_discount_rate



# Tax_administration --------------------------------------------------------- 

class Tax_administration():

    def __init__(self):
        self.__collected_money = 0
        self.__tax_rates = [[8800, 0.24], [4600, 0.15],[1200, 0.06], [0, 0.01]]  #[소득 구간을 기준액, 해당 소득 구간의 세율]
        self.__defaulters = {}

    # getter & setter =====================
    @property
    def collected_money(self):
        return self.__collected_money

    @property
    def tax_rates(self):
        return self.__tax_rates

    @property
    def defaulters(self):
        return self.__defaulters

    # ======================================

    def calc_tax(self, tax_payer): 
        for tax_bracket in self.__tax_rates:
            if tax_payer.wage > tax_bracket[0]:
                tax = int((tax_payer.wage * tax_payer.total_work_days) * tax_bracket[1])
                tax_payer.total_work_days = 0
                print(f'{tax_payer.name}님 {tax}만큼 세금을 납부하셔야 합니다')
                return tax
    
    def collect_tax(self, tax_payer):
        tax = self.calc_tax(tax_payer)
        if tax_payer.name in self.__defaulters.keys():
            tax += self.__defaulters[tax_payer.name]
            del(self.__defaulters[tax_payer.name])

        if tax_payer.money > tax:
            tax_payer.money -= tax
            print(f'[국세청] {tax_payer.name}님 세금 {tax}원이 납부되었습니다.')
            self.__collected_money += tax
        else:
            self.__defaulters[tax_payer.name] = tax
            print('[국세청] 가지고 있는 금액이 부족합니다.')



# admin = Tax_administration()
# person1 = Customer('존', 200, 1000)
# print(person1.name, person1.money, person1.wage)

# person1.make_money(100)
# admin.collect_tax(person1)