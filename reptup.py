check_string="MalegaonBaramatiPune"

dict = {}

for ch in check_string:

    if ch in dict:

        dict[ch] += 1

    else:

        dict[ch] = 1

        

for key in dict:

    print(key, "-" , dict[key])

