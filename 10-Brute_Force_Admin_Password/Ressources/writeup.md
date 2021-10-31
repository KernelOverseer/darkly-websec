## 10-Brute Force Admin Password
### How to reproduce :
We notice that they use a GET request in the login
`http://10.11.100.7/index.php?page=signin&username=zamazzal&password=biri&Login=Login#`
and its easy to brutforce so we BruteForce by using our script and wordlist.txt
### How to Fix :
Use strong passwords, and never use GET request in authentication and set a limit of tries and ban user if you pass the number of tries, or make them solve a captcha.