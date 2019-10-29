'''109-Trochę matematyki w Pythonie'''

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']

sumOfPoints = 4988

print('Największa wartość to:', max(percent),'Najmniejsza wartość to:',min(percent))

for i in range(len(countries)):
    print(percent[i],'\t',int(percent[i]),'\t',round(percent[i],2),'\t',int((sumOfPoints/100)*percent[i]),'\t',countries[i] )


print('--------------------------------------------')

'''112 - Korzystanie z modułów'''

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,

           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,

           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,

           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,

           8.740978348,6.174819567]

percent.sort()
print(percent)

import statistics

print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))

from statistics import*
print(median(percent))
print(median_low(percent))
print(median_high(percent))

print('---------------------------------------')
''' 115 - Moduł math'''

import math
'''
1° = (π * rad)/180   
1 rad = 180°/π
'''
#3
degree=360
radian=degree*math.pi/180
print('%2d degree is %f radians' %(degree, radian))

print('*********************')

#4
degree=45
radian=degree*math.pi/180
print('%2d degree is %f radians' %(degree, radian))

print('*********************')

#5

print('%d degree is %f radians' % (360, math.radians(360)))
print(math.radians(360))
print('%d degree is %f radians' % (45, math.radians(45)))
print(math.radians(45))

print('*********************')
#6

small_r=22
small_price=11.5
big_r=27
big_price=15.6
family_r=38
family_price=22

small_area=math.pi*small_r**2
big_area=math.pi*big_r**2
family_area=math.pi*family_r**2

print('small', small_r, small_price, small_area)
print('big', big_r, big_price, big_area)
print('family', family_r, family_price, family_area)
print('\n')
print('small', small_price/small_area)
print('big', big_price/big_area)
print('family', family_price/family_area)

print('\n')
math_ls=dir(math)
print(math_ls)
