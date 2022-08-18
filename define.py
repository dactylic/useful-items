import requests
requests.packages.urllib3.disable_warnings()
import sys
import keys

args = len(sys.argv)
if args > 2:
    raise SyntaxError('Please provide only one word.')

def dict_check(word: str) -> str:
    word = sys.argv[1]
    req = requests.get(f'https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={keys.keys}')
    json_data = req.json()
    shortdef = json_data[0]['shortdef']
    for index, word_defs in enumerate(shortdef):
        print(f'Definition {index} for {word} is: {word_defs}')
    

dict_check(sys.argv[1])

