Flag: SIS_CTF{Fluffy_fictional_friends}

Tools: md5sum, crackstation, patience

I started by first looking for a flag file.
As it was nowhere to be found I started looking randomly around.
Everything was read-only so I couldn't create anything or copy.

This is where I said I have no hope but to check everything.
This is because I saw that the fs was relatively clean and I could go through
everything in a reasonable time.

After a lengthy time I saw some interesting files in `/usr/local/share`, that
could not be created by default.
Unfortunately they were restricted.

This is when I tried looking for capability files but `getcap` was not on the
system.
As I knew one binary should have been able to read the content, I started trying
everything that seemed logical.
As most exercises used `shasum` and `mdsum` I went to those and tried them all.
`md5sum` worked and gave the hash for each file.

Finally I searched them on crackstation and got the flag.

