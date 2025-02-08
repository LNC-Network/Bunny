def OpenFile(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found."
    except UnicodeDecodeError:
        return f"Error: File '{file_path}' has an unsupported encoding."

def GetFilePath(path):
    return f"{path}"