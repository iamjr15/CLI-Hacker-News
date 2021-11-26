import requests
from bs4 import BeautifulSoup
import pprint


res1 = requests.get('https://news.ycombinator.com/')

soup1 = BeautifulSoup(res1.text, 'html.parser')
links1=soup1.select('.storylink')
subtext1=soup1.select('.subtext')


res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2=soup2.select('.storylink')
subtext2=soup2.select('.subtext')

links = links1+links2
subtext =subtext1+subtext2

 
def sort_dict(hackernews):
    return sorted(hackernews, key=lambda k:k['votes'],reverse=True)


def custom_hackerrank(links,subtext):
    hackernews=[]
    for  index ,item in enumerate(links):
        title= links[index].getText()
        hyperlink = links[index].get('href',None)
        vote =subtext[index].select('.score')
        if len(vote):
            point=int( vote[0].getText().replace(' points',''))
            if point>99:
                hackernews.append({'Name':title,'webaddress':hyperlink,'votes':point})
    return sort_dict( hackernews)


pprint.pprint(custom_hackerrank(links,subtext))
