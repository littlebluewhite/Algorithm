def solution(s: str):
    locl = {}
    locr = {}

    for i,w in enumerate(s):
        if w == "(":
            locl[i] = "("
        if w == ")":
            locr[i] = ")"
    if len(locl) != len(locr):
        return False
    if sorted(locl)[0] > sorted(locr)[0]:
        return False
    if sorted(locl)[-1] > sorted(locr)[-1]:
        return False
    return True
print(solution("(NADI3D(OCMS), id=8)"))
print(solution("(NADI3D(OCMS)), id=8)"))
print(solution("(NADI(3D(OCMS), id=8)"))