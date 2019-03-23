
def find_two_numbers_for_sum(number_list, sum):
    start = 0
    end = len(number_list) -1
    while(start < end):
        small_num = number_list[start]
        big_num = number_list[end]
        if (small_num + big_num == sum):
            return (small_num, big_num)
        elif (small_num < sum - big_num):
            start = start + 1
        else:
            end = end -1
    return None


def main():
    sum = 13
    number_list = [20, 5, 1, 10, 3, 2, 13]
    number_list.sort()
    
    two_numbers = find_two_numbers_for_sum(number_list, sum)
    print(two_numbers)


if __name__ == "__main__":
    main()
