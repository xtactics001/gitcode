# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:42:17 2018

@author: yjq13
"""

class neuralNetwork:
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        
        self.lr = learningrate
        
        self.wih = np.random.rand(self.hnodes, self.inodes) - 0.5
        self.who = np.random.rand(self.onodes, self.hnodes) - 0.5
        # 也可以使用  np.random.normal 初始化权重值
        
        self.actication_function = lambda x: scipy.special.expit(x)
    
    def train():
        pass
    
    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T
        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.actication_function(hidden_inputs)
        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.actication_function(final_inputs)
        
        return final_outputs