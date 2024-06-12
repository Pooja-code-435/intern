def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def largest_prime(numbers):
    max_prime = None
    for num in numbers:
        if is_prime(num):
            if max_prime is None or num > max_prime:
                max_prime = num
    return max_prime
test_numbers = [2, 3, 17, 19, 23, 97]
result = largest_prime(test_numbers)
if result is not None:
    print(f"The largest prime number in the list is {result}.")
else:
    print("There is no prime number in the list.")


def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = (n * (n + 1)) // 2
    array_sum = sum(arr)
    missing_number = total_sum - array_sum
    return missing_number
test_array = [1, 2, 4, 5, 6]
missing_number = find_missing_number(test_array)
print("The missing number in the array {} is {}".format(test_array, missing_number))


def find_repeating_number(arr):
    seen = set()
    repeating_numbers = set()
    for num in arr:
        if num in seen:
            repeating_numbers.add(num)
        else:
            seen.add(num)
    return repeating_numbers
test_array = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
repeating_numbers = find_repeating_number(test_array)
if repeating_numbers:
    print("The repeating numbers in the array {} are: {}".format(test_array, repeating_numbers))
else:
    print("No repeating numbers found in the array {}.".format(test_array))
    
