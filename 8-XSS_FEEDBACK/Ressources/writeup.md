## 8- XSS FEEDBACK
### How to reproduce :
We see on the feedback page that name and comment that you submit will be displayed.
So we think about imbedding javascript code, in the message so it will be executed whenever someone
opens that page.
so we send `<body onload="alert(1)"/>a` in the comment field
and we get our flag.
(and we found a bug, when you just enter a, you get the flag).
### How to Fix :
Escape Dynamic Content or add some Whitelist Values.
Some advanced solutions for XSS require running code in a sandbox, to detect javascript code.