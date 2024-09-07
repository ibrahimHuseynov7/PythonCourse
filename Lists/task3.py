
numbers = [1, 2, 3, 4, 5, 6, 7, 8]


numbers_copy = numbers.copy()

# Dilimləmə ilə kopyalanan list-dən ilk 3 elementi əldə edirik, mən burda dərsdə kecdiyimiz slice yəni dilimləmə istifadə etmisəm
first_three_words = numbers_copy[:3]

# Nəticədə dəyişdirilmiş list-ləri ekrana çıxaraq 
print("Original list:", numbers)
print("Copied list:", numbers_copy)
print("First three numbers:", first_three_words)
