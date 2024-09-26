# # Задание 1
# n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# nn= []
# for num in n:
#     if num % 2 == 0:
#         nn.append(num)
#
# print(nn)
#
#
# # Задание 2
# def is_palindrome(s):
#     s_lower = s.lower() #делает буквы все маленькими
#     return s_lower == s_lower[::-1]
# print(is_palindrome("шалаш"))
# print(is_palindrome("нешалаш"))



# Задание 3 - сделала не сама, ChatGPT в помощь, но разобралась вроде как ТТ

def sum_pairs(numbers):
    # Удаляем последнее число, если количество чисел нечётное
    if len(numbers) % 2 != 0:
        numbers = numbers[:-1]
    # Список для хранения сумм пар
    pairs_sum = []
    # Проходим по списку с шагом 2
    for i in range(0, len(numbers), 2):
        pairs_sum.append(numbers[i] + numbers[i + 1])
    return pairs_sum
# Пример использования
nums = [1, 2, 3, 4, 5]
result = sum_pairs(nums)
print(result)  # Вывод: [3, 7, 11]
