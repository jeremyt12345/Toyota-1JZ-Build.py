
    
# Jeremy Thomas

# 1JZ_Scion_FRS_Build

# This program is designed to tell the user not only what parts will be

# needed for a 1JZ engine build but the prices plus taxes, how long it

# it would take if you built it yourself or had a shop doing it

# this program was created to help me understand "while" loops

# and operations of math in Python.



# Define main function
def main():
    




    print()
    print()
    #Title
    print()
    print(" 1JZ Scion FRS Build...")
    print(" The 1JZ is an engine created by Toyota/n")
    print(" The 1JZ is an inline six cyclinder engine that was initially placed in many")
    print("Other Toyota cars but never in the Scion FRS")
    print(" This engine had a powerful 280hp and 270 lbs of torque")
    print(" The Scion FRS was created with a lackluster engine so")
    print(" many owners have sought to transform their car")
    print("First lets build the main components of your engine, if your car is too fast than needed our mechanics will make recommendations.")
    print()
    print()

option = 0
month = 0
horsepower = 0
time_attack_parts = 0

    

    
    

    
# My goal is to display 3 different options for the user
# Each Option is a loop, each loop will display three
# different menus
while option != 3:
        
# Above^ is stating that the prompt/loop will exit when/if the user enters 3.
    
        option = int(input('Choose one of the following options:\n'+
                   '    1. 1JZ Drift Build (Bought not built)\n'+
                   '    2. 1JZ Time-Attack Recommendations\n'+
                   '    3. 1JZ built by you or QUIT\n'+
                   'Option: '))
        print()
        

# Above^ is giving the user to input the option and display their choice.

        if option == 1:
            print('You choose the tire slayer. This build will include \n'+
                      '    * Tomei turbo kit.\n'+
                      '    * 2-Way LSD.\n'+
                      '    * Hydraulic Emergency Brake.\n'+
                      '    * Stronger Rods and Crankshaft.\n'+
                      '    * Stillen Body Kit.\n'+
                      '    * Polished Work Cr Kai\n'+
                      '    * Suspension Arms\n'+
                      '    * Angle Kit.\n'+
                      '    * Dry Sump Oiling System.\n')
                      
            print()

            
# ^These are the options user sees after selecting "1."
        elif option == 2:
                horsepower = int(input('Please enter 1JZ horsepower (>=280): '))

            
        
# If the user selects to "2" a weight over 100 pounds will be prompted to enter
                if horsepower >= 280:
                    print('We recomended modest engine modifactions and more of a focus on suspension/tires and weight reduction.\n')
                    
                elif horsepower < 100:
                     print('Error ... Invalid Horspower. Try Again')

                # ^Now the user will see their weight every month for six months subtracted by 4 pounds                   
                elif horsepower < 100:
                     print('Error ... Invalid Horspower. Try Again')
    

                   
                time_attack_parts = input('Would you like to buy our Time-Attack build parts? (Y/N): ')
                if  time_attack_parts.lower() == "y":
                                print('First we will reduce weight by 500lbs \n'+
                      '    * Install aerodynamic body.\n'+
                      '    * Improve Cooling system.\n'+
                      '    * Brembo Brakes.\n'+
                      '    * FALKEN tires.\n' +
                      '    * But, you are welcome to select your own parts\n')



parts = []

prices = []

total = 0

while True:
    part = input('Enter the parts you want to install (q to quit): ')

    if part.lower() == "q":
        
        break
    else:
            price = float(input(f"Enter the price of the {part}: $"))
            parts.append(part)
            prices.append(price)


print("----- YOUR CART -----")            

for part in parts:
    print(part, )


for price in prices:
    total += price
print()
print(f"Your total is: ${total}")
    
    
                          
                               
                          
if option == 3:
        

         print('Good Bye ...')
         

    

else:
        
    print('That option is not valid.')
                    
                   

                  
               

                    
# ^Here we have a possibility the user enter a weight less than 100
                   
# ^ A loop is created for this scenario.                        

                       
                      


                                

                         

       




             
main()             


            
