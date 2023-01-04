import requests
from bs4 import BeautifulSoup
import pprint
response = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')  # subtext will be same as links


def hn_sort(hn):
    return(sorted(hn, key=lambda k: k['votes'], reverse=True))


def res_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href')
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn_sort(hn)


pprint.pprint(res_hn(links, subtext))
