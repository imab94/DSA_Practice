if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])

    second_lowest = float('inf')
    lowest = float('inf')


    for i in range(len(grades)):
        if grades[i][1] < lowest:
            lowest = second_lowest
            second_lowest = grades[i][1]

        elif grades[i][1] < second_lowest and grades[i][1]!= lowest:
            second_lowest = grades[i][1]
            name = grades[i][0]

    print(second_lowest, name)