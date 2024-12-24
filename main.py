# main file of the project
# all rights are reserved
# ================================================================

# import all nessesary libs and modules
import is_even as m1 # import my own module
import sum_digits as m2 # import my own module
import sum as m3 # import my own module
import temperature as m4 # import my own module


# the main fuctions of the proj
def main():
    user_choise = input(" Choose your function"
            "\nif you want to convert temperature choose 1: "
            "\nif you want to convert temperature choose 2: "
            "\nif you want to convert temperature choose 3: "
            "\nif you want to convert temperature choose 4: ")
    if user_choise() == '1':
        m1.main()
    elif user_choise() == "2":
        m2.main()
    elif user_choise() == '3':
        m3.main()
    elif user_choise() == "4":
        m4.main()
    else:
        main()


        if __name__ == '__main__':
            main()