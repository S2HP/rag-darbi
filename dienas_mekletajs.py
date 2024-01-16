def find_day(this_year, this_month, this_day, this_date, bday_day, bday_month, bday_year, bday_date):
    daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 30, 31]
    
    # Skaita cik dienas ir pagājušas.
    daysGoneBy = 0
    yearsGoneBy = this_year-bday_year

    if bdayPassed(this_month, this_date, bday_month, bday_date) == False:
        yearsGoneBy = yearsGoneBy-1
    daysGoneBy = daysGoneBy+leapYear

    leapYear = 0
    test_year_end = this_year
    if bdayPassed(bday_month, bday_date, 2, 29):
        test_year_start = test_year_start+1
    
    
    test_year_start = bday_year
    if bdayPassed(bday_month, bday_date, 2, 29) == False:
        test_year_end = this_year-1


    for year in range(bday_year, this_year+1, 1):
        if year % 4 == 0:
            leapYear = leapYear+1
        if year % 100 == 0 and year % 400 != 0:
            leapYear = leapYear-1
    
    daysGoneBy += leapYear

    if this_month>bday_month:
        full_months = this_month-bday_month
    else:
        full_months = this_month+12-bday_month

    if bdayPassed(1, this_date, 1, bday_date) == False:
        full_months -= 1

    daysinMonth = 0

    for i in range(bday_month, this_month):
        if i == 13:
            i=1
        
        daysinMonth += daysPerMonth[i]

    daysGoneBy += daysinMonth

    if this_date>=bday_date:
        daysGoneBy += this_date-bday_date[this_month-1]
    else:
        daysGoneBy = this_date + daysinMonth[this_month-1]+bday_month
    return "OK"

def bdayPassed(this_month, this_date, bday_month, bday_date):
    if this_month>bday_month:
        return True
    if this_month<bday_month:
        return True
    if this_date<bday_date:
        return False 
    return True