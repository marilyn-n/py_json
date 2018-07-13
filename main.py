import json

with open('winter.json', 'r') as winter:
  season = json.load(winter)

def allCategories ():
  allCat = []
  animes = season['season']
  for anime in animes:
    for genre in anime['genre']:
      if not genre['name'] in allCat:
        allCat.append(genre['name'])
  return allCat

print(allCategories())
print('Total of Anime Categories: ' + str(len(allCategories())))
# --------------------------------------

from collections import Counter

def series ():
  episodes = []
  totalSeries = []
  animes = season['season']

  for anime in animes:
    if not ((anime['episodes'] == None) or (anime['episodes'] in episodes)):
      episodes.append(anime['episodes'])
    if (len(anime) == ((len(episodes)))):
      totalSeries.append(animes)
      print('--------')
      print('Hay ' + str(len(totalSeries)) + ' animes de ' + str(anime['episodes']) + ' episodios')
  
  return episodes, totalSeries

series()

# ---------------
# 1 episodios: 1 animes
# 2 episodios: 0 animes
# 3 episodios: 0 animes
# 4 episodios: 2 animes
# 5 episodios: 0 animes
# hay 3 animes de 10 episodios


with open('winter.json', 'r') as winter:
  animes = json.load(winter)


# Calificacion mas alta
  # max_score and min_score
def maxScore ():
  scores = []
  for i in animes['season']:
      if not i['score'] == None:
        scores.append(i['score'])
  return scores

print('Maximum score is: ', end='')    
print(max(maxScore()) )
print('Minimum score is: ', end='')
print(min(maxScore()) )

with open('todos.json', 'r') as todos:
  data = json.load(todos)

  completed = 0
  incompleted = 0 

  for item in data:
    if item['completed']:
      completed += 1 

    if not item['completed']:
      incompleted += 1
      
print('Incompleated:', incompleted, 'Compleated:', completed)
      
print('---------------------------------------------')



