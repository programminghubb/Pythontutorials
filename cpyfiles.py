with open('newfile.txt', 'r') as nf:
    with open('newfile2.txt', 'w') as nff:
        for line in nf:
            nff.write(line)
