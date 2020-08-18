import re
import urllib
import json
import numpy.random as rd

# This is still hard censoring. Only for n-word, includes the hard-r variant.
# Replaces them with random animal names from this gist:
# https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a

# https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script

animal_json_link = 'https://gist.githubusercontent.com/borlaym/585e2e09dd6abd9b0d0a/raw/6e46db8f5c27cb18fd1dfa50c7c921a0fbacbad0/animals.json'
default_data = [
    'ABSOLUTELY NO N-WORDS ALLOWED',
    'Man that R is sure hard',
    'You\'re going to get me demonetized',
    'STOP ADDING N-WORD TO THE LIST REEEE'
]

def fetch_animal() -> list:
    try:
        url = urllib.request.urlopen(animal_json_link)
        animal_data = json.loads(url.read().decode())
        return animal_data
    except:
        print("ERROR! COULD'NT GET THE ANIMAL DATA!")
        return default_data
    return default_data

animal_data = fetch_animal()

regex_finder = '[Nn][Ii][Gg][Gg](a|er|A|Er|eR|ER)'

def censor(word) -> str:
    out = word[:]
    matches = [i for i in re.finditer(regex_finder, out)]
    for match in reversed(matches):
        replacement = rd.choice(animal_data)
        out = out[:match.start()]+replacement+out[match.end():]
    return out