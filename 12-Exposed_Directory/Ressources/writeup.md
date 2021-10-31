## 12- Exposed Directory
### How to reproduce :
When taking a look at `/robots.txt` we can find some directories
```
User-agent: *
Disallow: /whatever
Disallow: /.hidden
```
when browsing the `/.hidden` directory we find a lot of nested folders
we wrote a script to browse them in a `DFS` order.
then we print all the files.
we find a flag.
```
~/Desktop/darkly❯ python3 hidden.py

Demande à ton voisin de gauche
Non ce n'est toujours pas bon ...
Demande à ton voisin du dessous
Demande à ton voisin du dessus
Toujours pas tu vas craquer non ?
Demande à ton voisin de droite
Tu veux de l'aide ? Moi aussi !
99dde1d35d1fdd283924d84e6d9f1d820
```
### How to Fix :
Do not expose important information in `robots.txt`
And better use a router to not allow the user to browse files freely on your server.
