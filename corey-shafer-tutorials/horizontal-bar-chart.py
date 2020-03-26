import csv 
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

# plot graph from csv file
language_counter = Counter()
# with open('./data.csv','r') as filein:
#     csv_reader = csv.DictReader(filein)
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))

data = pd.read_csv('./data-horizontal-bar.csv')
ids = data['Responder_id']
languages_response = data['LanguagesWorkedWith']

for response in languages_response:
    language_counter.update(response.split(';'))

languages = []
popularity = []

for items in language_counter.most_common(15):
    languages.append(items[0])
    popularity.append(items[1])

languages.reverse()
popularity.reverse()

plt.barh(languages,popularity)
plt.title('Languages Popularity')
# plt.ylabel('Language')
plt.xlabel('Popularity')

plt.tight_layout()

plt.savefig('lang-popularity.png')

plt.show()