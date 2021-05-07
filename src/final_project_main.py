#Aileen Morales, Maura Blazek, Matt Uriegas
#Group 3, Final Project, main
import budget_breakdown_calc as c

def main(): # Function to run final project program
    c.display_menu()
    choice = input('Please select an option:  ')

    while choice != '5':
        if choice == '1':
            c.create_user()
        elif choice == '2':
            c.addUserExpenses()
        elif choice == '3':
            c.generate_report()
        elif choice == '4':
            c.terms()
        else:
            print('That is an invalid choice')

        c.display_menu()
        choice = input('Please select an option:  ')

if __name__ == '__main__':
    main()