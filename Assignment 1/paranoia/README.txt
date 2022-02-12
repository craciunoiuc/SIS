Flag: SIS_CTF{conceal_hide_avoid_veil}

Tools: linenum.sh, patience

First I wondered through different folders and files to find things of interest.
As I found a tmux session file I tried different methods to access it to see
if there was something of interest.
As this was a dead-end I switched to trying something else.

Then I stumbled through different files (there is a file leaking all past
connections IPs to the machine), but still I didn't find anything.
I also discovered a `flag.swp` inside `/var/tmp`, but this did not yield
any results.

Finally, I switched to using `linenum.sh` and first I listed all files of
interest.
Here I found that `sha512` had capabilities on it and I tried using it.
The hash obtained was not on crackstation so this was yet another dead-end.

After running the tool again I noticed that `setfacl` could be run without
entering the password so I used that.
After losing some more time, I realized you had to run the `cat` command in
the same line.
This was probably because there was a daemon program running that continuously
changed the acl back to normal.

