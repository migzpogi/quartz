import requests
from lxml import etree


def scrape_stub():
    return 1


def foo():
    url = 'https://www.basketball-reference.com/teams/LAL/2025_games.html'
    page = requests.get(url)
    print(page.status_code)
    text = page.text

    tree = etree.HTML(text)


    for i in range(1, 87):
        gamenumber = tree.xpath(f'//*[@id="games"]/tbody/tr[{i}]/th')[0].text


        if gamenumber.isdigit():

            dategame = tree.xpath(f'//*[@id="games"]/tbody/tr[{i}]/td[1]/a')[0]
            humandate = dategame.text
            iso = dategame.attrib['href']



            result = tree.xpath(f'//*[@id="games"]/tbody/tr[{i}]/td[7]')[0].text

            if result:
                print(f'{gamenumber} - {humandate} - {result}')
            else:
                print(f'{gamenumber} - {humandate} - P')





if __name__ == '__main__':
    foo()