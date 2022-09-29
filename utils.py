import random
import operator

def writing_to_a_file(items):
    with open('vacancy.txt', 'a+', encoding='utf-8') as file:
        file.write(str(items)+'\n')



def read_file():
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        for i in file.read().split('\n'):
            print(i.replace('*', '  '))


def clear_file():
    with open('vacancy.txt', 'w', encoding='utf-8') as file:
        file.write('')



def top_10():
    sorted_list = []
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            list_content = line.split('*')
            list_content[1] = int(list_content[1].replace('None', '0'))
            sorted_list.append(list_content)
    sorted_v = sorted(sorted_list, key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        for item in sorted_v[i]:
            print(item)


def random_10():
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
        r = random.sample(content, 10)
        for i in r:
            print(str(i).replace('*', ' ').replace('None', '0'))
