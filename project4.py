""""
Content : 편의점에서 고객이 물건을 산다.

Date : 2022.06.07
Team : H
Members : 남소연, 윤준서, 전시영, 정가은, 송채영
"""

from abc import *
from dataclasses import dataclass
import sys

# ============================================================================
# ==                                                                       ==
# ==                               추상 클래스                                ==
# ==                                                                       ==
# ============================================================================

# -----------------------------------------------------------------------
# -------------------------------------------------------- AbstractPerson

class AbstractPerson(metaclass=ABCMeta):
    """사람 추상 클래스"""
    __person_num = '고객의 수'

    def __init__(self, name, money, wage):
        name = '고객 이름'
        point = '고객의 포인트'
        money = '현재 가진 돈'
        item_list = '구매한 물건 목록'
        wage = '시급'
        membership_num = '회원 번호'

    @classmethod
    @abstractmethod
    def person_num(cls):
        print('현재까지 사람의 수를 리턴하는 메서드입니다.')


    @abstractmethod
    def change_wage(self, input_wage):
        print('새로운 임금을 매개변수로 받아 새로운 임금으로 바꾸는 메서드입니다.')


    @abstractmethod
    def make_money(self, work_hours):
        print('일할 시간을 매개변수로 받아 해당 시간 만큼 일을 해 돈을 버는 메서드입니다.')


    @abstractmethod
    def add_item(self,item, num):
        print('구매 목록에 구매한 상품을 추가하는 메서드입니다.')

    @abstractmethod
    def purchase(self, cost):
        print('물건 구매 비용을 결제하는 메서드입니다.')

    @abstractmethod
    def buy_item(self, item, num):
        print('물건을 구매하는 과정에서 바뀌는 고객 정보를 갱신하는 메서드입니다.')




# -----------------------------------------------------------------------
# ----------------------------------------------- AbstractConvenientStore


class AbstractConvenientStore(metaclass=ABCMeta):
    """편의점 추상 클래스."""
    __convenient_stores = '편의점 지점들의 목록'

    def __init__(self, input_branch_name):
        branch_name = '지점명'
        inventory = '재고 목록'
        customers = '고객 명단'
        revenue = '수입'


    @classmethod
    @abstractmethod
    def get_convenient_stores(cls):
        print('현재 있는 편의점 지점들을 리턴하는 메서드입니다.')

    @abstractmethod
    def add_customer(self, customer):
        print('고객을 고객명단에 추가하는 메서드입니다.')

    @abstractmethod
    def print_customers(self):
        print('고객 명단을 출력하는 메서드입니다.')

    @abstractmethod
    def search_customer(self, membership_num):
        print('입력받은 회원번호를 통해 고객의 정보를 출력하는 메서드입니다.')


    @abstractmethod
    def add_item(self, item_name, num):
        print('재고 목록에 입고된 상품을 추가하는 메서드입니다.')

    @abstractmethod
    def remove_item(self, item_name, num):
        print('재고 목록에서 상품을 제거하는 메서드입니다.')

    @abstractmethod
    def print_inventory(self):
        print('재고 목록을 출력하는 메서드입니다.')

    @abstractmethod
    def get_item_info(self, item_name):
        print('특정상품의 재고 정보를 반환하는 메서드입니다.')

    @abstractmethod
    def sell_item(self, customer, item_name, num):
        print('상품을 판매하는 메서드입니다.')

    @abstractmethod
    def print_revenue(self):
        print('현재까지의 수입을 출력하는 메서드입니다.')

    @abstractmethod
    def change_discount_rate(self, item_name, input_discount_rate):
        print('특정상품의 할인률을 변경하는 메서드입니다.')




# ============================================================================
# ==                                                                       ==
# ==                             상속 받은 클래스                              ==
# ==                                                                       ==
# ============================================================================

# -----------------------------------------------------------------------
# ---------------------------------------------------------------- Person



class Person():

    def __init__(self, input_name, input_money=0, input_wage=10):
        self.__name = input_name
        self.__money = input_money
        self.__wage = input_wage










class Customer(Person):
    """사람 클래스."""
    __customer_num = 0

    def __init__(self, input_name, input_money, input_wage):

        if (input_money < 0) or (input_wage <= 0):
            super().__init__(input_name, input_money, input_wage)


            print('[error] usage: Person(이름->문자열, \
										현재 가진 돈->0이상의 정수, \
										임금->1이상의 정수)', file=sys.stderr)
            return

        self.__name = input_name
        self.__point = 0
        self.__money = input_money
        self.__item_list = {}
        self.__wage = input_wage
        Customer.__customer_num += 1
        self.__membership_num = Customer.__customer_num

    @classmethod
    def customer_num(cls):
        return cls.__customer_num


    @property
    def name(self):
        return self.__name


    @property
    def membership_num(self):
        return self.__membership_num


    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, input_point):
        self.__point = input_point


    @property
    def wage(self):
        return self.__wage

    @wage.setter
    def wage(self, input_wage):
        self.__wage = input_wage

    def change_wage(self, input_wage):
        if input_wage > 0:
            print(f'[사람] {self.name}의 임금이 시간 당 \
				{self.wage}원에서 {input_wage}원으로 바뀌었습니다.\n')
            self.wage = input_wage
        else:
            print('[사람] 변경하고자 하는 임금은 0보다 큰 정수여야 합니다.\n')


    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, input_money):
        self.__money = input_money

    def make_money(self, work_hours):
        if work_hours > 0:
            income = work_hours * self.wage
            print(f'[사람] {self.name}은 {self.wage}시간을 일해서 {income}원을 벌었습니다.')
            self.money = self.money + income
            print(f'[사람] 현재 {self.money}원을 갖고 있습니다.\n')
        else:
            print('[사람] 일한 시간은 0시간 보다 커야 합니다.\n')


    @property
    def item_list(self):
        return self.__item_list

    @item_list.setter
    def item_list(self, input_item_list):
        self.__item_list = input_item_list

    def add_item(self,item, num):
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
        self.point += int(cost * 0.1) #10퍼센트를 포인트로 적립(소수점은 내림)

        return True


    def buy_item(self, item, num):
        if self.purchase(item.price * num):
            self.add_item(item, num)
            print(f'[사람] {self.name}은 {item.name}을(를) {num}개 구매하였습니다.')
            return True
        print(f'[사람] {self.name}은 잔액이 부족합니다.\n')
        return False


# # -----------------------------------------------------------------------
# -------------------------------------------------------------------- Item

@dataclass
class Item:
    """물건 클래스."""
    name: str
    full_price: int    #정가
    price: int         #판매가(할인률 적용된 가격)
    quantity: int
    discount_rate: float



# # -----------------------------------------------------------------------
# --------------------------------------------------------- ConvenientStore

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


    @classmethod
    def get_convenient_stores(cls):
        return cls.__convenient_stores


    @property
    def branch_name(self):
        return self.__branch_name


    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, new_customer):
        self.__customers = new_customer

    def add_customer(self, customer):
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


    @property
    def inventory(self):
        return self.__inventory

    @inventory.setter
    def inventory(self, new_inventory):
        self.__inventory = new_inventory

    def add_item(self, item_name, num):
        if item_name not in self.inventory:
            while True:
                price = input(f'>>{item_name}의 가격을 입력하세요: ')
                if price.isdigit():
                    break
                print('가격을 잘 못 입력했습니다. 다시 입력하세요.')

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


    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, new_sales):
        self.__revenue = new_sales

    def print_revenue(self):
        print(f'[편의점] 현재까지의 수입은 {self.revenue}입니다.\n')


    def change_discount_rate(self, item_name, input_discount_rate):
        if (item := self.get_item_info(item_name)):
            item.discount_rate = input_discount_rate
            item.price *= input_discount_rate
