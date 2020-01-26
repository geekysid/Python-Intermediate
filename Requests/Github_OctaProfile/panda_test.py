
import pandas as pd
from collections import Counter
# import matplotlib.pyplot as plt

language_chart_data = [
                        {'language': 'JavaScript', 'count': 1}, 
                        {'language': 'Python', 'count': 4}, 
                        {'language': 'Jupyter Notebook', 'count': 1}
                        ]

starsPerRepo_chart_data = [
                            {'repo': 'Django-Projects', 'starCount': 1}, 
                            {'repo': 'Hackerrank-Solutions', 'starCount': 1}, 
                            {'repo': 'Pandas', 'starCount': 1}, 
                            {'repo': 'Python-Basics', 'starCount': 1}, 
                            {'repo': 'Python-Intermediate', 'starCount': 1}, 
                            {'repo': 'Python-Projects', 'starCount': 1}
                            ]

starsPerLanguage_chart_data = [{'language': 'JavaScript', 'starCount': 1}, {'language': 'Python', 'starCount': 4}, {'language': 'Jupyter Notebook', 'starCount': 1}]


df = pd.DataFrame(language_chart_data)
df2 = pd.DataFrame(starsPerRepo_chart_data)
df3 = pd.DataFrame(starsPerLanguage_chart_data)

df.plot(kind='bar', x='language', y='age')


language = df['language'].tolist()
print(language)

language_count = Counter()

for lang in language:
    language_count.update(lang.split('`'))

print()
for item in language_count.most_common():
    print(item[0], item[1])



# print()
# print(df)
# print()
# print(df2)
# print()
# print(df3)
# print()