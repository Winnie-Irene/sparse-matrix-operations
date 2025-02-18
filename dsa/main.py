# main.py
# Entry point for performing operations on sparse matrices

from sparse_matrix import SparseMatrix

def main():
    print("Sparse Matrix Operations")

if __name__ == "__main__":
    main()

from sparse_matrix import SparseMatrix

def main():
    print("Sparse Matrix Operations")
    operation = input("Enter operation (add/subtract/multiply): ")

    file1 = input("Enter the path of the first matrix file: ")
    file2 = input("Enter the path of the second matrix file: ")

    matrix1 = SparseMatrix(matrixFilePath=file1)
    matrix2 = SparseMatrix(matrixFilePath=file2)

    if operation == 'add':
        result = matrix1.add(matrix2)
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation")
        return

    result_file = input("Enter the path to save the result matrix: ")
    result.save_to_file(result_file)

if __name__ == "__main__":
    main()