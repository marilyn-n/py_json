import json

with open('todos.json', 'r') as todos:
  data = json.load(todos)

  count = 0
  countFalse = 0 

  for item in data:
    if item['completed']:
      count += 1 

    if not item['completed']:
      countFalse += 1

  print('Falsos:', countFalse, 'verdaderos', count)
      