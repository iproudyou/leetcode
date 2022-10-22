def solution():
    def condition(value):
        pass

    # left is the mininal value satisfying condition
    def binary_search(my_list):
        left, right = min(search_space), max(search_space)
        while left < right:
            mid = left + (right - left) // 2
            if coniditon(mid):
                right = mid
            else:
                left = mid + 1

        return left