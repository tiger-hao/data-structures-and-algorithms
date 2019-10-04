def merge(arr, left, mid, right):
    A = arr[left:mid]
    B = arr[mid:right]
    i = j = 0

    for k in range(left, right):
        if i < len(A) and (j >= len(B) or A[i] <= B[j]):
            arr[k] = A[i]
            i += 1
        else:
            arr[k] = B[j]
            j += 1

        k += 1


def merge_sort(arr, left, right):
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)


def main():
    arr = [5, 3, 15, 8, 2, 9, 1, 5, 0, 3, 11]
    print("Unsorted:", arr)

    merge_sort(arr, 0, len(arr))
    print("Sorted:", arr)


if __name__ == "__main__":
    main()
