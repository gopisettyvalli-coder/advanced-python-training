class EmployeeFileManager:

    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.file=None

    def __enter__(self):
        print("Opening File......")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print("Error occurred:", exc_value)
        else:
            print("Employee data processed successfully.")
            print("Saving changes...")
        self.file.close()
        print("File closed.")
        return False

with EmployeeFileManager("employees.txt", "w") as file:
    file.write("101, John, Python\n")
    file.write("102, Jane, Java\n")

print("Program completed.")




