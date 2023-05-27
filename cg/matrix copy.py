# import vector



def __dot_product_2(la,lb):
    # 两个向量 内积
    la = la[0]
    lbc = list()
    for i,ele in enumerate(lb):
        lbc.append(ele[0])
    
    lb = lbc

    out = 0
    for i in range(len(la)):
        ae = la[i]
        be = lb[i]

        # print('ae,be',ae,be)
        out+=ae*be
    return out

def dot_product(ma,mb):
    
    # ma  l行 m列
    # mb m行 n列
    l = len(ma)
    # m = len(ma[0])
    n = len(mb[0])

    out = list()
    # out有l行，n列
    # for i in range(l):
    #     out .append(list())
    
    for i in range(l):
        xa = [ ma[i] ]
        ro = list()
        for j in range(n):
            xb = self.get_column(mb,j)

            # print(xa,xb)

            x = self.__dot_product_2(xa,xb)
            ro.append(x)
        out.append(ro)

    return out




class matrix():


    # def 
    
    def get_column(self,matrix,column_num):
        column = list()
        for _,row in enumerate(matrix):
            ele = row[column_num]
            ro = [ele]
            column.append(ro)
        return column
    

    

    


    def soft_max(self,matrix):
        out = list()

        # m = len(matrix) # m 行
        # out = list()
        # for _ in range(m):
        #     out.append(list())
        
        up = 2**3
        bottom = -up
        base = 2    #计算幂用的底
        
        for i,row in enumerate(matrix):
            ro = list() # 输出矩阵的行
            for k,cik in enumerate(row):

                # ci = ele
                sum_eik = 0 # 分母
                fik = 0 # 输出矩阵的某个元素
                br = 0
                for i_1,row_1 in enumerate(matrix):
                    for k_1 ,cik_1 in enumerate(row_1):
                    # cik_0 是本值 ，cik_1是对方值
                    
                        dik = cik_1-cik
                        if(dik>up):
                            fik = 0  # 本值太小，权重为0，不必再算了
                            br = 1
                            break
                        else:
                            if(dik<bottom):
                                eik = 0
                            else:
                                eik = base**dik
                            sum_eik += eik
                    if(br ==1):break

                if(br ==1):
                    fik = 0
                else:
                    fik = 1/sum_eik

                
                ro.append(fik)
            out.append(ro)
        return out
    
    def __str__(self,matrix):
        out = ''
        

    def print(self,matrix):
        print('[')
        for i,row in enumerate(matrix):
            print('\t',row)
        print(']')
        return

