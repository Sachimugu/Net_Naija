### Importing all relevant libraries

import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm_notebook

#function to load a url and parse it content
def browse(url): #browse function
    page= requests.get(url) #to load a url
    soup= BeautifulSoup(page.content, 'lxml') # parse it content
    return soup


#function to get the next page link
def nextpage(soup): #nextpage function
    try:
        nxtpage=soup.find('a', class_="next page-numbers", href=True)['href']
        return nxtpage #return the page link
    except:
        return #return nothing if at the last page

#gets last page
url="https://www.thenetnaija.com/videos/movies"
soup=browse(url) 
x= int(soup.find('ul', class_='pagination').text[7:-1])-1

## Loop to get link of all pages
#Base url
url="https://www.thenetnaija.com/videos/movies" #open on your browser to get a feel of the site architecture

page_link=[] # empty list to store list of all pages

for i in tqdm_notebook(range(x), desc= 'Loading....'):
    soup=browse(url) # load the base url
    url=nextpage(soup)# get next page on base url append it to page list and become the new base url
    if not url:
        break
    page_link.append(url)
    
print(f'The total number of pages: {len(page_link)}')
    
##Loop to get the links to all movies on each page
movie_links=[] # empty list to store movie links form each page
for page in tqdm_notebook(page_link, desc='Loading...'): # a for loop to get each page from the page list
    soup= browse(page) # load each page and parse
    
    # this series of code get all link to movies on each page and append it to movie_links
    video_files=soup.find("div", class_="video-files")
    class_info=video_files.findAll("div", class_="info")
    for x in class_info:
        link=x.find("a", href=True)['href']
        movie_links.append(link)

##Empty list to store data we need about each movie   
titles = []
movie_linkss = []
movie_types = []
time_of_uplos = []
movie_lengths = []
num_of_comments = []
mo_summarys = []
Genres = []
Release_Dates = []
Starss = []
Languages = []
Subtitles = []
imdb_links = []

#Getting data about each movie

for link in tqdm_notebook(movie_links, desc='Loading'):
    soup= browse(link) # browse movie link and parse
    
    #This series of code get the requried data and append to the data list
    try:
        title=soup.find('h1', class_="page-h1").text 
        titles.append(title)
    except:
        titles.append(' ')
    post_meta=soup.find("div", class_="post-meta")
    try:
        movie_link=post_meta.find('a', href=True)['href']
        movie_linkss.append(movie_link)
    except:
        movie_links.append(' ')
    meta_one=soup.findAll('span', class_='meta-one')
    try:
        movie_type=meta_one[0].text.split()
        movie_types.append(movie_type)
    except:
        movie_types.append(' ')
    x=meta_one[1].text.split()
    try:
        time_of_uplo=' '.join(x)
        time_of_uplos.append(time_of_uplo)
    except:
        time_of_uplos.append(' ')
    try:
        movie_length=meta_one[2].text.split()
        movie_lengths.append(movie_length)
    except:
        movie_lengths.append(' ')
    try:
        num_of_comment=meta_one[3].text.split()
        num_of_comments.append(num_of_comment)
    except:
        num_of_comments.append('0')
    try:
        mo_summary=soup.find('p').next_element
        mo_summarys.append(mo_summary)
    except:
        mo_summarys.append(' ')
    try:
        block=soup.find('blockquote', class_='quote-content')
        y=block.findAll('p')
        
        try:
            Genre=y[1].text.split(':')[1:]
            Genres.append(Genre)
        except:
            Genres.append('missing')
        try:
            Release_Date=y[2].text
            Release_Dates.append(Release_Date)
        except:
            Release_Dates.append('missing')

        try:
            Stars=y[3].text.split(':')[1:]
            Starss.append(Stars)
        except:
            Starss.append('missing')

        try:
            Language=y[5].text.split(':')[1:]
            Languages.append(Language)
        except:
              Languages.append('missing')
        try:
            Subtitle=y[6].text.split(':')[1:]
            Subtitles.append(Subtitle)
        except:
            Subtitles.append('missing')

    except:
        Genres.append('missing')
        Release_Dates.append('missing')
        Starss.append('missing')
        Languages.append('missing')
        Subtitles.append('missing')
            
   
    try:
        imdb_link=block.find('a', href=True)['href']
        imdb_links.append(imdb_link)
    except:
         imdb_links.append('missing')

#Creating a table of all data with pandas dataframe
df=pd.DataFrame({"titles":titles,       
              "movie_types":movie_types,
              "time_of_uplos":time_of_uplos,
              "movie_lengths":movie_lengths,
              "num_of_comments":num_of_comments,
              "Genres":Genres,
              "Release_Dates":Release_Dates,
              "Starss":Starss,
              "Languages":Languages,
              "Subtitles":Subtitles,
              "movie_linkss":movie_linkss,  
              "imdb_links":imdb_links,
              "mo_summarys":mo_summarys,   
             })


#save data in cvs format
df.to_csv('./Datanetnaija_movie.csv')
        
