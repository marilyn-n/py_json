import json

# lista de categorias

with open('winter.json', 'r') as winter:
  animes = json.load(winter)

def allCategories ():
  for item in animes['season']:
    for i in item['genre']:
      print(i['name'])
      
allCategories()

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

# def minScore ():
#   for m in animes['season']:
#     print(m['score'])
# minScore()    




# agrupar por num de episodios 
  # episodes

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
      
print('------------------------------------------------')