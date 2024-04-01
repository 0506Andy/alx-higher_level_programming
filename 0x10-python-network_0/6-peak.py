def find_peak(list_of_integers):
    """
    Find a peak element in a list of unsorted integers.
    A peak element is one that is not smaller than its neighbors.
    """
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        # Check if mid is a peak
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
           (mid == len(list_of_integers) - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        # If the middle element is not a peak and its left neighbor is greater than it,
        # then the left half must have a peak element
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        # If the middle element is not a peak and its right neighbor is greater than it,
        # then the right half must have a peak element
        else:
            low = mid + 1

    return None
