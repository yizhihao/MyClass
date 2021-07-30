# -*- coding: utf-8 -*-
# 二叉搜索树

from pyecharts.charts import Tree

class BstNode:
    # 每个节点有三个属性，自身值以及左右枝
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        
    def grow(self,value):
        self.value=value
        self.left=BstNode()
        self.right=BstNode()
    
class BST:
    def __init__(self,root=None):
        # 初始化根节点
        if root is None:
            self.root=BstNode()
        else:
            self.root=root
    
    def fmax(self):
        # 以根节点为起点，寻找树中最大的分支节点
        if self.root.value is None:
            return None
        else:
            return self.__find_max(self.root)
    def __find_max(self,node):
        if node.right.value is None:
            return node.value
        else:
            return self.__find_max(node.right)
            
    def fmin(self):
        # 以根节点为起点，寻找树中最小的分支节点
        if self.root.value is None:
            return None
        else:
            return self.__find_min(self.root)
    def __find_min(self,node):
        if node.left.value is None:
            return node.value
        else:
            return self.__find_min(node.left)  
    
    def depth(self):
        # 以根节点为起点，计算树的最大深度
        return self.__depth_node(self.root)
    def __depth_node(self,node):
        if node.value is None:
            return 0
        else:
            return max(self.__depth_node(node.left),self.__depth_node(node.right))+1
            
    def insert(self,value):
        # 以根节点为起点，将新数插入树中
        self.__insert_node(value,self.root)
    def __insert_node(self,value,node):
        if node.value is None:
            node.grow(value)
        elif value<node.value:
            if node.left.value is None:
                node.left.grow(value)
            else:
                self.__insert_node(value,node.left)
        elif value>node.value:
            if node.right is None:
                node.right.grow(value)
            else:
                self.__insert_node(value,node.right)
                
    def remove(self,value):
        # 以根节点为起点，将指定数从树中移除
        if self.root.value is not None:
            self.__remove_node(value,self.root)
    def __remove_node(self,value,node):
        if (value<node.value) and (node.left.value is not None):
            self.__remove_node(value,node.left)
        elif (value>node.value) and (node.right.value is not None):
            self.__remove_node(value,node.right)
        elif value==node.value:
            node.value=None
            if (node.left.value is None) and (node.right.value is None):
                del node.left,node.right
            else:
                dl=self.__depth_node(node.left)
                dr=self.__depth_node(node.right)
                if dl>dr:  # 从较深的分支中提取节点来替换剔除节点
                    nvalue=BST(node.left).fmax() # 寻找替换值
                    self.__remove_node(nvalue,node.left) # 并将该值从该分支中剔除
                else:
                    nvalue=BST(node.right).fmin()
                    self.__remove_node(nvalue,node.right)
                node.value=nvalue
            
    def show_list(self):
        # 以根节点为起点，将树中的数从小到大输出成列表
        list_tree=[]
        self.__list_node(self.root,list_tree)
        return list_tree
    def __list_node(self,node,list_tree):
        if node.value is not None:
            self.__list_node(node.left,list_tree)
            list_tree.append(node.value)
            self.__list_node(node.right,list_tree)

    def show_tree(self,filename):
        # 以根节点为起点，将树中的数以树结构输出
        struct_tree=[]
        if self.root.value is not None:
            self.__tree_node(self.root,struct_tree)
        Tree().add("", struct_tree,orient="TB").render(filename+".html")
        return struct_tree
    def __tree_node(self,node,struct_tree):
        dict_tree={}
        dict_tree['name']=node.value
        if (node.left.value is not None) or (node.right.value is not None):
            children=[]
            if node.left.value is None:
                children.append({'name':'None'})
                self.__tree_node(node.right,children)
            elif node.right.value is None:
                self.__tree_node(node.left,children)
                children.append({'name':'None'})
            else:
                self.__tree_node(node.left,children)
                self.__tree_node(node.right,children)
            dict_tree['children']=children
        struct_tree.append(dict_tree)
        

if __name__=='__main__':
    mytree=BST()
    for i in [60,12,90,4,41,71,100,1,29,84,23,37]:
        mytree.insert(i)
        # mytree.show_list()
        # struct_tree=mytree.show_tree('BaseTree')