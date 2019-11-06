import requests
from parsel import Selector

def s(query,conferences=["icml","iclr","nips"],years=[2017,2018,2019,2020]):
    count=0
    for year in years:
        print_year=True
        for conference in conferences:
            url="https://"+conference+".cc/Conferences/"+str(year)+"/Schedule?q="+query.strip().replace(' ','+')+"&type=Poster"
            #url="https://nips.cc/Conferences/2019/Schedule?q=meta+reinforcement+learning&type=Poster"
            #url="https://icml.cc/Conferences/2018/Schedule?type=Poster"
            ret=requests.get(url)
            sel=Selector(ret.text)
            
            title=sel.xpath('//div[@class="maincardBody"]/text()').getall()
            author=sel.xpath('//div[@class="maincardFooter"]/text()').getall()
            
            if len(title)>0:
                if(print_year):
                    print('\033[1;31m{:^100}\033[0m'.format(year))
                    print_year=False
                print('\033[1;32m{}\033[0m'.format(conference.upper()))
                for t,a in zip(title,author):
                    count+=1
                    print('{}. \033[1m{}\033[0m.  {}'.format(count,t,a.replace(' · ',', ')))
                print("\n")
while True:
    q=input()
    s(q)
    print("\033[1;31;46m{:^100}\033[0m\n".format("Type to Search More"))
