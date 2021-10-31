## 5-Open Redirection
### How to reproduce :
in the footer there are links that redirect to social networks
`http://10.11.100.7/index.php?page=redirect&site=facebook`
we can change the link to redirect to our chosen website
`http://10.11.100.7/index.php?page=redirect&site=trojan.xxx`
and the user will think he is accessing the original website, but will be redirected to another link, that can be used to steal his credentials or download some malware
### How to Fix :
Never take the redirection URL from GET parameters, or warn the users that they will be leaving the site. or list the redirections in your backend.