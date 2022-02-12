Flag: SIS_CTF{for_science___you_monster}

Tools: Browser, dirb, sqlmap


First I entered the website and scanned through it.
`sqlmap` returned that nothing is injectable.

Everything seemed in order so I looked at the requests.
After logging in, the requests had extra cookies sent.

I started looking at the cookies.
Because we are given a salt, I guessed that it is appended to something to
obtain the hash in the id.
After checking different hashes lengths I matches the id hash with md5.

Afterwards I tried appending the salt to the left and then to the right of
"student" to check if it matches.
(Here I lost 1h because I was appending newline, because I forgot to use -n)
Now I could modify the logged user to change the string.

Because there were no more clues in the page (except `cake`) I tried using
`dirb` to check for any hidden pages.
Nothing interesting was returned with the default configuration so I used
some additional wordfiles to check for everything.
Thankfully one of them returned "/portaladmin"

Entering this I was greeted with a GLaDOS only message so I quickly changed
the user with the method discovered beforehand.
Now I could enter the page.

After losing more than enough time trying to find hidden meanings in the
poems I inspected the page and saw the commented flag.
This was quite a journey.

