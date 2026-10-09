class EmployeeFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(
            self.filename,
            self.mode,
            newline="",
            encoding="utf-8"
        )
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

        if exc_type is not None:
            print(f"File error: {exc_value}")

        return False