def anti_convert(number, base):
    result = 0
    size = len(number)
    for i in range(size):
        result += int(number[i]) * (base ** (size - i - 1))
    return result

# def convert(number, base):
#     result = ""
#     while number != 0:
#         result = str(number % base) + result
#         number //= base
#     return result
#
#
# print(convert(9**18 + 3**54 - 9, 3).count("2"))

# for x in "0123456789ABCDEFGHI":
#     value = int(f"321{x}4", 19) + int(f"498{x}9", 19)
#     if value % 23 == 0:
#         print(value // 23)
#         break

# for x in "0123456789":
#     value = int(f"{x}B09", 17) + int(f"{x}8E8", 15)
#     if value % 155 == 0:
#         print(value // 155)
#         break

# values = list()
# for x in "01234567":
#     for y in "01234567":
#         value = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)
#         if value % 117 == 0:
#             values.append(value // 117)
# print(min(values))


print(int("401041214", 40))
print(anti_convert("401041214", 40))
