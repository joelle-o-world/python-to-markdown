cat ./python-to-markdown.py | python ./python-to-markdown.py > readme.md

echo -e "\nNOTE: This readme was generated by piping the program to itself! (see generate-readme.sh)" >> readme.md
