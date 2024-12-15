import numpy as np
class Linear_Regression():
    #initiating the parameters( learning rate and the number of iteration)
    def __init__(self,learning_rate,no_of_iteration):
        self.learning_rate=learning_rate
        self.no_of_iteration = no_of_iteration
    
    
    def fit(self,X,Y):
        #number of training examples and number of features
        self.m,self.n=X.shape
        #initiating the weight and bias 
        self.w =   np.zeros(self.n)
        
        self.b=0
        self.X=X
        self.Y=Y
        
        #implementing Gradient Descent
        for i in range ( self.no_of_iteration):
            self.update_weight()
        
        
    def update_weight(self):
        Y_predication = self.predict(self.X)
        #calculate 
        dw = -(2 *(self.X.T).dot(self.Y -Y_predication))/self.m
        db=-2*np.sum(self.Y -Y_predication)/self.m
        #updating the weight
        self.w=self.w - self.learning_rate*dw
        self.b=self.b-self.learning_rate*db
    
    def predict(self,X):
        return X.dot(self.w)+ self.b
    