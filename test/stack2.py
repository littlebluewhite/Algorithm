def solution(s: str) -> bool:
    lt = []
    d = {")": "(", "]": "[", "}": "{"}
    for i in s:
        if i in d.values():
            lt.append(i)
        elif i in d.keys():
            if len(lt) < 1:
                return False
            if lt.pop() != d[i]:
                return False
    if not lt:
        return True
    else:
        return False


print(solution("(NADI[3D]{(OCMS), (id=8)})"))
print(solution("(NADI[3D{O]CMS, (id=8)})"))
print(solution("(NADI)[3D]{OCMS, (id=8)})"))
print(solution("(NADI[3D]{OCMS, (id=8)]})"))
print(solution("(NADI[[3D]{OCMS, (id=8)}])"))
