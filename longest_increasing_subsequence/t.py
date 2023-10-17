def find_longest_increasing_subsequences(numbers):
    lis_list = []
    max_lis_len = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] >= numbers[i]:
                sub = [numbers[i], numbers[j]]
                last_added = numbers[j]
                for k in range(j + 1, len(numbers)):
                    if numbers[k] >= last_added:
                        sub.append(numbers[k])
                        last_added = numbers[k]
                lis_list.append(sub)
                if len(sub) >= max_lis_len:
                    max_lis_len = len(sub)

    print("All Longest Increasing Subsequences:")
    # print(lis_list)

    print("Longest Increasing Subsequence(s):")
    for i in lis_list:
        if len(i) == max_lis_len:
            print(f"The LIS: {i}\nLength: {max_lis_len}")

# Example usage with a different list of numbers
numbers = [5, 8, 2, 7, 9, 12, 15, 18, 11]
find_longest_increasing_subsequences(numbers)










# nl = [10, 22, 9, 33, 21, 50, 41, 60, 80]
# lis_list = []
# max_lis_len = 0
#
# for i in range(len(nl)):
#     for j in range(i + 1, len(nl)):
#         if nl[j] >= nl[i]:
#             sub = [nl[i], nl[j]]
#             last_added = nl[j]
#             for k in range(j + 1, len(nl)):
#                 if nl[k] >= last_added:
#                     sub.append(nl[k])
#                     last_added = nl[k]
#             lis_list.append(sub)
#             if len(sub) >= max_lis_len:
#                 max_lis_len = len(sub)
#
# print("All Longest Increasing Subsequences:")
# print(lis_list)
#
# print("Longest Increasing Subsequence(s):")
# for i in lis_list:
#     if len(i) == max_lis_len:
#         print(f"The LIS: {i}\nLength: {max_lis_len}")
