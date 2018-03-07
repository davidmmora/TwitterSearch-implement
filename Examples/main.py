
#este es el primer ejercicio

"""
import requests

if __name__ == '__main__':
	url= 'https://www.google.com.mx'
	response = requests.get(url)

	if response.status_code == 200:
		print(response.content)
		content = response.content
		file = open('google.html', 'wb')
		file.write(content)
		file.close
"""

#aqui inicia el segundo ejercicio
"""
import requests
import json

if __name__ == '__main__':
	# url = 'http://httpbin.org/get?nombre=david&curso=python'
	# url = 'http://httpbin.org/get'
	url = 'http://httpbin.org/post'
	args = { 'nombre': 'David', 'curso': 'python', 'nivel' : 'intermedio' } 
	
	# response = requests.get(url, params=args)
	response = requests.post(url, params=args)
	print(response.url)

	if response.status_code == 200:
		#primer forma de consumir json
		
		# content = response.content
		# print(content)

		# response_json = response.json()
		# origin = response_json['origin']
		# print(origin)
		
		#segunda forma de consumir json
		response_json = json.loads(response.text)
		origin = response_json['origin']
		print(origin)
"""

#tercer ejercicio post

"""
import requests
import json

if __name__ == '__main__':
	url = 'http://httpbin.org/post'
	payload = { 'nombre': 'David', 'curso': 'python', 'nivel' : 'intermedio' }
	headers = {'Content-Type':'application/json' , 'access-token': '12345'}
	
	# response = requests.post(url, json=payload)
	response = requests.post(url, data=json.dumps(payload), headers=headers)
	print(response.url)

	if response.status_code == 200:
		# print(response.content)
		headers_response = response.headers
		# print(headers_response)
		server = headers_response['Server']
		print(server)

"""

# cuarto ejercicio manejo de archivos pesados

"""
import requests
import json

if __name__ == '__main__':
	url =  'http://david.devsschool.com/assets/images/myphoto.jpg'

	response = requests.get(url, stream=True) # realiza la peticion sin descargar el contenido
	with open('myphoto.jpg', 'wb') as file:
		for chunk in response.iter_content(): # descarga el contenido poco a poco
			file.write(chunk)

	response.close()

"""

import requests
if __name__ == '__main__':
	url= ''