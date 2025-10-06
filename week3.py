# Hoca kağıt verdi bu hafta, onu direkt bilgisayara aktardık.

class Stack:
    def __init__(self, N):
        self.N=N #capacity
        self.dizi = [None] * N # fixed size list
        self.top = -1 #empty begin

    def top(self):
        if self.is_empty():
            print("Stack boş, top yok!")
            return -1
        return self.dizi[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.N -1

    def push(self, e):
        if not self.is_full():
            self.top += 1
            self.dizi[self.top] = e
            print(f"{e} push")
        else:
            print("Stack is full, can not run push")

    def pop(self):
        if not self.is_empty():
            val = self.dizi[self.top]
            self.top -= 1
            print(f"{val} pop runned.")
            return val
        else:
            print("Stack is empty, can not run pop")
            return -1



#TEST
if __name__ == "__main__":
    yig = Stack(5)

    #6 time push
    for i in range(1,7):
        yig.push(i)

    #pop all elements
    for j in range(len(yig.dizi), 0, -1):
        yig.pop()

    # extra pop tries (empty stack)
    yig.pop()
    yig.pop()

cekmece = Stack(4)


class Stack2:
    def __init__(self):
        self.top = 0

    def push(self, x, arr, top):
        arr[self.top] = x
        top += 1
        self.top = top

    def pop(self,a , top):
        if self.top == 0:
            raise IndexError("Pop from empty stack.")
        top -= 1
        self.top = top
        return a[top]

# Hoca tahtaya yazmış bunları, bu kodların altına yazmamızı istedi
st = Stack2()
expr = '532-/47*+'
st_ar = [0] * len(expr) # ÖNEMLİ: push arr[self.top] yazdı

for i in range(len(expr)):
    ch = expr[i]
    if '0' <= ch <= '9':
        x = int(ch)
        st.push(x, st_ar, st.top)

    elif ch == '+':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a+b, st_ar, st.top)
        print("a+b = ", (a+b))

    elif ch == '-':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a-b, st_ar, st.top)
        print("a-b = ", (a-b))

    elif ch == '*':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        st.push(a*b, st_ar, st.top)
        print("a*b = ", (a*b))

    elif ch == '/':
        b = st.pop(st_ar, st.top)
        a = st.pop(st_ar, st.top)
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        st.push(a/b, st_ar, st.top)
        print("a/b = ", (a/b))

print("Postfix sonucu =", st.pop(st_ar, st.top))