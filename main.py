import csv
import json


def get_books(csv_file, json_file):
    data = []
    with open(csv_file, encoding='utf-8') as csvfile:
        file_reader = csv.DictReader(csvfile)
        for rows in file_reader:
            data.append(rows)
    with open(json_file, 'w') as file:
        json.dump(data, file)
    return data


def get_user(users_file):
    result_list = []
    with open(users_file, 'r') as file:
        data = json.load(file)
        for user in data:
            result_list.append(dict((key, user[key]) for key in ['name', 'gender', 'address', 'age']))
        for element in result_list:
            element['books'] = []
    return result_list


def get_books_to_user(books, users):
    i = 0
    while i < len(books):
        for user in users:
            user['books'].append(books[i])
            i += 1
            if i == len(books):
                break
    return users


def write_result(final_list):
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(final_list, file)
    return 'result.json'


if __name__ == '__main__':
    result = get_books_to_user(get_books('books.csv', 'books.json'), get_user('users.json'))
    write_result(result)
