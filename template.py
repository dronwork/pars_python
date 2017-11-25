in_file = "IN.txt"
out_file = "OUT.txt"
data_file = []

# Open and parse file !
with open(in_file, 'r') as read_file:
    tmp_string = ''
   # On Ruby it easier !!!
    for line in read_file:
        my_string = line.strip('\n')
        if my_string[0] == "c":
            data_file.append(my_string)
        if my_string[0] == "a":
            tmp_string = my_string
        if my_string[0] == "b":
            tmp_string = '%s - %s' % (tmp_string, my_string)
            data_file.append(tmp_string)
            tmp_string = ''

# Save !
with open(out_file, 'a') as save_file:
    for line in data_file:
        save_file.write('%s\n' % line)