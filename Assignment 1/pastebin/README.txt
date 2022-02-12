Flag: SIS_CTF{i_hope_you_liked_the_spoilers}

Tools: Browser, bash, crackstation.net

First I tried a couple of pastes and saw that every time there was a different
URL, but you could access older ones.
This got me thinking that the url might be encrypted/encoded/hashed so I used
crackstation to check for it.
It showed that it was hashed with md5 from a number.
I tried the URL's from multiple pastes and the number was increasing.

Afterwards i used `md5sum` to check url's for 1,2,... and found the spoilers
that were mentioned.
This meant that the flag was somewhere between 1 and my paste ~4000.

I created a script to get all addresses and their pages and look in them.
After running the script, the flag is returned.

```
	./auto_check.sh
```

