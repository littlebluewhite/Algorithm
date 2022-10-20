def bar(s: str):
    print(s)
    if len(s) <= 1:
        return
    mid_index = len(s) // 2
    bar(s[0: mid_index])


bar("abcdefghijklmnopqrstuvwxyz")
