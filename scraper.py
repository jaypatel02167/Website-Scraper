from bs4 import BeautifulSoup
import requests
import pandas as pd

def main():

    content = requests.get('http://quotes.toscrape.com/').content
    quotes_soup = BeautifulSoup(content, features="html.parser")

    quotes_tags = quotes_soup.find_all('span', class_ ='text')
    #print(quotes_tags)
    quotes = [tag.text[1:-1] for tag in quotes_tags]
    #print(quotes)
    

    quotes_author = quotes_soup.find_all('small', class_='author')
    #print(quotes_author)
    authors = [tag.text for tag in quotes_author]
    #print(authors)
    #print('')

    # Converting lists of tuples into
    # pandas Dataframe.
    df = pd.DataFrame((zip(quotes, authors)), columns=['Quotes', 'Authors'])

    # Print data.
    print(df)
    
    df.to_csv(r'D:\Coding Projects\Practice Programs\Website Scrapper\results.csv', index = None, header=True)

    #print("Authors: " , (len(authors)))
    #print("Quotes: " , (len(quotes)))

if __name__ == "__main__":
    main()
