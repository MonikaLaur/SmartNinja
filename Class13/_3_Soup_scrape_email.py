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
        email = subsoup.findAll("span", attrs={"class":"email"})[0].string
        gender = subsoup.findAll("span", attrs={"data-gender": True})[0].string
        city = subsoup.findAll("span", attrs={"data-city": True})[0].string
        print "Email: %s ; Gender: %s ; City: %s " % (email, gender, city)
        # print "email: {}, gender: {}, city: {}".format(email,gender,city) # doesnt work on py 2.6.
