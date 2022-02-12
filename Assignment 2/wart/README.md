# Wart

Flag: SIS_CTF{Ceterum_censeo_Carthaginem_delendam_esse}

Tools: [`python`, `cat`, `luck`]

Description:
The flag is hidden inside the archive itself and is ordered with the file numbers.
I was a bit lucky as I accidentaly `cat` the `tar` archive.
There I saw the flag characters.
First I tried to order by `atime` and `ctime`, but no luck.
Finally, I saw that the order was same as the file numbers inside the archive.

(I also parsed the output a bit by using grep on the archive)

To get the flag:
```
    cat wart_0965a5637fb538b9cc23525a198015a2.tar | grep -a --binary ctime -A 1 > input.txt
    # Format the input.txt file by removing the first line(s)

    cat wart_0965a5637fb538b9cc23525a198015a2.tar | grep -a --binary -o "wart/[0-9][0-9]*" > output_order.txt

    ./parse.py
```