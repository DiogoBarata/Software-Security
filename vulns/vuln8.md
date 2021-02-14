# Vulnerability 8: CSRF with new post

- Vulnerability: CSRF
- Where: New and Edit Post
- Impact: Allows the attacker to redirect traffic to a malicious website

## Steps to reproduce

1. Login with any account (create one if necessary)
2. Access 'New post'
3. Insert the following script in the post's content: [(script)](htmli.txt)
4. Create the post
5. A post with a button will be created, which will try to trick a user into clicking it
6. If a user click it, the user will be redirected to the malicious page
7. When the presses the button a new post will be created with his authorship, saying "I'was hacked"

## Notes
We weren't able to produce a full PoC for this vulnerability because we couldn't find a way to emulate a user clicking a button on the malicious webpage.
For that reason we decided to provide screenshots of the vulnerability happening to let the teacher know that the vulnerability exists.

[(Semi_PoC)](vuln9.py) Check that the script was successfully added to the server (same as HTML Injection)  

[(Image1)](Image1.png) FaceFive webpage with the injected html

[(Image2)](Image2.png) Malicious website accessed by the button

[(Image3)](Image3.png) Post created after clicking the "Continue to FaceFive" button

[(MaliciousWebsiteHTML)](csrf.html)