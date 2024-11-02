#Tanke input
medical_cause=input("Did you have a medical cause Y and N :")
#input
atten = (int(input("Enter attendence of the student :")))

#checking

if medical_cause=='Y': #cheacking the condition 1
    print("Your allowed")
else:
    if atten>=75: #cheacking the condition 2
        print("Allowed")
    else:
      print("Not allowed")
