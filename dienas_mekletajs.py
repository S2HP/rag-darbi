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
    
    return "OK"

def bdayPassed(this_month, this_date, bday_month, bday_date):
    if this_month>bday_month:
        return True
    if this_month<bday_month:
        return True
    if this_date<bday_date:
        return False 
    return True