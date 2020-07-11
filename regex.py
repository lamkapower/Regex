from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def fix_tel_number(contacts_list):
    pattern = re.compile(r'(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*')
    for data in contacts_list:
        tel_num = pattern.sub(r'+7(\2)\3-\4-\5 \6\7', data[-2])
        data[-2] = tel_num.strip()
    return print(contacts_list)

def fix_name(contacts_list):
    for data in contacts_list:
        try:
            one = data[0].split()
            data[2] = one[2]
            data[1] = one[1]
            data[0] = one[0]
        except IndexError: continue
    for data in contacts_list:
        try:
            two = re.split(r'(\b[А-Я]\w+)', data[1])
            data[2] = two[3]
            data[1] = two[1]
        except IndexError: continue
    for data in contacts_list:
        try:
            three = data[0].split()
            data[1] = three[1]
            data[0] = three[0]
        except IndexError: continue   
    return contacts_list


fix_tel_number(fix_name(contacts_list))