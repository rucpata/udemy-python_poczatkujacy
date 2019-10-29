import math

#3
degree=360

radian=math.pi*degree/180
print(radian)

#4
degree=45
radian=math.pi*degree/180
print(radian)

#5
print(math.radians(360))
print(math.radians(45))

print('')

#6
small_pizza_r=0.22
big_pizza_r=0.27
family_pizza_r=0.38
small_pizza_price=11.50
big_pizza_price=15.60
family_pizza_price=22.00

small_area=math.pi*small_pizza_r**2
big_area=math.pi*big_pizza_r**2
family_area=math.pi*family_pizza_r**2


print('Cena za metr kwadratowy pizzy small:',small_pizza_price/small_area)
print('Cena za metr kwadratowy pizzy big:', big_pizza_price/big_area)
print('Cena za metr kwadratowy pizzy familu:', family_pizza_price/family_area)

print(' ')
math_ls=dir(math)
print(math_ls)
