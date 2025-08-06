import json

with open("example.json") as f:
  data=json.load(f)

for state in data['states']:
  del state['area_codes']

with open('new_states.json','w') as f:
  json.dump(data,f,indent=2)