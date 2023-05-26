


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
        m = len(ma[0])
        n = len(mb[0])

        out = list()
        # out有l行，n列
        # for i in range(l):
        #     out .append(list())
        
        for i in range(l):
            xa = ma[i]
            ro = out[i]
            for j in range(m):
                xb = self.matrix_get_column(mb,j)
                x = self.dot_product(xa,xb)
                ro.append(x)

        return out



    def mp3(self,la,lb):
        # 向量相乘得矩阵

        matrix = list()

        n = len(la)
        m = len(lb)
        # for i,ele in enumerate()
        for i in range(n):
            row = list()
            for j in range(m):
                a = la[i]*lb[j]
                row.append(a)
            matrix.append(row)
        return matrix

    def dot_product(self,la,lb):
        # 内积
        out = 0
        for i in range(len(la)):
            ae = la[i]
            be = lb[i]
            out+=ae*be
        return out

    def mp(self,a,lb):
        c = list()
        for i,ele in enumerate(lb):
            d = a*ele
            c.append(d)
        return c


    def soft_max(self,vector):
        out = list()
        
        up = 10
        bottom = -10

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

    def list_to_matrix(self,list_a):
        out = list()
        out.append(list_a)
        return out

    def main(self):
        in_put = list()
        # n = 5 m = 1 l = 1
        in_put = [3,2,4,5,1]

        wq = 1
        wk = 2
        wv = 3

        q = self.mp(wq,in_put)
        k = self.mp(wk,in_put)
        v = self.mp(wv,in_put)

        v = [v]
        print(k,q,v)

        a = self.mp3(k,q)
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

        # at = [[1,2,55],[3,4,66]]
        self.print_matrix(at)
        # print(at)
        at = self.matrix_trans(at)
        # print(at)
        self.print_matrix(at)


        return

    def __init__(self):
        self.main()



if __name__ == '__main__':
    self_attention()