def large_power(base, exponent):
    result = pow(base, exponent)

    if result > 5000:
        return True
    else: 
        return False

print(large_power(50,4))

def divisible_by_ten(num):
    result = num % 10

    if result == 0:
        return True
    else:
        return False

print(divisible_by_ten(73))

price = int(input('Enter the price: '))
discount_percent = int(input('Enter the discount for the product: '))

def calculate_discount(price, discount_percent):
    if discount_percent > 20:
        return price - price*(discount_percent/100)
    else: 
        return price

print(calculate_discount(price, discount_percent))
