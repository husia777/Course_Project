from classes import *
from  utils import *

def main():
    hh = HeadHunter()
    ss = SuperJob()
    name_vacancy = input('Введите название вакансии по которой нужно осуществить поиск>>>')
    count_vacancy_h = int(input('Введите количество страниц для поиска на сайте HeadHunter в каждой странице по 10 вакансий>>>'))
    count_vacancy_s = int(input('Введите количество страниц для поиска на сайте SuperJob максимальное количество страниц 2 если превысить макимум по умолчанию будет 2 страницы>>>'))
    if count_vacancy_s > 2:
        print('Превышен лимит по умолчанию установленно значение 2')
        count_vacancy_s = 2
    for i in range(count_vacancy_s):
        s = ss.get_request(name_vacancy, i)
        b = 0
        print(f'Обработка страницы SuperJob {i+1}')
        for j in range(10):
            vacancy_ss = Vacancy(s[b], s[b+1], s[b+2], s[b+3] )
            writing_to_a_file(vacancy_ss.__repr__())
            b+=4

    for i in range(count_vacancy_h):
        h = hh.get_request(name_vacancy, i)
        a = 0
        print(f'Обработка страницы HeadHunter {i+1}')
        for j in range(10):
            vacancy_hh = Vacancy(h[a], h[a+1], h[a+2], h[a+3] )
            writing_to_a_file(vacancy_hh.__repr__())
            a+=4

    cmd = int(input('Введите цифру команды для  дальнейших действий\n1 - Открыть файл\n2 - Вывести 10 рандомных вакансий\n3 - Вывести 10 вакансий с наибольшей зарплатой\n4 - Очистить файл'))
    if cmd == 1:
        read_file()
    elif cmd == 2:
        random_10()
    elif cmd == 3:
        top_10()
    elif cmd == 4:
        clear_file()

if __name__ == '__main__':
    main()