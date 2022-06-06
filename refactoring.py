from abc import *
from dataclasses import dataclass
import sys

# class PersonInitException(Exception):
#     def __init__(self):
#         super().__init__("[error] usage: \
# Person(이름->문자열,현재 가진 돈->0이상의 정수, 임금->1이상의 정수)")

class Person():

    def __init__(self, input_name, input_money=0, input_wage=10):

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
    
    @wage.setter
    def wage(self, input_wage):
        self.__wage = input_wage

    # ======================================
    def make_money(self, work_hours):
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






class Customer(Person):
    __customer_num = 0

    def __init__(self, input_name, input_money, input_wage):

        if (input_money < 0) or (input_wage <= 0):
            super().__init__(input_name, input_money, input_wage)
            self.__point = 0
            self.__item_list = {}
            Customer.__customer_num += 1
            self.__membership_num = Customer.__customer_num

    # getter & setter =====================

    @property
    def __point(self):
        return self.__point

    @property
    def item_list(self):
        return self.__item_list

    @property
    def membership_num(self):
        return self.__membership_num
    
