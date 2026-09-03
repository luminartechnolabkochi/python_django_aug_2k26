
# q1 display all even numbers from 10  to 50
# q2 display all odd numbers from 10 to 50
# q3 display all years from 1800 to 2026
# q4 display all century years (ending with two 0's) from 1800 t0 2026
# q5 display all non century year's from 1800 t0 2026

#display all leap years from 1800 to 2026



for year in range(1800,2027):

    if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):

        print(year)

