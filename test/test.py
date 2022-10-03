def solution(s):
    lt = []
    d = {")": "(", "]": "[", "}": "{"}
    for i in s:
        if i in d.values():
            lt.append(i)
        elif i in d.keys():
            if len(lt) < 1:
                return False









# input: (NADI[3D]{(OCMS), (id=8)})
# output: True
#
# input: (NADI[3D{O]CMS, (id=8)})
# output: False
#
# input: (NADI)[3D]{OCMS, (id=8)})
# output: False
#
# input: (NADI[3D]{OCMS, (id=8)]})
# output: False