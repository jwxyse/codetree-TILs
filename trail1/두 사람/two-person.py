arr_1=input().split()
arr_2=input().split()

age_1=int(arr_1[0])
sex_1=arr_1[1]

age_2=int(arr_2[0])
sex_2=arr_2[1]

if (age_1>=19 and sex_1=='M')or(age_2>=19 and sex_2=='M'):
    print(1)
else:
    print(0)
