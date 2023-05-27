# 向量 vector 就是 [] 无所谓 行还是列，无所谓是竖的还是横的
# 向量有内积 软大 变成矩阵 乘标量
# 向量转成矩阵就变成了行向量

# 矩阵 

# 行向量是 1行 n列的矩阵 
# 列向量是 m行 1列的矩阵

# 矩阵的方法
# 矩阵相乘，矩阵提取列向量（输出为向量vector）,转置，打印，矩阵乘标题

import matrix
# import vector


class self_attention():



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


    def main(self):
        in_put = list()
        # n = 5 m = 1 l = 1
        in_put = [[3,2,4,5,1],[1,3,4,3,2]]

        wq = [[0.8,2.1]]
        wk = [[1.1,1]]
        wv = [[20,1]]

        q = matrix.dot_product(wq,in_put)
        k = matrix.dot_product(wk,in_put)
        v = matrix.dot_product(wv,in_put)

        # v = [v]
        # print(k,q,v)

        self.print_matrix(q)
        self.print_matrix(k)
        self.print_matrix(v)
        k = self.matrix_trans(k)
        a = matrix.dot_product(k,q)


        # a = self.mp3(k,q)
        # self.print_matrix(a)
        # a.print()
        print(a)
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



        b = matrix.dot_product(v,at)
        self.print_matrix(b)


        return

    def __init__(self):
        self.main()



if __name__ == '__main__':
    self_attention()