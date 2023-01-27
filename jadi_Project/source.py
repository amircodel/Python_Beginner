import hashlib
import csv
from collections import OrderedDict
def hash_password_hack(input_file_name,output_file_name):
    with open(input_file_name) as fin :
        f = csv.reader(fin)
        f = OrderedDict(f)
    passcodes = OrderedDict()
    for i in range(1000,10000):
        hashi = hashlib.sha256(str(i).encode())
        hashi = hashi.hexdigest()
        passcodes[hashi] = str(i)
    with open(output_file_name, 'w', newline='') as fou :
        for k,v in f.items():
            password = passcodes.get(v)
            w = csv.writer(fou)
            w.writerow([k,password])
hash_password_hack('example.csv','xxx.csv')