while True:

        number = input('Please enter a positive number: ')
        digits = len(number)
        summ = 0
       
        if number.isalpha():
            print("Please enter a numeric character")
        
        elif "." in number or "," in number:

            print("Please enter an integer number")
        
        elif int(number) < 0 :
        
            print("Please enter a positive number")

        else:

            for i in range(digits):
                summ += int(number[i])**digits

            if summ == int(number):

                print(number, "is an Armstrong number")
                break
            else:
                print(number, "is not an Armstrong number")
                break