from PyOptimizer.Model import Model
class Optimizer:
    def __init__(self, model):
        if(isinstance(model,Model)):
            self.model = model
        else:
            print("Model invalid")
    pass

    def setModel(self,model):
        if (isinstance(model, Model)):
            self.model = model
        else:
            print("Model invalid")
    pass
