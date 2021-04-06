text = '''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit'''

text_transpose = '''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line
'''


def read_matrix():
    s = input('Enter size of matrix: ')
    s = s.split()
    m, n = int(s[0]), int(s[1])
    matrix = []
    print('Enter matrix:')
    for i in range(m):
        s = input()
        s = s.split()
        matrix.append([])
        for j in s:
            matrix[i].append(float(j))

    return Matrix(matrix)


def print_matrix(matrix):
    for line in matrix:
        for x in line:
            print(x, end=' ')
        print()


class Matrix:
    def __init__(self, matrix):
        self._matrix = matrix
        self._m = len(matrix)
        self._n = len((matrix[0]))

    @property
    def matrix(self):
        return self._matrix

    def __add__(self, other):
        if self._m != len(other.matrix) or self._m != len(other.matrix[0]):
            print("The operation cannot be performed.")
            return None

        result = []
        for line1, line2 in zip(self._matrix, other.matrix):
            result.append([el1 + el2 for el1, el2 in zip(line1, line2)])
        return Matrix(result)

    def __mul__(self, scalar):
        result = [*map(lambda line: [*map(lambda x: scalar * x, line)], self._matrix)]
        return Matrix(result)

    def __neg__(self):
        return self * -1

    def transpose(self):
        trans = []
        for i in range(self._n):
            trans.append([])
            for j in range(self._m):
                trans[i].append(self._matrix[j][i])
        self._matrix = trans
        return self

    def transpose_second_diagonal(self):
        self._matrix.reverse()
        self.transpose()
        self._matrix.reverse()
        return self

    def transpose_horizontal(self):
        self._matrix.reverse()
        return self

    def transpose_vertical(self):
        for line in self._matrix:
            line.reverse()
        return self

    def mul(self, other):
        if self._n != len(other.matrix):
            print('The operation cannot be performed.')
            return None
        aux = other.transpose().matrix
        result = []
        for line1 in self._matrix:
            result.append([])
            for line2 in aux:
                result[-1].append(sum([el1 * el2 for el1, el2 in zip(line1, line2)]))

        return Matrix(result)

    def minor(self, i, j):
        minor = [line.copy() for line in self._matrix]
        minor.pop(i)
        for line in minor:
            line.pop(j)

        return Matrix(minor)

    def cofactor(self, i, j):
        return (-1) ** (2 + i + j) * self.minor(i, j).determinant()

    def determinant(self):
        if self._n != self._m:
            print('Invalid operation')
            return None
        if self._n == 1:
            return self._matrix[0][0]

        if self._n == 2:
            return self._matrix[0][0] * self._matrix[1][1] - self._matrix[0][1] * self._matrix[1][0]

        det = 0
        for j in range(self._n):
            det += (-1) ** (2 + j) * self.minor(0, j).determinant() * self._matrix[0][j]
        return det

    def adjugate(self):
        adjugate = []
        for i in range(self._m):
            adjugate.append([self.cofactor(i, j) for j in range(self._n)])
        return Matrix(adjugate)

    def inverse(self):
        det = self.determinant()
        if det == 0:
            print("This matrix doesn't have an inverse")
            return None
        return self.adjugate().transpose() * (1 / det)

    def __str__(self):
        s = ''.join((''.join((str(x) + ' ') for x in line) + '\n') for line in self._matrix)
        return s[0: len(s) - 1]


def main():
    while True:
        print(text)
        s = input('Your choice: ')
        if not s.isdigit() and 0 <= int(s) <= 4:
            print('Invalid input')
            continue
        x = int(s)
        if x == 0:
            exit()
        if x == 1:
            A = read_matrix()
            B = read_matrix()
            C = A + B
            if C is not None:
                print(f'The result is:\n{C}')
        elif x == 2:
            A = read_matrix()
            a = float(input('Enter constant: '))
            B = A * a
            if B is not None:
                print(f'The result is:\n{B}')
        elif x == 3:
            A = read_matrix()
            B = read_matrix()
            C = A.mul(B)
            if C is not None:
                print(f'The result is:\n{C}')
        elif x == 4:
            print(text_transpose)
            s = input('Your choice: ')
            if not s.isdigit() and 0 <= int(s) <= 4:
                print('Invalid input')
                continue

            A = read_matrix()
            if s == '1':
                A.transpose()
            elif s == '2':
                A.transpose_second_diagonal()
            elif s == '3':
                A.transpose_vertical()
            elif s == '4':
                A.transpose_horizontal()
            print(f'The result is:\n{A}')

        elif x == 5:
            A = read_matrix()
            det = A.determinant()
            print(det)
        elif x == 6:
            A = read_matrix()
            inv_A = A.inverse()
            if inv_A is not None:
                print(f'The result is: \n{inv_A}')


if __name__ == '__main__':
    main()
