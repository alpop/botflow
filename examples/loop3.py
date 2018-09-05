from botflow.flow import Pipe,Branch,Loop
from botflow.botframe import BotFrame
class Sum(object):
    def __init__(self):
        self.sum=0
    def __call__(self, i):
        self.sum+=i
        return self.sum
    def __repr__(self):
        return 'sum:'+str(self.sum)

op_sum=Sum()

def main():
    Pipe(
        Loop(range(10)),
        Loop(range(10)),
            Branch(op_sum,print)
        )

    BotFrame.run()
    print(op_sum)
main()




