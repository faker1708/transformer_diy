


class self_attention():

    def matrix_get_column(self,matrix,column_num):
        column = list()
        for _,row in enumerate(matrix):
            column.append(row[column_num])
        return column

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

    def mp2(self,la,lb):
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
        
        for i,ci in enumerate(vector):
            # ci = ele
            sum_ej = 0
            fi = 0
            br = 0
            for j,cj in enumerate(vector):
                dj = cj-ci
                if(dj>up):
                    fi = 0  # 本值太小，权重为0，不必再算了
                    br = 1
                    break
                else:
                    if(dj<bottom):
                        ej = 0
                    else:
                        ej = 2**dj
                    sum_ej += ej

            if(br ==1):
                fi = 0
            else:
                fi = 1/sum_ej

            out.append(fi)
        return out

    def main(self):
        in_put = list()
        # n = 5 m = 1 l = 1
        in_put = [3,2,4,22,74]

        wq = 1
        wk = 2
        wv = 3

        q = self.mp(wq,in_put)
        k = self.mp(wk,in_put)
        v = self.mp(wv,in_put)

        print(k,q,v)

        a = self.mp3(k,q)
        print(a)

        a0 = self.matrix_get_column(a,0)
        print(a0)

        a0 = [2,2,-30,4]

        sa0 = self.soft_max(a0)
        print(sa0)
        return

    def __init__(self):
        self.main()



if __name__ == '__main__':
    self_attention()