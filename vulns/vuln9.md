# Vulnerability 9: HTML Injection in post

- Vulnerability: HTML Injection
- Where: New and Edit Post
- Impact: Allows the attacker to inject HTML in the website

## Steps to reproduce

1. Login with any account (create one if necessary)
2. Access 'New post'
3. Insert the following script in the post's content: [(script)](htmli.txt)
4. Create the post
5. A post with a button will be created

[(PoC)](vuln9.py)