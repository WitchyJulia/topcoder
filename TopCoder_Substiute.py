key = str(raw_input("Key:").split())
code = str(raw_input("Code:").split())
key_lst = list(key)
key_lst.remove("'")
key_lst.remove("'")
key_lst = key_lst[1:11:1]
code_lst = list(code)
code_lst.remove("'")
code_lst.remove("'")
final = int(len(code_lst) - 1)
code_lst = code_lst[1:final:1]
key1 = "".join(key_lst[0:1:1])
key2 = "".join(key_lst[1:2:1])
key3 = "".join(key_lst[2:3:1])
key4 = "".join(key_lst[3:4:1])
key5 = "".join(key_lst[4:5:1])
key6 = "".join(key_lst[5:6:1])
key7 = "".join(key_lst[6:7:1])
key8 = "".join(key_lst[7:8:1])
key9 = "".join(key_lst[8:9:1])
key10 = "".join(key_lst[9:10:1])
result = []

for c in code_lst:
    if c == key1:
        result.append("1")
    if c == key2:
        result.append("2")
    if c == key3:
        result.append("3")
    if c == key4:
        result.append("4")
    if c == key5:
        result.append("5")
    if c == key6:
        result.append("6")
    if c == key7:
        result.append("7")
    if c == key8:
        result.append("8")
    if c == key9:
        result.append("9")
    if c == key10:
        result.append("10")
resulted = "".join(result)
print resulted

