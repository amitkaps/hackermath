import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

def vis2d(X, y):
    plt.scatter(X[:,0], X[:,1], c = y, s = 50, cmap='bwr')
    plt.show()
    
def visClassifier2d(X, y, clf):
    s = 1.1
    x1_min, x1_max = X[:,0].min()*s, X[:,0].max()*s
    x2_min, x2_max = X[:,1].min()*s, X[:,1].max()*s
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, (x1_max - x1_min)/100), 
                           np.arange(x2_min, x2_max, (x2_max - x2_min)/100))
    z = clf.predict(np.c_[xx1.ravel(), xx2.ravel()])
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, cmap='viridis', alpha = 0.3)
    plt.scatter(X[:,0], X[:,1], c = y, s = 50, cmap='bwr')
    plt.show()
    
    
def visClassifier2dProb(X, y, clf):
    s = 1.1
    x1_min, x1_max = X[:,0].min()*s, X[:,0].max()*s
    x2_min, x2_max = X[:,1].min()*s, X[:,1].max()*s
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, (x1_max - x1_min)/100), 
                           np.arange(x2_min, x2_max, (x2_max - x2_min)/100))
    z = clf.predict_proba(np.c_[xx1.ravel(), xx2.ravel()])[:,0]
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, cmap='viridis', alpha = 0.3)
    plt.scatter(X[:,0], X[:,1], c = y, s = 50, cmap='bwr')
    plt.show()