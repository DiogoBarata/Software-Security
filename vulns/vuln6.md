# Vulnerability 6: SQL Injection in edit post allows to change a post from another user
- Vulnerability: SQL Injection
- Where: content in Edit Post
- Impact: Changes a post from another user

## Steps to reproduce (Change administrator's post)
	
1. Login with any account
2. Access `New Post`
3. Create Post
4. Access `Edit Post`
5. Insert query : `teste', type = 'Public', author = 'teste1' where id = 1 -- `
4. Post changed

[(POC)](vuln6.py)
