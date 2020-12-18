"""
PSUEDOCODE

infile = final.txt
infile.open()

grades = [line.rstrip() for line in infile]

infile.close()

gradesLength = len(grades)

print(gradesLength)

for grade in grades:
    sum += grade

average = sum / gradesLength

print(average)

for grade in grades:
    if grade > average:
        counter += 1

percentAbove = counter / gradesLength

print(percentAbove)

END PSUEDOCODE
"""