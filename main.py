from utils.math_tools import add, multiply, subtract
from utils.file_helpers import save_text

def main():
    print("Addition Result:", add(5, 3))
    print("Add:", add(10, 20))
    print("Multiply:", multiply(4, 6))
    print("Subtract:", subtract(10, 4))
    save_text("output.txt", "This is a test.")

if __name__ == "__main__":
    main()
