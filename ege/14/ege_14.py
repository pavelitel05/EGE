"""
author: Nerzon (30.10.2024)
"""


def anti_convert(number, base):
    """
    :param number: число, которое хотим перевести type:str
    :param base: основание системы счисления, из которой хотим перевести type:int
    :return: число number, переведенное в десятичную систему счисления type:int
    """
    result = 0
    size = len(number)
    for i in range(size):
        result += int(number[i]) * (base ** (size - i - 1))
    return result


def convert(number, base):
    """
    :param number: число, которое хотим перевести type:str
    :param base: основание системы счисления, в которую хотим перевести type:int
    :return: число number, переведенное в систему счисления с основанием base type:int
    """
    result = ""
    while number != 0:
        result = str(number % base) + result
        number //= base
    return result


# 1) Прямое сложение в СС
# print(convert(9**18 + 3**54 - 9, 3).count("2"))

# 2) Операции в одной СС с одной переменной
# for x in "0123456789ABCDEFGHI":
#     value = int(f"321{x}4", 19) + int(f"498{x}9", 19)
#     if value % 23 == 0:
#         print(value // 23)
#         break

# 3) Операции в разных СС с одной переменной
# for x in "0123456789":
#     value = int(f"{x}B09", 17) + int(f"{x}8E8", 15)
#     if value % 155 == 0:
#         print(value // 155)
#         break

# 4) Операции с двумя переменными
# values = list()
# for x in "01234567":
#     for y in "01234567":
#         value = int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)
#         if value % 117 == 0:
#             values.append(value // 117)
# print(min(values))
