import Number as N
num_list = [1, 2, 3]
num1 = N.Number(num_list)
print(num1.high(), num1.low(), num1.sum())

num2 = N.Number(4)
print(num2.sqrt(), num2.log(2), num2.binary_number(), num2.even_odd())

num3 = N.Number(15)
print(num3.Fizz_Buzz())
