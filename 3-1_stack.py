class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        return self.stack.append(x)
    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop()
    def size(self):
        return len(self.stack)
    def empty(self):
        if self.stack ==[]:
            return 1
        else:
            return 0
    def top(self):
        if self.stack ==[]:
            return -1
        else:
            return self.stack[-1]
def main():
    N=int(input("명령의 수:"))
    output=Stack()
    for i in range(N):
         command=input()
         if "push" in  command :
           output.push(command[-1])
         elif command == "pop" :
            print(output.pop())
         elif command == "size" :
            print(output.size())
         elif command == "empty" :
            print(output.empty())
         elif command == "top" :
            print(output.top())
      
main()

