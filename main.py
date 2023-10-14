def main():
    with open('data.txt') as file:
        file_lines = file.read().split('\n')
    cells_count, pass_count = int(file_lines[0]), int(file_lines[1])    # Считаем K и N
    passengers = [[int(i) for i in j.split()] for j in file_lines[2:]]  # и время [[<сдачи>, <освобождения>], ...]
    print(cells_count, pass_count, passengers)


if __name__ == '__main__':
    main()
