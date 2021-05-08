import csv
import sys

def create_csv(email_list, index=1):
    with open(f'TB_address_newsletter_{index}.csv', 'w', newline='') as file:
        fieldnames = ['name', 'surname', 'display_name', 'nickname', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for el in email_list:
            writer.writerow({'email': f'{el}'})


def read_emails():
    try:
        with open('maile.txt', 'r') as f:
            emails = f.read().splitlines()
            emails = [el.strip() for el in emails]
            return emailsa
    except FileNotFoundError as fnf:
        sys.exit(fnf)


def main():
    i = 1
    email_list = read_emails() 

    while len(email_list) > 49:
        temp_list = email_list[:49]
        create_csv(temp_list, i)
        for el in temp_list:
            email_list.remove(el)
        i += 1
    else:
        create_csv(email_list)


if __name__ == '__main__':
    main()
