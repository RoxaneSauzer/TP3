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
        assert (i<=len(self.heap_list))
        assert (j<=len(self.heap_list))
        self.heap_list[i],self.heap_list[j] = self.heap_list[j],self.heap_list[i]
        return self.heap_list

    def percolate_up(self, n_index):
        if len(self.heap_list)==1:
            return self.heap_list
        if n_index==0:
            n_index=len(self.heap_list)-1
        if self.heap_list[n_index]<self.heap_list[self.get_parent(n_index)]:
            a= self.get_parent(n_index)
            self.swap(n_index, self.get_parent(n_index))
            return self.percolate_up(a)
        return self.heap_list

    def insert(self,n):
        self.heap_list.append(n)
        self.percolate_up(self.heap_list.index(n))
        return self.heap_list

    def min_child(self,i):
        min=0
        if len(self.heap_list)<2*i+1:
            print('no child to compare')
        if self.heap_list[self.get_left_child(i)]<self.heap_list[self.get_right_child(i)]:
            min=self.get_left_child(i)
        else:
            min=self.get_right_child(i)
        return min


    def percolate_down(self, i):
        print(i)

        if len(self.heap_list)<2*i+1:
            print('no child to compare')
            return self.heap_list
        print(self.min_child(i))
        if self.heap_list[self.min_child(i)]<=self.heap_list[i]:
            a= self.min_child(i)
            self.swap(i, self.min_child(i))
            print(self.heap_list)
            return self.percolate_down(a)
        return self.heap_list


    def extract(self):
        self.swap(0,len(self.heap_list)-1)
        self.heap_list.pop()
        return self.percolate_down(0)

    def delete(self, i):
        new_list=[]
        for k in range(i, len(self.heap_list)):
            print(self.heap_list[k])
            new_list.append(self.heap_list[k])

        for k in range(len(new_list)):
            self.heap_list.pop()
        tas=Heap(new_list)
        print(tas.heap_list)
        tas.extract()
        for k in range(len(new_list)):
            self.heap_list.append(tas.heap_list[k])
        return self.heap_list


    def build(self, list):
        self.heap_list=[]
        for i in list:
            self.insert(i)
        return self.heap_list


l=[1,4,2,3,5]
tas=Heap([])
print(tas.build(l))
