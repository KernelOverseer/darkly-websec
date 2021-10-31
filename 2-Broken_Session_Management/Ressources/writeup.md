## 2- Broken Session Management
### How to reproduce :
When browsing cookies in the application tab on the developer console, you will notice a cookie `I_am_admin`, that has content `false` hashed in md5, we replace it with `true` hashed in md5, and we get admin privilege. 
### How to Fix :
Use jwt or another secure auth, and never put sensitive data in cookies