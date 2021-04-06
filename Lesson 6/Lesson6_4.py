with open('users.csv') as f1:
    with open('hobby.csv') as f2:
        for line in f1:
            if line:
                hobby = f2.readline()
                name = line.replace("\n", "")
                a = f'{name}: {hobby}'
            else:
                print("1")
            with open('users_hobby.txt', 'a') as f:
                f.write(a)