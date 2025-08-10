import programs

while True:
    print("1. Even or Odd")
    print("2. Factorial")
    print("3. Leap year")
    print("4. Diamond pattern")
    print("5. Positive or Negative")
    print("6. Check if number is zero")
    print("7. Eligible to vote")
    print("8. Check if temperature is hot > 30")
    print("9. Pass or fail")
    print("10. Greatest number")
    print("0. Exit")
    
    ch = input("Enter the Choice: ")

    if ch == '1':
        programs.EvenorOdd()
    elif ch == '2':
        programs.factorial()
    elif ch == '3':
        programs.leaf_year()
    elif ch == '4':programs.diamand_pattern()
    elif ch == '5':
        programs.PositiveorNegative()
    elif ch == '6':
        programs.Check_if_number_is_zero()
    elif ch == '7':
        programs.Eligible_to_vote()
    elif ch == '8':
        programs.Check_if_temperature_is_hot_30()
    elif ch == '9':
        programs.passorfail()
    elif ch == '10':
        programs.greatest_number()
    elif ch == '0':
        break
    else:
        print("Invalid choice")