import os

def make_files_read_write(folder_path):
    """
    Makes all files in the specified folder readable and writable.
    """
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Change permissions to readable and writable (octal 0o666)
                os.chmod(file_path, 0o666)
                print(f"Updated permissions: {file_path}")
        print("All files are now readable and writable.")
    except Exception as e:
        print(f"Error: {e}")

# Specify the folder path
folder_path = "/Users/ish/Documents/workspace/ai-ml/Machine Learning A-Z"

# Run the function
make_files_read_write(folder_path)