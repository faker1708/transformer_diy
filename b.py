import torch
import torch.nn.functional as F

class b_class():

    def new_tensor(self,list:list):
        device = torch.device('cpu')
        
        if(self.cuda_on):
            if( torch.cuda.is_available()   ):
                device = torch.device('cuda')

        # self.device=
        a = torch.tensor( list).to(device)
        return a


    def main(self):
        self.cuda_on = 0
        # a = self.new_tensor([[3.,2,4,5,1],[1,3,4,3,2]])
        a = self.new_tensor([[3.,2,3,3,1],[1,3,4,3,2]])
        print(a.device)
        # print(torch.cuda.is_available() )
        print(a)
        print(a.dtype)

        


        # wq = self.new_tensor([[2.,4],[5,1],[6,4]])
        # wq = self.new_tensor([[0.2,0.4],[0.1,0.1],[0.6,0.4]])
        wq = self.new_tensor([[0.02,0.04],[0.01,0.01],[0.06,0.04]])
        wk = self.new_tensor([[0.02,0.04],[0.01,0.01],[0.06,0.04]])
        wv = self.new_tensor([[0.02,0.04],[0.01,0.01],[0.06,0.04]])
        wv = self.new_tensor([[0.02,0.04],[0.01,0.01],[0.06,0.04],[0.02,0.09]])
        # wv = self.new_tensor([[0.2,0.4],[0.1,0.1],[0.6,0.4]])
        # wv = self.new_tensor([[2.,4],[5,1],[6,4]])

        q = wq @ a
        k = wk @ a
        v = wv @ a




        kt = k.permute(1,0)

        print(q)
        print('kt',kt)
        print(v)
        
        a = kt @ q

        print('\na',a)
        a = a/3**0.5

        
        print('\na',a)
        ap = F.softmax(a,dim=0)
        # print(k)
        print('ap',ap)

        b = v @ ap
        print(b)


        return
    def __init__(self):
        self.main()

    
if __name__ == '__main__':
    b_class()