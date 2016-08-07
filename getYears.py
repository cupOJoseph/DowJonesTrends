strings = ["01/15/2015", "11/15/3015", "07/21/14"]

year = 15
for string in strings:
    print string

    if string.endswith(str(year)):
        print "year is ", str(year)
    else:
        year -= 1
        print "year is ", str(year)
