from abc import *
from dataclasses import dataclass
import sys

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
