filename = 'alice.txt'
line = 'Europe'

cities = ['Lonon', 'Berlin', 'Paris', 'Warsaw', 'Madrid', 'Rome']

file = open(filename, 'a')

file.write(line)
file.write('\n')
#file.writelines(cities)

for city in cities:
    file.write(city + '\n')

file.close()
