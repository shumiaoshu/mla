import pandas as pd
import numpy as np
import queue

class TreeNode:
    def __init__(self):
        self.label = None
        self.choose_feature = None
        self.pros = None
        self.next_nodes = {}
        self.alternative_features = None # 可选择分支特征，包括自己
        self.father = None
        self.samples = []

class DecisionTree:
    def __init__(self,datafile,label_col,features_col,num_features_col):
        self.datafile = datafile
        self.label_col = label_col
        self.num_features_col = num_features_col
        self.label = None
        self.features = None
        self.features_col = features_col
        self.num_value_features = []
        self.str_features = None
        self.data = self.parsedata()

    def construct_tree(self):
        pass

    def get_root(self):
        rootNode = TreeNode()
        rootNode.samples = self.data
        rootNode.alternative_features = self.str_features



    def parsedata(self):
        dataf = pd.read_csv(self.datafile)
        columns = [column for column in dataf]
        self.label = columns[self.label_col]
        self.features = columns[self.features_col[0]:self.features_col[1]]
        for col_num in self.num_features_col:
            self.num_value_features.append(columns[col_num])
        self.str_features = [feature for feature in self.features if feature not in self.num_value_features]
        self.data = dataf

    def cal_gini(self):
        pass

    def pred(self,samples):
        pass

    def pre_test(self,samples):
        pass


if __name__ == "__main__":
    DecisionTree('data3.0.csv',-1,[1,-1],[7,8])