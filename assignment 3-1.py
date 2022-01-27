# 스택 활용 문제

global arr
arr = []

class stack:
    def __init__(self, arr):
        self.arr = arr
    

    def push(self, data):
        self.arr.append(data)


    def pop(self):
        if len(arr) > 0:
            p = self.arr[len(arr) - 1]
            self.arr.pop(len(arr) - 1)
            return p

        else:
            return -1


    def size(self):
        return len(arr)


    def empty(self):
        if len(arr) == 0:
            return 1
        else:
            return 0


    def top(self):
        if len(arr) > 0:
            return self.arr[len(arr) - 1]
        
        else:
            return -1


def main():
    global arr
    check = stack(arr)
    command = input("")
    
    # push
    if command[:3 + 1] == "push":
        check.push(command[5:])

    # pop
    if command == "pop":
        print(check.pop())

    # size
    if command == "size":
        print(check.size())

    # empty
    if command == "empty":
        print(check.empty())

    # top
    if command == "top":
        print(check.top())
        

N = input("명령의 수 : ")
for i in range(int(N)):
    main()