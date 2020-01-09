# Number module v=1.0.1
# coding utf-8

import math

class Number:

    def __init__(self, num):
        self.num = num  # A number or list.

    def high(self):  # Return the most high number of list.
        self.high = 0
        for i in self.num:
            if i > self.high:
                self.high = i
        return self.high

    def low(self):  # Return the most low number of list.
        self.low = self.num[0]
        for i in self.num:
            if i < self.low:
                self.low = i
        return self.low

    def sum(self):  # Return sum numbers of list.
        self.sum = 0
        for i in self.num:
            self.sum += i
        return self.sum
        
    def sqrt(self):  # Return root of self.num
        self.sqrt = math.sqrt(self.num)
        return self.sqrt

    def log(self, y):  # Return log of self.num to the base e.
        self.log = math.log(self.num, y)
        return self.log

    def binary_number(self):  # Return binary_number.
        self.binary_number = bin(self.num)
        return self.binary_number

    def power(self, index):  # Number^index number, but don't return.
        self.num = (self.num) ** (index)

    def fib_list(self): # Return between 1 to numberth fibonacci number.
        self.fib_list = []
        a, b = 1, 0
        for _ in range(self.num):
            self.fib_list.append(a)
            a, b = a + b, a
        return self.fib_list

    def fib(self): # Return numberth fibonacci number.
        a, self.fib = 1, 0
        for _ in range(self.num):
            a, self.fib = a + self.fib, a
        return self.fib
                
    def Fizz_Buzz(self):  # Return fizz buzz of one number.
        self.Fizz_Buzz = ""
        if self.num % 3 == 0 and self.num % 5 == 0:
            self.Fizz_Buzz = "FizzBuzz"
        elif self.num % 3 == 0:
            self.Fizz_Buzz = "Fizz"
        elif self.num % 5 == 0:
            self.Fizz_Buzz = "Buzz"
        else:
            pass
        return self.Fizz_Buzz
      
    def even_odd(self):  # Return even or odd.
        self.even_odd = ""
        if self.num % 2 == 0:
            self.even_odd = "even"
        else:
            self.even_odd = "odd"
        return self.even_odd

    def show(self):  # Show the number's status.
        print(
            self.sqrt(),
            self.binary_number,
            self.fib_list(),
            self.fib(),
            self.Fizz_Buzz(),
            self.even_odd()
            )

def __help__():
     print("""This module is Number module.
     You can get info of number.
     example,
     num = Number(3)
     print(num.even_odd())
     ==>odd
     print(num.Fizz_Buzz())
     ==>Fizz
     This is my first module.
     I'm Japanese and 13 years old in 2020.1 so I can't write English complete.
     thank you."""
     )  

if __name__ == "__main__":
    __help__()

