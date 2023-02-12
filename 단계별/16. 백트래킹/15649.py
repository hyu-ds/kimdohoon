n, m = map(int, input().split())

def permutation(lst):
    if len(lst) == m:
        print(' '.join(map(str, lst)))