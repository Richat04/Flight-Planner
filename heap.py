'''
Python Code to implement a heap with general comparison function
'''


def comp1(a,b):             # a and b are crewmates
    if a[0]<b[0]:
        return True
    else:
        return False
    
def comp2(a,b):
    
    if a[0] < b[0]:
        return True
    elif a[0] > b[0]:
        return False
    else:
        if a[1] < b[1]:
            return True
        else:
            return False
      

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    def __init__(self, comparison_function, init_array):

        self.heap = init_array
        self.comparator = comparison_function
        self.build_heap()
        
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        
        
    def insert(self, value):
        
        # Arguments:value : Any : The value to be inserted into the heap
        # Returns:None
        # Description:Inserts a value into the heap
        # Time Complexity:O(log(n)) where n is the number of elements currently in the heap
        # Write your code here
        self.heap.append(value)
        self.upheap(len(self.heap)-1)
        # print("MYYY ", self.heap)
       
    
    def extract(self):
        # Arguments:None
        # Returns:Any : The value extracted from the top of heap
        # Description:Extracts the value from the top of heap, i.e. removes it from heap
        # Time Complexity:O(log(n)) where n is the number of elements currently in the heap
        
        
        # Write your code here
        if len(self.heap)== 0:
            return None
        else:
            val = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            self.heap.pop()
            # print("leloleoleo", self.heap[0])
            self.downheap(0)
            # print("HIIIII  ", self.heap)
            return val
    
    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]
        
            # Arguments: None
            # Returns: Any : The value at the top of heap
            # Description: Returns the value at the top of heap
            # Time Complexity: O(1)'''
        
        # Write your code here
        
    # You can add more functions if you want to

    def downheap(self,i):                        #here key is the index #using min heap function
        left = (2*i)+1
        right = (2*i)+2
        smallest = i
        if right < len(self.heap) and self.comparator(self.heap[right], self.heap[smallest]):
            smallest = right
        if left < len(self.heap) and self.comparator(self.heap[left], self.heap[smallest]):
            smallest = left
        
        if smallest!=i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.downheap(smallest)

    def build_heap(self):
        for i in range(len(self.heap)//2 -1,-1,-1):
            self.downheap(i)

    def upheap(self, i):      #for insert operation
        parent = (i-1)//2
        while i>0 and self.comparator(self.heap[i], self.heap[parent]):
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            i = parent
            parent = (i-1)//2

    def print_heap(self):
        print(self.heap)

    def length(self):
        return len(self.heap)
    
    def l(self,i):
        left = (2*i)+1
        return left
    
    def r(self,i):
        ri = (2*i)+2
        return ri
    
    def p(self,i):
        pa = i//2
        return pa




# l=[None]*5
# for i in range(5):
#     if l[i] == None:
#         l[i] = [i]
#     else:
#         l[i].append(i)
# print(l)