with open('my_file', 'r') as reader:
    for line in reader:
        print(line, end="")

with open('my_file', 'r') as reader:
    my_file_list = reader.readlines()

with open('my_file_2', 'w') as writer:
    for string in reversed(my_file_list):
        writer.write(string)
