# 向量 vector 就是 [] 无所谓 行还是列，无所谓是竖的还是横的
# 向量有内积 软大 变成矩阵 乘标量
# 向量转成矩阵就变成了行向量

# 矩阵 

# 行向量是 1行 n列的矩阵 
# 列向量是 m行 1列的矩阵

# 矩阵的方法
# 矩阵相乘，矩阵提取列向量（输出为向量vector）,转置，打印，矩阵乘标题




class self_attention():

    def matrix_get_column(self,matrix,column_num):
        column = list()
        for _,row in enumerate(matrix):
            column.append(row[column_num])
        return column
    

    def matrix_mp(self,ma,mb):
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
            xa = ma[i]
            ro = list()
            for j in range(n):
                xb = self.matrix_get_column(mb,j)
                x = self.dot_product(xa,xb)
                ro.append(x)
            out.append(ro)

        return out

    def matrix_mp_num(self,num_a,mb):
        # 矩阵乘标量
        # m = len(mb)
        out = list()
        for i,row in enumerate(mb):
            ro = list()
            for j,ele in enumerate(row):
                d = num_a*ele
                ro.append(d)
            out.append(ro)
        return out
    




    def dot_product(self,la,lb):
        # 两个向量 内积
        out = 0
        for i in range(len(la)):
            ae = la[i]
            be = lb[i]
            out+=ae*be
        return out

    def vector_mp_num(self,a,lb):
        c = list()
        for i,ele in enumerate(lb):
            d = a*ele
            c.append(d)
        return c


    def soft_max(self,vector):
        out = list()
        
        up = 2**3
        bottom = -up

        base = 2    #计算幂用的底
        
        for i,ci in enumerate(vector):
            # ci = ele
            sum_ej = 0
            fi = 0
            br = 0
            for _,cj in enumerate(vector):
                # ci是本值 ，cj是对方值
                
                dj = cj-ci
                if(dj>up):
                    fi = 0  # 本值太小，权重为0，不必再算了
                    br = 1
                    break
                else:
                    if(dj<bottom):
                        ej = 0
                    else:
                        ej = base**dj
                    sum_ej += ej

            if(br ==1):
                fi = 0
            else:
                fi = 1/sum_ej

            out.append(fi)
        return out
    
    def matrix_trans(self,matrix):
        # 矩阵转置
        # m行 n列
        m = len(matrix)
        n = len(matrix[0])
        out = list()
        for i in range(n):
            out.append(list())  # 原来有n列，后来就有n行
        for _,row in enumerate(matrix):
            for j ,ele in enumerate(row):
                out[j].append(ele)


        return out

    def print_matrix(self,matrix):
        print('[')
        for i,row in enumerate(matrix):
            print('\t',row)
        print(']')
        return

    def vector_to_matrix(self,list_a):
        out = list()
        out.append(list_a)
        return out

    def main(self):
        in_put = list()
        # n = 5 m = 1 l = 1
        in_put = [[3,2,4,5,1],[1,3,4,3,2]]

        wq = [[0.8,2.1]]
        wk = [[1.1,1]]
        wv = [[20,1]]

        q = self.matrix_mp(wq,in_put)
        k = self.matrix_mp(wk,in_put)
        v = self.matrix_mp(wv,in_put)

        # v = [v]
        # print(k,q,v)

        self.print_matrix(q)
        self.print_matrix(k)
        self.print_matrix(v)
        # k = self.vector_to_matrix(k)
        k = self.matrix_trans(k)
        # q = self.vector_to_matrix(q)
        a = self.matrix_mp(k,q)


        # a = self.mp3(k,q)
        self.print_matrix(a)
        # print(a)

        # print(a0)

        # a0 = [2,2,-30,4]

        # print(sa0)

        # 把a的每列计算soft_max，然后拼装成at，作为注意力权重
        at = list()
        for i ,ele in enumerate(a): # a的列数，但a行数=列数，所以这里直接用行数

            a0 = self.matrix_get_column(a,i)
            sa0 = self.soft_max(a0)
            at.append(sa0)

        at = self.matrix_trans(at)
        self.print_matrix(at)



        b = self.matrix_mp(v,at)
        self.print_matrix(b)


        return

    def __init__(self):
        self.main()



if __name__ == '__main__':
    self_attention()