import statistics
import random

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )

        return (
            quicksort(items_less) +
            pivot_items +
            quicksort(items_greater)
        )

def get_random_numbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))

    return numbers

def twice(f):
    def result(x):
        return f(f(x))
    return result
@twice
def g(i):
    return i + 3    

if __name__ == '__main__':
    #plus_three = lambda i: i + 3
    #g = twice(plus_three)
    print(g(7))
    print(quicksort([10, -3, 21, 6, -8]))
    numbers = get_random_numbers(20)
    print(numbers)
    print(quicksort(numbers))