file_handle = open('hygdata_v3.csv')
count = 0
for line in file_handle:
    count = count + 1
    print(line,end='')
#print('Line count:', count)

# text = file_handle.read()
# print(len(text))