def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    a = input()
    a1 = convert(a)
    print(a1)

if __name__ == "__main__":
    main()
