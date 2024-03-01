def count_palindromes_in_range(start, end):

    count = 0
    for num in range(start, end + 1):
        if str(num) == str(num)[::-1]:
            count += 1
    return count
start = 8
end = 34
print(count_palindromes_in_range(start, end)) # Output: 5

start = 1550
end = 1552
print(count_palindromes_in_range(start, end)) # Output: 1
