# [] create The Weather

#curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt
 
city_file = open('mean_temp.txt', 'a+')
city_file.write('Rio de Janeiro,Brazil,30.0,18.0')

city_file.seek(0)
headings = city_file.readline()
heading = headings.split(',')
print("Stewart Bowman")
city_temp = city_file.readline()
while city_temp:
    cities = city_temp.split(',')
    print(heading[0].title(), 'of', cities[0], heading[2], 'is', cities[2], 'Celcius')
    city_temp = city_file.readline()
city_file.close()