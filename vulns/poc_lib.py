from pwn import *
from string import*
import requests

SERVER = "http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt"
LOGIN = '/login'
REGISTER = '/register'
FRIENDS = '/friends'
PENDING_REQUESTS = '/pending_requests'
ADD_A_FRIEND = '/request_friend'
NEW_POST = '/create_post'
PROFILE = '/profile'
LOGOUT = '/logout'
RESET = '/init'

cookie = {}

def reset():
	r = requests.get(SERVER + RESET)
	return r

def register(user, passwd):
	auth = {'username' : user, 'password' : passwd}
	r = requests.post(SERVER + REGISTER, data = auth)
	return r

def login(user, passwd):
	auth = {'username' : user, 'password' : passwd}
	r = requests.post(SERVER + LOGIN, data = auth)
	cookie = r.cookies
	return r

def logout():
	r = requests.post(SERVER + LOGOUT, cookies = cookie)	
	return r

def add_friend(payload):
	r = requests.post(SERVER + ADD_A_FRIEND, cookies = cookie, data = payload)
	return r

def create_post(payload):
	r = requests.post(SERVER + NEW_POST, cookies = cookie, data = payload)
	return r

def update_profile(payload):
	r = requests.post(SERVER + PROFILE, cookies = cookie, data = payload)
	return r

