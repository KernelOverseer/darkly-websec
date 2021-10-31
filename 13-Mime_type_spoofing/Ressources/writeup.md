## 13- MIME type spoofing
### How to reproduce :
The image upload page expects an image to be uploaded.
but we can see if we can upload a php script
since we know uploaded images will be stored at `/images`
we expect our shell to be accessible at `/images/shell.php`
and will give us access to a shell
so first, we need to upload this `php` file while making the backend think this is an image
so we use the following curl command:
```BASH
curl \
  -F "MAX_FILE_SIZE=100000" \
  -F "uploaded=@/tmp/shell.php;type=image/jpeg" \
  -F "Upload=true" \
  -X POST \
  "http://10.11.100.253/?page=upload" | grep flag
```
and the backend trusts the `MIME` type we provided and uploads it.
and then we get a flag.
### How to Fix :
Trusting the `MIME` type provided by the user is a bad idea.
you can at least check the file extension `.php`, but an improved way is to used a utility that can
detect the type of a file, like the `file` utility in linux.
```
$ file /tmp/shell.php
/tmp/shell.php: PHP script text, ASCII text
```
