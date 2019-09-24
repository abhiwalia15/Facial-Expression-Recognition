# Python3 code for movie 
# recommendation based on 
# emotion 
  
# Import library for web 
# scrapping 
from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 
  
# Main Function for scraping 
def main(emotion): 

    # IMDb Url for Drama genre of 
    # movie against emotion Sad 
    if(emotion == "Sad" or emotion == "sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Musical genre of 
    # movie against emotion Disgust 
    elif(emotion == "Disgust" or emotion == "disgust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Family genre of 
    # movie against emotion Anger 
    elif(emotion == "Anger" or emotion == "anger"): 
        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Thriller genre of 
    # movie against emotion Anticipation 
    elif(emotion == "Anticipation" or emotion == "anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
  # IMDb Url for Sport genre of 
    # movie against emotion Fear 
    elif(emotion == "Fear" or emotion == "fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Thriller genre of 
    # movie against emotion Enjoyment 
    elif(emotion == "Enjoyment" or emotion == "enjoyment"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Western genre of 
    # movie against emotion Trust 
    elif(emotion == "Trust" or emotion == "trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
  
    # IMDb Url for Film_noir genre of 
    # movie against emotion Surprise 
    elif(emotion == "Surprise" or emotion == "surprise"): 
        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'
  
    # HTTP request to get the data of 
    # the whole page 
    response = HTTP.get(urlhere) 
    data = response.text 
  
    # Parsing the data using 
    # BeautifulSoup 
    soup = SOUP(data, "lxml") 
  
    # Extract movie titles from the 
    # data using regex 
    b = soup.find_all('h3',{'class':'lister-item-header'})
    #c = b.findAll()

    return b
    # title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}) 
    # return title 

    # Driver Function 
if __name__ == '__main__': 
    

    print("What is your mood right now shitbag:\n")
    print('************************************')
    print("1.Sad\n2.Disgust\n3.Anger\n4.Anticipation\n5.Fear\n6.Enjoyment\n7.Trust\n8.Surprise")
    emotion = input("Enter the emotion: ") 
    a = main(emotion)
    for c in a:
        print(c.find_all('a')[0].text)
    #print(a[:10])  

    # containers=a.findAll('h3')
    # print(containers)
    
    









    # count = 0
  
    # if(emotion == "Disgust" or emotion == "Anger"
    #                        or emotion=="Surprise"): 
  
    #     for i in a: 
  
    #         # Splitting each line of the 
    #         # IMDb data to scrape movies 
    #         tmp = str(i).split('>;') 
            
    #         #print(tmp)
    #         if(len(tmp) == 3):
    #             print("error") 
    #             print(tmp[1][:-3]) 
  
    #         if(count > 13): 
    #             break
    #         count += 1
    # else: 
    #     for i in a: 
    #         tmp = str(i).split('>') 
    #         print(tmp)
    #         if(len(tmp) == 3):

    #             print('Error')
    #             print(tmp[1][:-3]) 
  
    #         if(count > 11): 
    #             break
    #         count+=1