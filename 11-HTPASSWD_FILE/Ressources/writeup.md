## 11-HTPASSWD FILE
### How to reproduce :
After using dirsearch to search for the directroys and files in the url
`python3 dirsearch.py -u http://10.11.100.7/`
and we found this paths:
`http://10.11.100.7/robots.txt`
and
`http://10.11.100.7/admin`
and inside robots.txt we found a htpasswd
and inside it we found a password for root user
we decrypt it and we found the password of the user root in admin `http://10.11.100.7/admin`
and we get the flag
### How to Fix :
never store passwords in files
and It is better to use a router, than use the default apache or nginx, so you can avoid giving access to unwanted files.