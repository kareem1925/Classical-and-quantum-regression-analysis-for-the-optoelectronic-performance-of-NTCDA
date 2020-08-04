#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:22:50 2020

@author: kareem
"""

from pennylane import numpy as np
import pennylane as qml
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score as r2
from sklearn.metrics import mean_absolute_error as mae



dev = qml.device('strawberryfields.fock', wires=1, cutoff_dim=18,hbar=2)

def accuracy(labels, predictions):
    score = mse(labels,predictions)
    s = mae(labels,predictions)
    r =r2(labels,predictions)
    return score,s,r


def ansatz(v):
    qml.Rotation(v[0], wires=0)
    qml.Squeezing(v[1], 0, wires=0)
    qml.Rotation(v[2], wires=0)
    qml.Displacement(v[3], 0, wires=0)
    qml.Kerr(v[4], wires=0)
    

@qml.qnode(dev)
def qnn(var, x=None):
    
    # Encoding the volt and intensity into quantum states
    qml.DisplacedSqueezedState(x[0], 0,x[1],0, wires=0)

    for v in (var):
        ansatz(v)

    return qml.expval(qml.X(0))

def testing(var,features):
    result = []
    for i in range(len(features)):
        preds = qnn(var,x=features[i])
        result.append(preds)
    return np.array(result).reshape(-1,1)

def next_batch(X, y, batchSize):
    rem = len(X)//batchSize
    out = len(X)%batchSize
    # loop over our dataset `X` in mini-batches of size `batchSize`
    for id ,i in enumerate(np.arange(0, X.shape[0], batchSize)):
        # yield a tuple of the current batched data and labels
        if id == rem and out != 0:
            temp = abs(batchSize-out)
            d = X[i:i + batchSize]
            l = y[i:i + batchSize]
            batch = np.random.choice(622,temp,replace=False)
            
            dd,ll = X[batch],y[batch]

            return (np.vstack((d,dd)),np.vstack((l.reshape(-1,1),ll.reshape(-1,1))))
        yield (X[i:i + batchSize], y[i:i + batchSize])
        
def data_preparation():
    
    data = pd.read_csv('data.csv')

    features = data.drop('I', axis=1).values
    I = data.I.values
    
    I = data.I.values*1000
    
    X_train, X_test, y_train, y_test = train_test_split(features,I,
                                                        test_size=0.15,random_state=0)
    
    Volt = X_train[:,0:1]
    Inten = X_train[:,1:]
    
    disp_scale = MinMaxScaler(feature_range=(-1.1,1)).fit(Volt)
    
    squeeze_scale = MinMaxScaler(feature_range=(0,0.8)).fit(Inten)
    
    X_train[:,0:1] = disp_scale.transform(X_train[:,0:1])
    X_train[:,1:] = squeeze_scale.transform(X_train[:,1:])
    
    X_test[:,0:1] = disp_scale.transform(X_test[:,0:1])
    X_test[:,1:] = squeeze_scale.transform(X_test[:,1:])
    
    return X_train, X_test, y_train, y_test
    
    