import numpy as np

class Heap :

    def __init__(self, heap_list):
        self.heap_list=heap_list
        heap_list=[]

    def get_left_child(self, i):
        assert(len(self.heap_list)>=2*i+1)
        return 2*i+1

    def get_right_child(self, i):
        assert(len(self.heap_list)>=2*i+2)
        return 2*i+2

    def get_parent(self,i):
        assert(i>0)
        return (i-1)//2

    def swap(self,i,j):
        assert (i<len(self.heap_list))
        assert (j<len(self.heap_list))
        self.heap_list[i],self.heap_list[j] = self.heap_list[j],self.heap_list[i]
        return self.heap_list

    def percolate_up(self, n_index):
        print(str(n_index))
        if n_index==0:
            n_index=self.heap_list.index(self.heap_list[-1])
        if self.heap_list[n_index]<self.heap_list[self.get_parent(n_index)]:
            self.swap(n_index, self.get_parent(n_index))
            return self.percolate_up(self.get_parent(n_index))
        return self.heap_list

    def insert(self,n):
        self.heap_list.append(n)
        self.percolate_up(self.heap_list.index(n))
        return self.heap_list

    def min_child(self,i):
        min=0
        if self.get_left_child(i)<self.get_right_child(i):
            min=self.get_left_child(i)
        else:
            min=self.get_right_child(i)


    def percolate_down(self, i):

        if self.heap_list[self.min_child(i)]<=self.heap_list[i]:
            self.swap(i, self.min_child(i))
            return self.percolate_down(self.min_child(i))
        return self.heap_list



    def extract(self):
        self.heap_list.remove(self.heap_list[0])
        last=self.heap_list.pop()
        self.heap_list=[last]+self.heap_list
        self.percolate_down(0)




tas=Heap([1,5,8,3])

print(tas.extract())
