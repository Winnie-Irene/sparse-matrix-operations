# sparse_matrix.py
# SparseMatrix class for performing matrix operations

class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        # Initialization code here
        pass

    def getElement(self, currRow, currCol):
        pass

    def setElement(self, currRow, currCol, value):
        pass

class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = {}  # Dictionary to store non-zero elements (row, col): value

        if matrixFilePath:
            self.load_from_file(matrixFilePath)

    def load_from_file(self, matrixFilePath):
        with open(matrixFilePath, 'r') as file:
            lines = file.readlines()

            # Read rows and columns from the first two lines
            self.numRows = int(lines[0].split('=')[1].strip())
            self.numCols = int(lines[1].split('=')[1].strip())

            # Process the rest of the lines for non-zero entries
            for line in lines[2:]:
                line = line.strip()
                if line:
                    if line.startswith('(') and line.endswith(')'):
                        row, col, value = map(int, line[1:-1].split(','))
                        if value != 0:
                            self.elements[(row, col)] = value
                    else:
                        raise ValueError("Input file has wrong format")

    def getElement(self, currRow, currCol):
        return self.elements.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        if value == 0:
            if (currRow, currCol) in self.elements:
                del self.elements[(currRow, currCol)]
        else:
            self.elements[(currRow, currCol)] = value

    # Add more functions for matrix operations (addition, subtraction, multiplication)

def add(self, other):
    if self.numRows != other.numRows or self.numCols != other.numCols:
        raise ValueError("Matrices must have the same dimensions for addition")

    result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)

    # Add non-zero elements from both matrices
    for (row, col), value in self.elements.items():
        result.setElement(row, col, value + other.getElement(row, col))

    for (row, col), value in other.elements.items():
        if (row, col) not in self.elements:
            result.setElement(row, col, value)

    return result

def subtract(self, other):
    if self.numRows != other.numRows or self.numCols != other.numCols:
        raise ValueError("Matrices must have the same dimensions for subtraction")

    result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)

    # Subtract non-zero elements from both matrices
    for (row, col), value in self.elements.items():
        result.setElement(row, col, value - other.getElement(row, col))

    for (row, col), value in other.elements.items():
        if (row, col) not in self.elements:
            result.setElement(row, col, -value)

    return result

def multiply(self, other):
    if self.numCols != other.numRows:
        raise ValueError("Number of columns of the first matrix must equal the number of rows of the second matrix")

    result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)

    for (row, col), value in self.elements.items():
        for k in range(other.numCols):
            result.setElement(row, k, result.getElement(row, k) + value * other.getElement(col, k))

    return result