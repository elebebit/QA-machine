import json

test={'Q5':'5Do you have a dog?'}

js=json.dumps(test)
with open('5.json','w') as jsf:
	jsf.write(js)