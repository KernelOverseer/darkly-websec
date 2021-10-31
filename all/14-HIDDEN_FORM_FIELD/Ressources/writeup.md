## 14- Hidden Form Field
### How to reproduce :
On the login page, we see a recover password page,
usually a recover password has a field to input your username or email
so when we inspect the form
we see a hidden field with the value `webmaster@borntosec.com`
When we change it to our email, and submit, we get the flag
### How to Fix :
Exposing an administrator email is a bad idea, as you gave up half the credentials, a hacker will only have to bruteforce the password, and not both username and password, making it easier.
Or he can flood the email address with spam emails.
The use of hidden fields is generally bad if the goal was hiding sensitive data.
It would be prefered if the email address was saved on the backend.
