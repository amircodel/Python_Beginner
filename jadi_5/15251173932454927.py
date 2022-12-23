import csv
import math
from collections import OrderedDict 
# For the average
from statistics import mean 

def calculate_averages(input_file_name, output_file_name):
    l2 = []
    with open(input_file_name) as fin :
        lines = csv.reader(fin)
        for line in lines :
            for nomreh in line[1:] :
                line.append(float(nomreh))
                line.remove(nomreh)
            jam = math.fsum(line[1:])
            line.append(jam/(len(line) - 1))
            for i in line[1:len(line)-1] :
                line.remove(i)
            l2.append(line)
    with open(output_file_name, 'w', newline='') as fou :
        writer = csv.writer(fou)
        for row in l2:
            writer.writerow(row)
def calculate_sorted_averages(input_file_name, output_file_name):
    l2 = []
    with open(input_file_name) as fin :
        lines = csv.reader(fin)
        for line in lines :
            for nomreh in line[1:] :
                line.append(float(nomreh))
                line.remove(nomreh)
            jam = math.fsum(line[1:])
            line.append(jam/(len(line) - 1))
            for i in line[1:len(line)-1] :
                line.remove(i)
            l2.append(line)
        l2 = OrderedDict(l2)
        dl2 = OrderedDict()
        for key, value in sorted(l2.items(), reverse = False) :
            dl2[key] = value
        dl2 = dl2.items()
    with open(output_file_name, 'w', newline='') as fou :
        writer = csv.writer(fou)
        for row in dl2:
            writer.writerow(row)

# def calculate_three_best(input_file_name, output_file_name):

# def calculate_three_worst(input_file_name, output_file_name):

# def calculate_average_of_averages(input_file_name, output_file_name):
calculate_sorted_averages('jadi_5/nomarat.csv','jadi_5/moadel.csv')