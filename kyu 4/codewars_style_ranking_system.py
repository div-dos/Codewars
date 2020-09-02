class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, rank):
        value = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        if rank not in value:
            raise IndexError
        
        diff = 0
        #calculate the progress
        if self.rank == rank:
        #    print('cond: 1')
            diff = 3
            self.progress +=3
        elif self.rank == rank+1 and ((rank < 0 and self.rank < 0) or (rank > 0 and self.rank > 0)):
        #    print('cond: 2')
            diff = 1
            self.progress +=1
        elif self.rank == rank+2 and (self.rank > 0 and rank <0):
        #    print('cond: 5')
            diff = 1
            self.progress += 1
        elif self.rank < rank and ((rank < 0 and self.rank < 0) or (rank > 0 and self.rank > 0)):
        #    print('cond: 3')
            diff = abs(self.rank - rank)*abs(self.rank - rank) * 10
            self.progress += abs(self.rank - rank)*abs(self.rank - rank) * 10
        elif self.rank < rank and (rank > 0 and self.rank < 0):
        #    print('cond: 4')
            diff = abs(self.rank - rank +1)*abs(self.rank - rank +1) *10
            self.progress += abs(self.rank - rank +1)*abs(self.rank - rank +1) *10
        
        #print(diff)
        
            
        while self.progress >= 100:
            if -8 <= self.rank <-1:
                self.rank += 1
            elif self.rank == -1:
                self.rank +=2
            elif 1<= self.rank<8:
                self.rank += 1
            elif self.rank == 8:
                self.progress = 0
                break
            
            self.progress -= 100
            
        if self.rank == 8:
            self.progress = 0