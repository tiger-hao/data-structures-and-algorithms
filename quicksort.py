def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)
        quicksort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo

    for j in range(lo, hi):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[hi] = arr[hi], arr[i]
    return i


def main():
    arr = [5, 3, 15, 8, 2, 9, 1, 5, 0, 3, 11]
    print("Unsorted:", arr)

    quicksort(arr, 0, len(arr) - 1)
    print("Sorted:", arr)


if __name__ == "__main__":
    main()
