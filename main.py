import csv
import re


class Book:
    contacts = []

    def __init__(self, lastname, firstname, surname, organization, position, phone, email):
        self.lastname = lastname
        self.firstname = firstname
        self.surname = surname
        self.organization = organization
        self.position = position
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'== {self.lastname} {self.email} {self.phone} =='
    
    def __repr__(self):
        return f'** {self.lastname} {self.email} {self.phone} **'

    def find_contact(self):
        success = False
        for c in self.contacts:
            if c.lastname == self.lastname:
                success = True
                if c.email == '':
                    c.email = self.email
                if c.phone == '':
                    c.phone = self.phone
                break
        return success

    def fix_tel_number(self):
        pattern = re.compile(r'(\+7|8)\s*\(*(\d{3})\)*\s*\-*(\d{3})\-*(\d{2})\-*(\d{2})\s*\(*(доб.)*\s*(\d{4})*\)*')
        self.phone = pattern.sub(r'+7(\2)\3-\4-\5 \6\7', self.phone)

    @staticmethod
    def set_contacts(csv_file_path):
        with open(csv_file_path, encoding='utf-8') as f:
            rows = csv.reader(f, delimiter=",")
            contacts_list = list(rows)

            for c in contacts_list[1:]:
                fio = c[0].split()
                io = c[0].split()
                if len(fio) == 3:
                    c[0] = fio[0]
                    c[1] = fio[1]
                    c[2] = fio[2]
                if len(fio) == 2:
                    c[0] = fio[0]
                    c[1] = fio[1]
                if len(io) == 2:
                    c[1] = io[0]
                    c[2] = io[1]

                b = Book(c[0], c[1], c[2], c[3], c[4], c[5], c[6])
                b.fix_tel_number()
                if not b.find_contact():
                    Book.contacts.append(b)

    @staticmethod
    def save_contacts():
        first_row = []
        complit_table = []
        for b in Book.contacts:
            if len(first_row) == 0:
                first_row = b.__dict__.keys()
                complit_table.append(first_row)
            complit_table.append(b.__dict__.values())
        with open("phonebook.csv", "w", encoding='utf-8') as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(complit_table)

                
Book.set_contacts("phonebook_raw.csv")
Book.save_contacts()