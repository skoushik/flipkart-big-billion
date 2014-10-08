from bs4 import BeautifulSoup
import urllib2
import webbrowser
import time

 
def cheat():
    url = "http://www.flipkart.com"
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    offers = []
    link = []
    link_update = []
    discount = []
    rank = soup.findAll("div", {"class":"pu-offer fk-capitalize fk-font-17 fk-bold"})
    for i in rank:
    #  offers.append('\n'.join(i.contents).strip('\n\t\t\t\t'))
      if '%' in i.text:
        offers.append(i.text)
        link.append(i.parent.attrs['href'])
       
    for j in xrange(len(offers)):
        discount.append(int(offers[j].split()[1].rstrip("%")))
        link_update.append(link[j])
    new_url = []
    for i in link_update:
      new_url.append(url + i)
    z = zip(discount,new_url)
    z.sort(reverse=True)
    return z

opened = []
discount = []
while True:
    new_url = cheat()
    for i in new_url:
        if i[0] >= 70 and not i[1] in opened:
            opened.append(i[1])
            discount.append(i[0])
            webbrowser.open_new_tab(i[1])

    time.sleep(5)