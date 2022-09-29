import random
import re
def writing_to_a_file(items):
    with open('vacancy.txt', 'a+', encoding='utf-8') as file:
        file.write(str(items)+'\n')



def read_file():
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        print(file.read().split('\n'))


def clear_file():
    with open('vacancy.txt', 'w', encoding='utf-8') as file:
        file.write('')



def top_10():
    b = []
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            print(line.split('\n'))

def random_10():
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()
        r = random.sample(content, 10)
        for i in r:
            print(str(i).strip())



top_10()
#random_10()