import json


# f = open('files/moj_plik.txt')
#
# for line in f:
#     print(line)
#
# f.close()

# with open('files/moj_plik.txt') as f:
#     for line in f:
#         print(line)

# with open('files/moj_plik.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)

# with open('files/moj_plik.txt') as f:
#     foo = f.read()
#     # print(f.read())
# print(foo)

# with open('files/moj_plik.txt') as f:
#     print(f. readline())
#     print(f. readline())

# with open('files/moj_plik.txt') as f:
#     # foo = f.read()
#     print(f. readlines())

# with open('files/nowy_plik.txt', 'r') as f:
#     print('przed:\n', f.read())
#
# with open('files/nowy_plik.txt', 'w') as f:
#     f.write('hello pliki\ndruga linia')
#
# with open('files/nowy_plik.txt', 'r') as f:
#     print('po:\n', f.read())

# with open('files/moj_json.json', 'r') as read_file:
#     data = json.load(read_file)
#     print(data)
#     print(data['firstName'])
#     print(data['address'])


with open('files/moj_json.json', 'r') as read_file:
    data = json.load(read_file)
json_string = json.dumps(data)
print(json_string)
btp = json.loads(json_string)
print(btp)
with open('files/new_json.json', 'w') as write_file:
    json.dump(data, write_file)
