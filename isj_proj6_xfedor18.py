class Polynomial():

    def __init__(self, *args, **intt):
        self.digits = list()
        for i in args:
            if type(i) is list:
                self.digits = i
        if not self.digits:
            if args:
                self.digits = list(args)
            else:
                for name, value in intt.items():
                    for i in range(1 + int(name.split("x")[1]) - len(self.digits)):
                        self.digits.append(0)
                    self.digits[int(name.split("x")[1])] = value
        for i in range(len(self.digits) - 1, 0, -1):
            if self.digits[i] == 0:
                del self.digits[i]
            else:
                break

    def __str__(self):
        arr = ""
        if len(self.digits) == 1:
            arr = arr + str(self.digits[0])
            return arr
        for i in reversed(range(len(self.digits))):
            if self.digits[i] == 0:
                continue
            if arr:
                if self.digits[i] > 0:
                    arr += " + "
                else:
                    arr += " - "
            if i == 0:
                arr += "{0}".format(str(abs(int((self.digits[0])))))
                return arr
            if i == 1:
                if abs(self.digits[1]) == 1:
                    arr += "x"
                else:
                    arr += "{0}x".format(str(abs(int(self.digits[1]))))
            else:
                if abs(self.digits[i]) == 1:
                    arr += "x^{0}".format(i)
                else:
                    arr += "{0}x^{1}".format(str(abs(int(self.digits[i]))), i)
        return arr

    def __eq__(self, other):
        if len(self.digits) != len(other.digits):
            return False
        for s, o in zip(self.digits, other.digits):
            if s != o:
                return False
        return True

    def __add__(self, other):
        tmp = self.digits[:]
        i = 0
        for tmp_digits, o_digits in zip(self.digits, other.digits):
            tmp[i] = tmp_digits + o_digits
            i = i + 1
        if (len(self.digits) < len(other.digits)):
            for i in range(len(self.digits), len(other.digits)):
                tmp.append(other.digits[i])
        return Polynomial(tmp)

    def derivative(self):
        if len(self.digits) == 1:
            return 0
        tmp = self.digits[:]
        del tmp[0]
        for a in range(len(tmp)):
            tmp[a] = tmp[a] * (a + 1)
        return Polynomial(tmp)

    def at_value(self, x1, x2="undefined"):
        res = self.digits[-1]
        for i in reversed(range(len(self.digits) - 1)):
            res = (res * x1) + self.digits[i]
        if x2 == "undefined":
            return res
        else:
            res2 = self.digits[-1]
        for i in reversed(range(len(self.digits) - 1)):
            res2 = (res2 * x2) + self.digits[i]
        return res2 - res

    def __mul__(self, other):
        tmp = [0] * (1 + len(self.digits) + len(other.digits))
        for i in range(len(self.digits)):
            for j in range(len(other.digits)):
                tmp[i + j] += self.digits[i] * other.digits[j]
        return Polynomial(tmp)

    def __pow__(self, n):
        if n == 1:
            return Polynomial(self.digits)
        if n == 0:
            if len(self.digits) == 1 and self.digits[0] == 0:
                raise ValueError("Undefined operation: 0^0")
            else:
                return 1
        if n < 0:
            raise ValueError("Negative power is not supported.")
        if n > 1:
            tmp = self
            for i in range(1, n):
                tmp *= self
            return Polynomial(tmp)


print(Polynomial(x0=1))
print(Polynomial(x1=1))
print(Polynomial(x2=3, x0=-1, x1=-2).at_value(5))
print(Polynomial(x2=3, x0=-1, x1=-2).at_value(3))
print(Polynomial(x2=3, x0=-1, x1=-2).at_value(3, 5))
print(Polynomial(x0=1) + Polynomial(x1=1))
