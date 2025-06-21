from functions.get_files_info import get_files_info, get_file_content


def main():
    result = get_file_content("calculator", "main.py")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print("")

if __name__ == "__main__":
    main()