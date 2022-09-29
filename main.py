from classes import *
from  utils import *

def main():
    hh = HeadHunter()
    ss = SuperJob()
    name_vacancy = input('Введите название вакансии по которой нужно осуществить поиск>>>')
    count_vacancy = int(input('Введите количество страниц для поиска на двух сайтах в каждой странице по 10 вакансий из двух сайтов в итоге 20 вакансий с одной страницы>>>'))
    for i in range(count_vacancy):
        h = hh.get_request(name_vacancy, i)
        s = ss.get_request(name_vacancy, i)
        a = 0
        for j in range(10):
            vacancy_hh = Vacancy(h[a], h[a+1], h[a+2], h[a+3] )
            vacancy_ss = Vacancy(s[a], s[a+1], s[a+2], s[a+3])
            writing_to_a_file(vacancy_hh.__repr__())
            writing_to_a_file(vacancy_ss.__repr__())
            a+=4


if __name__ == '__main__':
    main()