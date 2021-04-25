import requests
import spacy
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

topic = input("enter your topic: ")
numResults = 100

url = "https://www.google.com/search?q=" + topic + "&hl=en&sxsrf=ALeKk03aYY67dkoHBhbg6SMxoBE4uRONwA:1619158608650&source=lnms&sa=X&ved=0ahUKEwjUjtDt25PwAhXowzgGHSneBn8Q_AUIDigA&biw=1920&bih=909&dpr=" + str(
    numResults)

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
results = soup.find_all('div', attrs={'class': 'ZINbbc'})
descriptions = []
for result in results:
    try:
        description = result.find('div', attrs={'class': 's3v9rd'}).get_text()
        if description != '':
            descriptions.append(description)
    except:
        continue
text = ''.join(descriptions)

sp = spacy.load('en_core_web_sm')
doc = sp(text)
newText = ''

# for word in doc:
#     if word.pos_ in ['ADJ', 'NOUN']:
#         newText = " ".join((newText, word.text.lower()))

newText = " ".join((newText, text.lower()))

color = input("enter background color: ")
wordcloud = WordCloud(stopwords=STOPWORDS,
                      background_color=color,
                      max_words=2000, max_font_size=256,
                      random_state=42, width=1500,
                      height=1500, colormap='Set2', collocations=False).generate(newText)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
