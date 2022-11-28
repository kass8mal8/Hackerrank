def solution(grades):
    L = []
    for grade in grades:
        if grade >= 38 and grade % 5 != 0:
            rem = grade % 5
            mult_five = grade + (5 - rem)
            if mult_five - grade < 3:
                grade = mult_five
                L.append(grade)
            else:
                L.append(grade)

        else:
            L.append(grade)

    return L


nums = [68, 72, 38, 65, 29, 71, 83, 94]
print(solution(nums))
