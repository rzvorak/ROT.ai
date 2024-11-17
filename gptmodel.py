import ast

def read_vectors_from_file(filename):
    vectors = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Parse the line as a literal list using ast.literal_eval
                vector = ast.literal_eval(line.strip())
                
                # Discard the first entry (the string) and keep the rest
                vectors.append(vector[1:])  # Slice to remove the first element
                
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return vectors