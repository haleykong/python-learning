# READING FILES
# - Open and read files, do something with content of files

# ipsum_file = open('files/ipsum.txt')

# # for line in ipsum_file:
# #     # Strip out gap in between each line
# #     print(line.rstrip())

# # # Return to start of file
# # ipsum_file.seek(0)

# # # Store each line in a list
# # lines = ipsum_file.readlines()
# # print(lines)

# ipsum_file.seek(50)
# # Read a certain number of characters
# file_text = ipsum_file.read(100)
# print(file_text)

# # Close file to ensure no performance hit
# ipsum_file.close()

def sequence_filter(line):
    return '>' not in line


with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))

# Do not need to close the file with syntax above
