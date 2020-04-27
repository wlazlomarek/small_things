import csv

def increment_and_write(email_list, index=0):
    with open(f'TB_address_newsletter_{index}.csv', 'w', newline='') as file:
        fieldnames = ['name', 'surname', 'display_name', 'nickname', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for el in email_list:
            writer.writerow({'email': f'{el}'})


with open('address.txt', 'r') as f:
    emails = f.read().splitlines()
    emails = [el.strip() for el in emails]
    print(len(emails))

first_list = []
second_list = []
third_list = []

if len(emails) > 49:
    i = 0
    for _ in emails:
        if i < 50:
            first_list.append(_)
            i += 1
        elif 50 <= i <= 99:
            second_list.append(_)
            i += 1
        else:
            third_list.append(_)
            i += 1
    increment_and_write(first_list, index=1)
    increment_and_write(second_list, index=2)
    increment_and_write(third_list, index=3)
else:
    increment_and_write(emails, index=1)

print('Done!')
