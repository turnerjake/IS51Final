def main():
    #Open File
    inFile = {}
    try:
        inFile = open('Final.txt', 'r')
    except FileNotFoundError:
        print("ERROR! Couldn't find your grades file. Please check it exists in the current directory.")
        exit()
    
    tempGrades = [line.rstrip() for line in inFile]
    grades = [int(i) for i in tempGrades]

    #Get number of grades
    gradesLength = len(grades)

    if gradesLength > 0:
        print("Number of grades: ", gradesLength)
        #Calculate average
        averageScore = sum(grades) / gradesLength
        print(("Average score is: {0:.2f}").format(averageScore))

        calculate_percent_above_average(grades, gradesLength, averageScore)
    else:
        print("Grades list should not be empty!")
        exit()
    
def calculate_percent_above_average(grades, gradesLength, averageScore):
    counter = 0
    for i, val in enumerate(grades):
        if val > averageScore:
            counter += 1
    percent_above_average = counter / gradesLength
    print(("Percent of scores above average is: {0:.2%}").format(percent_above_average))

main()