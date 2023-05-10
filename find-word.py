import os
import re
import textract

def search_directory_for_word(directory, search_word):
    file_types = (".conf", ".txt", ".pdf", ".sh", ".docx", "", ".py")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(file_types):
                file_path = os.path.join(root, file)
                try:
                    if file.endswith(".pdf"):
                        text = textract.process(file_path).decode("utf-8")
                    elif file.endswith(".docx"):
                        text = textract.process(file_path).decode("utf-8")
                    else:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            text = f.read()
                    if re.search(search_word, text):
                        print(f"Word or phrase '{search_word}' found in file: {file_path}")
                except UnicodeDecodeError:
                    print(f"Error: Could not read file {file_path}")
                except:
                    pass

directory = input("Enter the directory: ")
search_word = input("Enter the word to search for: ")
search_directory_for_word(directory, search_word)
