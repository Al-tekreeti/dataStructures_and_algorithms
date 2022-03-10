class MaxHeap:
    def __init__(self):
        self.arr = []

    def size(self):
        return len(self.arr)
    
    def heapify(self, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2 
        
        if l < self.size() and self.arr[i] < self.arr[l]:
            largest = l
        
        if r < self.size() and self.arr[largest] < self.arr[r]:
            largest = r
        
        if largest != i:
            self.arr[i],self.arr[largest] = self.arr[largest],self.arr[i]
            self.heapify(largest)

    def insert(self, val):
        self.arr.append(val)
        if self.size() > 1:
            for i in range((self.size()//2)-1, -1, -1):
                self.heapify(i)

    def delete(self, val):
        i = 0
        for i in range(0, self.size()):
            if val == self.arr[i]:
                break
            
        self.arr[i], self.arr[-1] = self.arr[-1], self.arr[i]

        self.arr.remove(val)
        
        for i in range((self.size()//2)-1, -1, -1):
            self.heapify(i)

    def peek(self):
        return self.arr[0]
    
    def extract_max(self):
        max_val = self.arr[0]
        self.delete(max_val)
        return max_val

if __name__ == "__main__":
    mheap = MaxHeap()

    mheap.insert(3)
    mheap.insert(4)
    mheap.insert(9)
    mheap.insert(5)
    mheap.insert(2)

    print ("Max-Heap array: " + str(mheap.arr))

    #mheap.delete(4)
    print(mheap.extract_max())
    print("After deleting an element: " + str(mheap.arr))
