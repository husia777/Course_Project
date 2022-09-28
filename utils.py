def writing_to_a_file(items):
    with open('vacancy.txt', 'a+', encoding='utf-8') as file:
        for item in items:
            file.write(str(item) + '\n')



def read_file():
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        print(file.read())


def clear_file():
    with open('vacancy.txt', 'w', encoding='utf-8') as file:
        file.write('')

clear_file()

def top_10():
    with open('vacancy.txt', 'r', encoding='utf-8') as file:
        content = file.read().split('\n')
        for i in content:
            print(i)

top_10()