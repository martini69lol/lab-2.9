def find(find_list):
    N = int(pow(2, len(find_list)))
    s = set()
    find_list.sort()
    for i in range(N):
        subset = []
        for j in range(len(find_list)):
            if i & (1 << j):
                subset.append(find_list[j])

        s.add(tuple(subset))

    print(s)


if __name__ == '__main__':
    find_list = [1, 2, 1]
    find(find_list=find_list)
