import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = 'https://scrapebook22.appspot.com/'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response) #BS is for the file and BeautifulSoup is a name of a class within the file
    # print soup.head #prints only whats inside the headtag of the doc
    print soup.title  #  returns <title>Scrapebook | by SmartNinja</title>
    print soup.title.string   # returns  Scrapebook | by SmartNinja

    links = soup.findAll("a")
    for link in links:
        print link
