# Flag Debug

Flag: SIS_CTF{please_dont_do_this_ahx1que}

Tools: [`python`]

Description:
This challenge was pretty straight-forward.
I created a `flag` file and "reverse engineered" the binary.
I saw that you first had to guess the size and then you would get the 'offset' to the flag.
As such, I created a python script that first brute-forced the size and then brute-forced each letter inside `SIS_CTF{}`.
I had to create another one using `subprocess` to work on the remote.

I left no traces on the remote ;)

To get the flag:
```
    python3 brute_force_subproc.py # or brute_force_pwn.py if you have pwntools with processes
```