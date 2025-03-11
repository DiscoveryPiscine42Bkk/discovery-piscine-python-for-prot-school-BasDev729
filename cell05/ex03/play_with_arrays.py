def remove_duplicates(arr):
    seen = set()
    unique_values = []
    
    for num in arr:
        if num not in seen:
            seen.add(num)
            unique_values.append(num)
    
    return unique_values
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
filtered_output = remove_duplicates(original_array)

print(filtered_output)
