# Pit

Flag: SIS_CTF{me_puero_silvae_ambulacram}

Tools: [`python`, `stat`, `cat`, `tar`]

Description:
First I put together the archive and untarred it.
I saw that all files had the same content in them (same checksum) and discovered that they contained only NULL.
The hint said that the flag is in order so there had to be something in the first file.
As nothing special was inside it I tried looking inside the archive, but the output was too hard to read.
Finally, I tried reading metadata and saw that some things differed between the files.
As the flag character had to be in the each of the files I looked at the first and third ones.
They both had the same number of blocks.
Also, there were multiple `_` as the block number for `_` was repeated.
After looking at the ascii values a bit, I discovered that the ascii value was `nr_of_blocks / 8`.
I created a small python script and got the flag.


To get the flag:
```
 # Generate the metadata file using:
 stat -c %b 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 > metadata

 # Get the flag:
 ./parse.py
```
