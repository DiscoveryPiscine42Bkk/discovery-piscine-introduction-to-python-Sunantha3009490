def main():
    array = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = [x + 2 for X in array]
    result = set(new_array)
    print(result)
    if __name__ == "__main__":
        main()