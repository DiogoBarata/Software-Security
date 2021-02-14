# Vulnerability 1: SQL Injection in search friends allows to obtain information from the database

- Vulnerability: SQL Injection
- Where: search in My Friends form
- Impact: Allows access to all information in the database

## Steps to reproduce (Obtain ssofadmin's password)
	
1. Login with any account
2. Access `My Friends`
3. Insert query : `' and 1=0 UNION SELECT 1,1,password,1,1 FROM Users WHERE username like 'ssofadmin' -- `
4. Obtain password from the field `Found`

## Note 

The password is stored in plaintext wich is also a vulnerability

[(POC)](vuln1.py)
