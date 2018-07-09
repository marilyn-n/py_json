import json

with open('winter.json', 'r') as winter:
  data = json.load(winter)
  # print(data)

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

# Calificacion mas alta
# mas baja
# agrupar por num de episodios 
# lista de categorias



