def main():
    with open('data.txt') as file:
        file_lines = file.read().split('\n')
    cells_count, pass_count = int(file_lines[0]), int(file_lines[1])      # Считаем K и N
    passengers = [[int(i) for i in j.split()] for j in file_lines[2:-1]]  # и время [[<сдачи>, <освобождения>], ...]
    # print(cells_count, pass_count, passengers)
    passengers.sort()
    cells = []
    occupied_count = last_number = 0
    for j in range(len(passengers)):
        for i in range(len(cells)):
            if passengers[j][0] > cells[i][1]:
                cells[i] = passengers[j]
                print('З', passengers[j], cells)    # Один пассажир освободил место и его Заменил другой
                occupied_count += 1
                last_number = i+1
                break
        else:
            if len(cells) < cells_count:
                cells.append(passengers[j])
                print('Н', passengers[j], cells)    # Пассажир занял Новое место
                occupied_count += 1
                last_number = len(cells)+1
            else:
                print('У', passengers[j], cells)    # Пассажир ушёл
    print(occupied_count, last_number)


if __name__ == '__main__':
    main()
