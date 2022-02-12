# Tic Toc

Flag: SIS_CTF{when_did_you_have_the_time?}

Tools: [`IDA`, `rm`]

Description:
I tried running the program and saw that I had to match the number.
I opened it in `IDA` and saw some interesting `sleep` calls that could be 'abused'.
As the program opened a tmp file and wrote to it and then read it, this could be used.
From here I saw 2 methods:
 * Continuously search for `tmp*` files and echo the value chosen into it between the write and the read
 * Continuosly delete all files matching the pattern `tmp*`.
The second one worked because the value was read inside a variable with default 0.
Because of this, this method also worked.

I tried the second one as it was easier to do.

For some reason (maybe directory permissions) I had to run everything from the parent directory.
After doing this, I got the flag.

To get the flag:
```
    while true; do rm -f tmp*; done # in one terminal or as a background process
    ./tictoctou/tictoc 0 # in another terminal
```
