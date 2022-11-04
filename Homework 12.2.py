import json

A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = A.copy()

for i, j in B.items():
    if A.get(i):
        C[i] = [C[i], j]
    else:
        C[i] = j

json_C = json.dumps(C)

with open("result.json", "w") as f:
    f.write(json_C)
