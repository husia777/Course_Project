from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class Engine(ABC):

    @abstractmethod
    def get_request(self, name_prof, i):
        pass


class HeadHunter(Engine):

    def get_request(self, name_prof: str, i: int) -> list[str]:
        """
        :param name_prof: Имя вакансии
        :param i: Количество страниц сайта для обработки
        :return: Выдаёт 10 вакансий
        """
        data = []
        par = {'per_page': '10', 'page': str(i)}
        api = f'https://api.hh.ru/vacancies?text={name_prof}'
        response = requests.get(api, params=par)
        response = response.json()
        for i in range(10):
            name = response['items'][i]['name']
            try:
                salary = response['items'][i]['salary']['from']
            except:
                salary = 0
            link = response['items'][i]['alternate_url']
            description = [str(v).strip('None').strip('<highlighttext>').strip('</highlighttext>') for v in response['items'][i]['snippet'].values()]
            data.extend([name, salary, link, description])
        return data


class SuperJob(Engine):

    def get_request(self, name_prof: str, i: int) -> list[str]:
        """
        :param name_prof: Имя вакансии
        :param i: Количество страниц сайта для обработки
        :return: Выдаёт 10 вакансий
        """
        data = []
        par = {'per_page': '10', 'page': str(i)}
        api = f'https://russia.superjob.ru/vacancy/search/?keywords={name_prof}'
        response = requests.get(api, params=par)
        html = BeautifulSoup(response.content, 'html.parser')
        for i in range(10):
            name = html.findAll('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')[i].find('a').text
            salary = html.findAll('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')[i].text.replace('\xa0', ' ').replace('По договорённости', '0').replace(' ', '').replace('от', '').replace('до', '').replace('руб.', '').split('—')[0]
            link = 'https://superjob.ru' + html.findAll('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')[i].find('a').get('href')
            description = html.findAll('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')[i].text.replace('<highlighttext>', '').replace('</highlighttext>', '')
            data.extend([name, salary, link, description])
        return data





class Vacancy:

    def __init__(self, job_title, salary_vacancies, link_to_the_vacancy, job_description):
        self.job_title = job_title
        self.salary_vacancies = salary_vacancies
        self.link_to_the_vacancy = link_to_the_vacancy
        self.job_description = job_description


    def __repr__(self):
        return str(self.job_title) + '*' + str(self.salary_vacancies)  + '*' +  str(self.link_to_the_vacancy) + '*' +  str(self.job_description) + '*'



