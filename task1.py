# TASK 1
# Zaimplementuj funkcję, która znajduje maksymalny i minimalny element tablicy, korzystając z metody „dziel i zwyciężaj”.
# Funkcja akceptuje tablicę liczb o dowolnej długości.
# Zastosowano podejście rekurencyjne.
# Funkcja zwraca krotkę wartości (minimum, maksimum).
# Złożoność algorytmu wynosi O(n).

def find_min_max(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty") 
    if len(arr) == 1:
        return (arr[0], arr[0])
    mid = len(arr) // 2
    left_min_max = find_min_max(arr[:mid])
    right_min_max = find_min_max(arr[mid:])
    return (min(left_min_max[0], right_min_max[0]), max(left_min_max[1], right_min_max[1])) 

# Example usage:
if __name__ == "__main__":
    arr = [3, 5, 1, 8, 2]
    min_val, max_val = find_min_max(arr)
    print("Minimum:", min_val)
    print("Maximum:", max_val)


