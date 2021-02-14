
# Vulnerability 2: SQL Injection in login allows to obtain the Database through the multiple endpoints

- Vulnerability: SQL Injection
- Where: login form, register form, profile, new and edited posts, myfriends
- Impact: Allows the the attacker to obtain information about the database structure and content

## Steps to reproduce

1. Insert query in any of the vulnerable forms : 'or extractvalue(1,concat(0x7e,database())) or'
2. Read from the error screen

[(POC)](vul2.py)