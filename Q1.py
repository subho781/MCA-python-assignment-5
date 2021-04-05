def change_char(str1):
    result = ""
    record = set()
    for i in range(len(str1)):
        item = str1[i]
        if item in record:
            result += "*"
        else:
            result += item
            record.add(item)
    return result

print(change_char('Balloon'))
