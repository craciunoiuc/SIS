Flag: SIS_CTF{give_me_something_to_shoot}

Tools: IDA, nc, nasm, shellstorm, peda, strings

(The story below does not include the hundreds of fails)

First I decompiled the source with IDA and saw that program reads 32 bytes
and appends an exit shellcode to it.
It also places it inside a page that is both writable and executable.

Finally it also check for usual characters inside a shellcode (/ b i n s h).

First I tried to build a shellcode myself, but as I could not get below 32
bytes, I started looking through all smaller ones on shellstorm.
The idea behind it was to give not(/bin//sh) and negate the string before
placing it on the stack.

Thankfully, I actually found one that did exactly this.
I assembled it with nasm and tested inside peda.
It worked as expected so I moved on to the remote one.

I used netcat to connect to the remote and use the shell to do strings on the
executable.

```
	cat shellcode - | nc 141.85.224.99 2242
	ls
	cd /home/ctf/extraction
	strings extraction
```

