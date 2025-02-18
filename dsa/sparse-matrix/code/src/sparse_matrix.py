class SparseMatrix:
    def __init__(self, filename):
        self.data = {}  
        self.num_rows = 0
        self.num_cols = 0
        self.read_from_file(filename)

    def read_from_file(self, filename):
        """Reads the sparse matrix from a file and stores it in dictionary format."""
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                
               
                self.num_rows = int(lines[0].split('=')[1].strip())
                self.num_cols = int(lines[1].split('=')[1].strip())

                
                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue
                    
                    if not line.startswith("(") or not line.endswith(")"):
                        raise ValueError("Invalid format in file.")

                   
                    row, col, value = map(int, line[1:-1].split(','))
                    self.data[(row, col)] = value  

        except FileNotFoundError:
            print("Error: File not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def get_element(self, row, col):
        """Returns the value at (row, col), or 0 if not found."""
        return self.data.get((row, col), 0)

    def set_element(self, row, col, value):
        """Sets or updates an element in the sparse matrix."""
        if value == 0:
            self.data.pop((row, col), None) 
        else:
            self.data[(row, col)] = value

    def display(self):
        """Prints the sparse matrix in dictionary format."""
        print(f"Rows: {self.num_rows}, Cols: {self.num_cols}")
        print("Stored Data:", self.data)

    def display_full_matrix(self):
        """Prints the full matrix in grid format."""
        for i in range(self.num_rows):
            row_values = []
            for j in range(self.num_cols):
                row_values.append(str(self.get_element(i, j)))
            print(" ".join(row_values))


matrix = SparseMatrix("matrix1.txt")
matrix.display()
matrix.display_full_matrix()
