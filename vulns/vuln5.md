# Vulnerability 5: IDOR in edit post

- Vulnerability: IDOR
- Where: Edit post
- Impact: Allows the attacker to access other user's posts and also to edit them

## Steps to reproduce
	
1. Login with any account (create one if necessary)
2. Access 'New post' and create a post
3. On the main page, select 'Edit this post'
4. The url: http://34ead85a967c3a29f1f3d306c40d31e50f45c0adc2ef24f9f20babfa4e40.project.ssof.rnl.tecnico.ulisboa.pt/edit_post?id=X
5. Change the X for a valid id starting on 1 and press Enter
6. Access gained to post X with the ability to edit it

## Notes

This vulnerability also proves that the server is vulnerable to Broken Access Control because it allows us to access/change another user post which we should not have the permissions to

[(POC)](vuln5.py)