import urllib2
import BeautifulSoup as BS

if __name__ == '__main__':
    url = 'https://scrapebook22.appspot.com'
    response = urllib2.urlopen(url).read()
    soup = BS.BeautifulSoup(response) #BS is for the file and BeautifulSoup is a name of a class within the file

    links = soup.table.findAll("a")
    for link in links:
        subpage_link = url + link["href"]
        subpage_response = urllib2.urlopen(subpage_link).read()
        subsoup = BS.BeautifulSoup(subpage_response)
        print subsoup.findAll("h1")[1].string # without [1] we would get a list with 2 h1, [1] takes the second one.

