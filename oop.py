class Metod:
    gl = 'aieouy'
    input_one = input()
    gl_one = 0
    sgl = 0
    def __init__(self, input_one, gl, gl_one, sgl):
        self.input_one = input_one
        self.gl = gl
        self.gl_one = gl_one
        self.sgl = sgl
        self.func_print()

    def func_print(self):
        return self.gl_one, self.sgl

    def func_str(self):
        if type(self.input_one) is list:
            for i in self.input_one:
                if i in self.gl:
                    self.gl_one += 1
                else:
                    self.sgl +=1


print(Metod.gl_one, Metod.sgl)