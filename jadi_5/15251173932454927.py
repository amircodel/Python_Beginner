import csv
from collections import OrderedDict
from statistics import mean
from operator import itemgetter
# Task 1 ===>>
def calculate_averages(input_file_name, output_file_name):
    l2 = []
    with open(input_file_name) as fin :
        lines = csv.reader(fin)
        for line in lines :
            for nomreh in line[1:] :
                line.append(float(nomreh))
                line.remove(nomreh)
            meaning = mean(line[1:])
            line.append(meaning)
            for i in line[1:len(line)-1] :
                line.remove(i)
            l2.append(line)
    with open(output_file_name, 'w', newline='') as fou :
        writer = csv.writer(fou)
        for row in l2:
            writer.writerow(row)
# Task 2 ===>>
def calculate_sorted_averages(input_file_name):
    def keymaximumer(dic) :
        dkeym = OrderedDict()
        for key, value in sorted(dic.items(), key= itemgetter(0), reverse = False) :
            dkeym[key] = value
        return dkeym
    l2 = []
    with open(input_file_name) as fin :
        lines = csv.reader(fin)
        for line in lines :
            for nomreh in line[1:] :
                line.append(float(nomreh))
                line.remove(nomreh)
            meaning = mean(line[1:])
            line.append(meaning)
            for i in line[1:len(line)-1] :
                line.remove(i)
            l2.append(line)
        l2 = OrderedDict(l2)
        l2 = keymaximumer(l2)
        dl2 = OrderedDict()
        for key, value in sorted(l2.items(), key= itemgetter(1,0), reverse = False) :
            dl2[key] = value
        dl2 = dl2.items()
        print(dl2)
    with open(output_file_name, 'w', newline='') as fou :
        writer = csv.writer(fou)
        for row in dl2:
            writer.writerow(row)
# Task 3 ===>>
def calculate_three_best(input_file_name, output_file_name):
    l2 = []
    with open(input_file_name) as fin :
        lines = csv.reader(fin)
        for line in lines :
            for nomreh in line[1:] :
                line.append(float(nomreh))
                line.remove(nomreh)
            meaning = mean(line[1:])
            line.append(meaning)
            for i in line[1:len(line)-1] :
                line.remove(i)
            l2.append(line)
        def keymaximumer(dic) :
            dkeym = OrderedDict()
            for key, value in sorted(dic.items(), key= itemgetter(0), reverse = False) :
                dkeym[key] = value
            return dkeym
        l2 = OrderedDict(l2)
        l2 = keymaximumer(l2)
        l3 = []
        maxi = max([(v, k) for k, v in l2.items()])
        maxi = list(maxi)
        maxi = maxi[::-1]
        l2.pop(maxi[0])
        maxi = tuple(maxi)
        l3.append(maxi)
        l31 = []
        for _ in range(2) :
            maxi = max([(v, k) for k, v in l2.items()])
            maxi = list(maxi)
            maxi = maxi[::-1]
            l2.pop(maxi[0])
            maxi = tuple(maxi)
            l31.append(maxi)
        l31 = l31[::-1]
        for i in l31 :
            l3.append(i)
        l3 = OrderedDict(l3)
        l3 = l3.items()
    with open(output_file_name, 'w', newline='') as fou :
        writer = csv.writer(fou)
        for row in l3:
            writer.writerow(row)
# def calculate_three_worst(input_file_name, output_file_name):
# def calculate_average_of_averages(input_file_name, output_file_name):
