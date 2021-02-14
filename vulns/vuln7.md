# Vulnerability 7: Blind SQL Injection in Add a Friend allows to obtain the database

- Vulnerability: Blind SQL Injection
- Where: Add a Friend
- Impact: Allows the the attacker to obtain information about the database structure and content

## Steps to reproduce (Get table name Users)

1. Login with any account (create one if necessary) 
2. Access 'Add a Friend'
3. Insert the query on the input space: aaa' UNION SELECT 1,2,3,4,5 FROM information_schema.columns WHERE table_name LIKE '***%'#
4. Change the *** and test the server response
5. If the server return a status code 500 if the query is successful and status code 200 if the query fails
6. Build the table_name

[(POC)](vuln7.py)