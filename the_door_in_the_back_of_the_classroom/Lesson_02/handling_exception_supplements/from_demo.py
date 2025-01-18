

class SumError(Exception):
    """raised when custom_sum fails"""


def custom_sum(nums: list[int | str]) -> int | None:
    sum = 0
    for num in nums:
        try:
            sum += int(num)
        except ValueError as e:
            raise SumError from e
    return sum


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 'five', 6]
    custom_sum(nums)
