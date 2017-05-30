class Complejo(object):
    def __init__(self, p_real, p_ima=0.0):
        self.p_real = p_real
        self.p_ima = p_ima

    def sumar(self, aux):
        return Complejo(self.p_real + aux.p_real,
                        self.p_ima + aux.p_ima)

    def restar(self, aux):
        return Complejo(self.p_real - aux.p_real,
                        self.p_ima - aux.p_ima)

    def multiplicar(self, aux):
        return Complejo(self.p_real * aux.p_real - self.p_ima * aux.p_ima,
                        self.p_ima * aux.p_real + self.p_real * aux.p_ima)

    def __str__(self):
        return str(self.p_real) + ", " + str(self.p_ima) + "i"

    def __eq__(self, aux):
        return self.p_real == aux.p_real and self.p_ima == aux.p_ima
