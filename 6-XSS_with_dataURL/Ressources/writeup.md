## 6- XSS with dataURL
### How to reproduce :
if we click to nsa image on the home page
we get redirected to this page
`http://10.11.100.7/?page=media&src=nsa`
we can pass any data by using dataurl and it will be taked as source of the img
so we can pass any java script code in to many differnt format
the best way is encode as base64
`http://10.11.100.7/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgndGVzdCcpPC9zY3JpcHQ+`
and we get the flag.
### How to Fix :
We must not expose the src from user in GET request if necessary we can Escape Dynamic Content or add some Whitelist Values