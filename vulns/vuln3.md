# Vulnerability 3: SQL Injection in login to gain access to user account

- Vulnerability: SQL Injection
- Where: Username in Login form
- Impact: Allows access to any created account	

## Steps to reproduce
	
1. Acess `Login`
2. Insert query in `Username`: `validUsername' OR '1'='1 ;--` 
3. Insert any word in `Password`
4. Acess profile

[(POC)](vuln3.py)



