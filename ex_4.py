# Print five lines of zeros in a loop, each line must be numbered

zero = "00000"
line_number = 0
for x in range(1, 6):
    line_number += 1
    print(str(line_number) + "." + str(zero))
