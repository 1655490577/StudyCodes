with open('0013_a1.txt', 'r', encoding='utf-8') as f:
    a = f.read().splitlines()

list = []

for i in a:
    i = i.replace(' ','')
    if not i:
        continue
    name, age = i.split(':')
    if int(age) > 50:
        list.append(name)

with open('0013_a1.txt', 'a', encoding='utf-8') as b:
    c = ','.join(list)
    text = f'\n大于50岁的人有：{c}'
    b.write(text)

# with open('0013_a1.txt', encoding='utf8') as f:
#     lines = f.read().splitlines()
#
# oldPeople = []
# for line in lines:
#     # 去掉行中的空格
#     line = line.replace(' ', '')
#
#     # 如果是空格，跳过
#     if not line:
#         continue
#
#     name, age = line.split(':')
#     if int(age) > 50:
#         oldPeople.append(name)
#
# oldPeopleStr = ','.join(oldPeople)
# appendText = f'\n\n大于50岁的人有：{oldPeopleStr}'
#
# with open('0013_a1.txt', 'a', encoding='utf8') as f:
#     f.write(appendText)

