a = {}

with open('users.csv') as f:
    with open('hobby.csv') as f1:
        for line in f:
            if line:
                hobby = f1.readline()
                a[line.replace("\n", "")] = hobby.replace("\n", "")
            else:
                print("1")
print(a)