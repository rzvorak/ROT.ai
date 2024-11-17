
from bs4 import BeautifulSoup
import requests



# Function to fetch pronunciation from Wiktionary
def get_pronunciation_score(word):
    phonemePrev = {
  "ə" : 7.3, "n" : 6.72, "t" : 5.78, "l" : 5.15, "s" : 4.61, "r" : 3.87, "i" : 3.69,
  "ɪ" : 3.64, "d" : 3.33, "ɛ" : 3.21, "ð" : 3.14, "k" : 3.10, "m" : 2.99, "aɪ" : 2.97, "w" : 2.77, "z" : 2.75,
  "æ" : 2.25, "b" : 1.9, "o" : 1.85, "p" : 1.79, "v" : 1.74, "e" : 1.57, "f" : 1.55, "ʌ" : 1.46,"ɑ" : 1.43, 
  "h" : 1.31, "g" : 1.18, "u" : 1.13, "y" : 1.09, "ŋ" : 1.08, "ɾ" : 1.03, "ɔ" : 0.77, "u" : 0.76, "θ" : 0.7
    }
    # URL of the word on Wiktionary
    url = f'https://en.wiktionary.org/wiki/' + word

    # Send a GET request to fetch the page content
    response = requests.get(url)

    if response.status_code != 200:
        return "Error: Unable to retrieve data"

    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the pronunciation section in the HTML (it is typically under <span class="ipa"> for IPA transcriptions)
    pronunciation = None
    usPronounce = soup.find('a', href='https://en.wikipedia.org/wiki/American_English')
    ipa_section = usPronounce.find_next('span', class_='IPA')

    if ipa_section:
            pronunciation = ipa_section.get_text()

    if pronunciation:
        return pronunciation
    else:
        return "Pronunciation not found"
    
def prevalenceScore(ipa):
     phonemePrev = {
    "ə" : 7.3, "n" : 6.72, "t" : 5.78, "l" : 5.15, "s" : 4.61, "r" : 3.87, "i" : 3.69,
    "ɪ" : 3.64, "d" : 3.33, "ɛ" : 3.21, "ð" : 3.14, "k" : 3.10, "m" : 2.99, "aɪ" : 2.97, "w" : 2.77, "z" : 2.75,
    "æ" : 2.25, "b" : 1.9, "o" : 1.85, "p" : 1.79, "v" : 1.74, "e" : 1.57, "f" : 1.55, "ʌ" : 1.46,"ɑ" : 1.43, 
    "h" : 1.31, "g" : 1.18, "u" : 1.13, "y" : 1.09, "ŋ" : 1.08, "ɾ" : 1.03, "ɔ" : 0.77, "u" : 0.76, "θ" : 0.7
        }
     normed = 0
     preval = 0
     currPreval = 0
     if (ipa ==  "Pronunciation not found"):
          return 0
     for i in range(len(ipa)):
          currPreval = phonemePrev.get(ipa[i])
          if (currPreval == None):
               currPreval = -1
          preval = preval + currPreval
     normed = preval / len(ipa)
     return normed
