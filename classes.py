from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup


class Engine(ABC):

    @abstractmethod
    def get_request(self, name_prof, i):
        pass


class HeadHunter(Engine):

    def get_request(self, name_prof, i):
        data = []
        par = {'per_page': '10', 'page': str(i)}
        api = 'https://api.hh.ru/vacancies?text=' + name_prof
        response = requests.get(api, params=par)
        response = response.json()
        for i in range(10):
            name = response['items'][i]['name']
            salary = response['items'][i]['salary']['from']
            link = response['items'][i]['alternate_url']
            description = response['items'][i]['snippet']
            data.extend([name, salary, link, description])
        return data


class SuperJob(Engine):

    def get_request(self, name_prof, i):
        data = []
        par = {'per_page': '10', 'page': str(i)}
        api = f'https://russia.superjob.ru/vacancy/search/?keywords={name_prof}'
        response = requests.get(api, params=par)
        html = BeautifulSoup(response.content, 'html.parser')
        for i in range(10):
            name = html.findAll('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')[i].find('a').text
            salary = html.findAll('span', class_='_2eYAG _1nqY_ _249GZ _1jb_5 _1dIgi')[i].text.replace('\xa0', ' ').replace('По договорённости', '0').replace(' ', '').replace('от', '').replace('до', '').replace('руб.', '')
            link = 'https://superjob.ru' + html.findAll('span', class_='_9fIP1 _249GZ _1jb_5 QLdOc')[i].find('a').get('href')
            description = html.findAll('span', class_='_1Nj4W _249GZ _1jb_5 _1dIgi _3qTky')[i].text
            data.extend([name, salary, link, description])
        return data





class Vacancy:

    def __init__(self, job_title, salary_vacancies, link_to_the_vacancy, job_description):
        self.job_title = job_title
        self.salary_vacancies = self.correction_salary_vacancies(salary_vacancies)
        self.link_to_the_vacancy = link_to_the_vacancy
        self.job_description = self.correction_job_description(job_description)


    def __repr__(self):
        return self.job_title, self.salary_vacancies, self.link_to_the_vacancy, self.job_description

    def correction_job_description(self, job_description):
        return job_description

    def correction_salary_vacancies(self, salary_vacancies):
        if salary_vacancies == None:
            self.salary_vacancies = 0


