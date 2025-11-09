
#Task 7 :
 # ?? # #??????? ???? ??? 15 ???? ???? ?? ???? ????? ??? ??? ???? ?? ?? : - _ - _ - _ -??
new_private_school = {"Students_Names" : ["Alaa","Noor","Mariam","Youssra","Sama","Bibo","Mohamed","Saeed","Ali","Ahmed","Abdo","Lione","Amal","Toka","Rania"] ,
                      "City" : ["Alex","Alex","Beheira","Fayoum","Cairo","Qena","Alex","Qena","Cairo","Alex","Alex","Alex","Alex","Alex","Alex"] ,
                      "Seating_numbers" : ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15" ] ,
                      "Secret_number" : ["033312890","033398765","023354693","055584530","024386734","078734096","025394385","077743064","029611296","039401994","039227592","033615724","036627566","034599094","033398116" ],
                      "Degrees" : ["98.9" , "95" , "96", "98" , "94" , "90" , "99" , "98" , "70" ,"50" ,"99.9" , "99.", "95.0" , "88" , "80"] }
 # Use DataFrame
import pandas as pd
df = pd.DataFrame(new_private_school)
print(df)
# Print CIties & transform it into a graph #Official website of school
objects1= df["City"].value_counts()
print(objects1)
objects2= df["Degrees"].value_counts()
print(objects2)
# While true and try to Enter correct seating number : -
min_seating_number = 1
max_seating_number = 15
while True :
    try :
        seating_numbers = int(input("Enter your seating number : "))
        if seating_numbers == min_seating_number or seating_numbers == max_seating_number :
            print("Successful")
        elif seating_numbers > min_seating_number and seating_numbers < max_seating_number :
            print("Successful")
    except ValueError:
        print("Invalid input.This isn't a number. Please enter a seating number start from 1 : 15 only .")
