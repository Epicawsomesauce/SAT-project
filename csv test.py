import csv
import math

#data = [['3', '467', '197'], ['1', '828', '195'], ['2', '297', '305'], ['0', '715', '459']]

#with open('data.csv', 'w', newline='') as file:
    #csv_writer = csv.writer(file)
    #csv_writer.writerows(data)


x1 = 100
y1 = 200

lemon = (input('Pick a number from 0 to 3: '))

with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            for element in row:
                  if element == lemon:
                        x2 = int(row[1])
                        y2 = int(row[2])



points = int(((((y2-y1)**2) + ((x2-x1)**2))**1/2)/1000)
print (points)