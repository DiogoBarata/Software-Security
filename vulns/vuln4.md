# Vulnerability 4: Stored XSS in new post produces a DoS attack

- Vulnerability: Stored XSS
- Where: New and Edit post, edit profile's name and picture
- Impact: Allows the attacker to store a DoS attack on the database

## Steps to reproduce
	
1. Login with any account (create one if necessary)
2. Access `New post`
3. Insert the following script in the post's content : `<script>`document.location="https://www.youtube.com/watch?v=dQw4w9WgXcQ" `</script>`
4. Create the post
5. Everytime the main page is accessed, it will be redirected to https://www.youtube.com/watch?v=dQw4w9WgXcQ 

[(POC)](vuln4.py)