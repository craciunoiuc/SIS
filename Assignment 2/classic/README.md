# Classic

Flag: SIS_CTF{fere_libenter_homines_id_quod_volunt_credunt}

Tools: [`python`, `pwntools`, `IDA`, `peda`, `objdump`, `ROPgadget`]

Description:
This was a strong one.
First I inspected the program with `IDA` and it's flow with `gdb-peda`.
I saw the buffer overflow in the `main` function.
As DEP was activated I used `ROPgadget` to find any `pop rdi; ret` gadgets.
Thankfully, there was one.

Then I got to writing the exploit.
Because ASLR was on, there was a need for an information leak first.
I got the addresses of `puts@plt` and `puts@got` from `objdump` and `gdb`.
I then sent a payload to basically call `puts@plt(puts@got)` and got the absolute address of `puts@libc`.
Then, with the offsets from `objdump` I got the address of `system@libc` and `'/bin/sh'@libc`, by calculating them.
The first stage was done.

In the second stage I sent another payload to call `system@libc('/bin/sh'@libc)` and got the shell.

Note: There is currently a small problem with the local addresses (the default `libc` is used), but the exploit works on the remote.

To get the flag:
```
    ./exploit.py
```
