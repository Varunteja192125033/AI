from itertools import permutations

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def travelling_salesman_bruteforce(distances):
    num_cities = len(distances)
    all_cities = set(range(num_cities))
    min_distance = float('inf')
    optimal_path = None

    for path in permutations(all_cities):
        distance = calculate_total_distance(path, distances)
        if distance < min_distance:
            min_distance = distance
            optimal_path = path

    return optimal_path, min_distance

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_path, min_distance = travelling_salesman_bruteforce(distances)
print("Optimal Path:", optimal_path)
print("Minimum Distance:", min_distance)
