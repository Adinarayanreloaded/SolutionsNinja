inputs = input().strip().split()
results = []

for i in range(0, len(inputs), 2):
    basic_salary = int(inputs[i])
    grade = inputs[i + 1]

    HRA = 0.2 * basic_salary
    DA = 0.5 * basic_salary

    if grade == 'A':
        Allow = 1700
    elif grade == 'B':
        Allow = 1500
    else:
        Allow = 1300

    PF = 0.11 * basic_salary

    total_salary = basic_salary + HRA + DA + Allow - PF

    results.append(int(round(total_salary)))

for result in results:
    print(result)
