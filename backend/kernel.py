import io
import sys
class CustomKernel:
    def __init__(self):
        self.user_globals={}
    def execute(self, code_string):
        buffer = io.StringIO()
        sys.stdout = buffer 
        try:
            exec(code_string, self.user_globals)
            output = buffer.getvalue().strip()
            sys.stdout = sys.__stdout__
            return(output)
        except Exception as e:
            output = buffer.getvalue().strip()
            sys.stdout = sys.__stdout__
            return(output + f'\nError: {str(e)}')
        finally:
            sys.stdout = sys.__stdout__
if __name__ == "__main__":
    k=CustomKernel()
    print(k.execute("print('hello_world')\nx=10"))
    print(k.execute("print(x)"))
    print(k.execute("print(y)"))