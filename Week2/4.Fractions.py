# Task An Immutable Fraction class

class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __eq__(self, other_frac):
        self.other_frac = other_frac
        try:
            result = "{}/{} == {}/{}".format(self.numerator, self.denominator, other_frac.numerator, other_frac.denominator)
            return result, self.denominator == other_frac.numerator/other_frac.denominator
        except ZeroDivisionError:
            return ("Divison by zero is not allowed!")

    def lcm(self):          # намиране на най-малко общо кратно

         self_den = self.denominator
         other_den = self.other_frac.denominator
         for i in range(1, self_den+1):
             if i*other_den % self_den == 0:
                return abs(i*(other_den))

    def gcd(self, general_copy, lcm_copy):                  # намиране на най-голям общ делител

        while general_copy != 0 and lcm_copy != 0:
            var = lcm_copy
            lcm_copy = general_copy % lcm_copy
            general_copy = var
        gcd = general_copy + lcm_copy
        return gcd

    def __add__(self, other_frac):
        try:
            self_num = self.numerator*(self.lcm() / self.denominator)
            other_num = other_frac.numerator*(self.lcm() / other_frac.denominator)
            total_numerator = self_num + other_num
            frac = self.lcm()

            result = self.gcd(total_numerator, frac)
            total_numerator /= result
            frac /= result

            if self.numerator == 0 and other_frac.numerator == 0:
                return "{}/{} + {}/{} = {}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),0)

            elif self.numerator == 0:
                return "{}/{} + {}/{} = {}/{}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),int(other_frac.numerator),int(other_frac.denominator))

            elif other_frac.numerator == 0:
                return "{}/{} + {}/{} = {}/{}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),int(self.numerator),int(self.denominator))

            elif total_numerator == frac:

                return "{}/{} + {}/{} = {}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),1)

            return "{}/{} + {}/{} = {}/{}".format(int(self.numerator), int(self.denominator),
            int(other_frac.numerator), int(other_frac.denominator),int(total_numerator), int(frac))

        except ZeroDivisionError:
            return ("Divison by zero is not allowed!")


    def __sub__(self, other_frac):

         try:
            self_num = self.numerator*(self.lcm() / self.denominator)
            other_num = other_frac.numerator*(self.lcm() / other_frac.denominator)
            total_numerator = self_num - other_num
            frac = self.lcm()

            result = self.gcd(total_numerator, frac)
            total_numerator /= result
            frac /= result

            if self.numerator == 0 and other_frac.numerator == 0:
                return "{}/{} - {}/{} = {}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),0)

            elif self.numerator == 0:
                return "{}/{} - {}/{} = -{}/{}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),int(other_frac.numerator),int(other_frac.denominator))

            elif other_frac.numerator == 0:
                return "{}/{} - {}/{} = {}/{}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),int(self.numerator),int(self.denominator))

            return "{}/{} - {}/{} = {}/{}".format(int(self.numerator), int(self.denominator),
            int(other_frac.numerator), int(other_frac.denominator),int(total_numerator), int(frac))

         except ZeroDivisionError:
            return ("Divison by zero is not allowed!")


    def __mul__(self, other_frac):
        try:
            total_numerator = self.numerator*other_frac.numerator
            total_denominator = self.denominator*other_frac.denominator

            result = self.gcd(total_numerator, total_denominator)
            total_numerator /= result
            total_denominator /= result

            if self.numerator == 0 and other_frac.numerator == 0:
                return "{}/{} * {}/{} = {}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),0)

            elif self.numerator == 0:
                return "{}/{} * {}/{} = {}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),0)

            elif other_frac.numerator == 0:
                return "{}/{} * {}/{} = {}".format(int(self.numerator), int(self.denominator),
                int(other_frac.numerator), int(other_frac.denominator),0)

            return "{}/{} * {}/{} = {}/{}".format(int(self.numerator), int(self.denominator),
            int(other_frac.numerator), int(other_frac.denominator),int(total_numerator), int(total_denominator))

        except ZeroDivisionError:
            return ("Divison by zero is not allowed!")

a = Fraction(15,13)
b = Fraction(9,6)

print (a == b)
print (a + b)
print (a - b)
print (a * b)



