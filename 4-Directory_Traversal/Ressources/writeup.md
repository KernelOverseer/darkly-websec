## 4-Directory Traversal
### How to reproduce :
In a page like the survey page : `http://10.11.100.7/index.php?page=survey`
`index.php` takes a GET argument page, and loads the corresponding file,
so that means we can give it any file and it should be able to read it.
so for example we can access `/etc/passwd` using the URL
`http://10.11.100.7/index.php?page=../../../../../../../../../etc/passwd`
### How to Fix :
Never take an input passed by user without verifying it, or specify the paths in a lookup table that the user can't modify.