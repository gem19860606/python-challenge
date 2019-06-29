def max_groups(ary):
    stk = [ary[0]]
    for item in ary[1:]:
        if (item >= stk[-1]):
            stk.append(item)
        else:
            last = stk.pop()
            while(len(stk) > 0 and stk[-1] > item):
                stk.pop()
            stk.append(last)
        
    return len(stk)

def main():
    test_ary = [1, 4, 3, 4, 2, 1]
    print(max_groups(test_ary))

if __name__ == "__main__":
    main()
