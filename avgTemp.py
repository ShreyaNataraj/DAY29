numDays = int(input("How many Days  temperature you want :"))
total =0
temp =[]
for i in range(numDays):
  nextday = int(input("Day" + str(i+1) + 's temperature'))
  temp.append(nextday)
  total+=temp[i]
avg = round(total/numDays,2)
print("\n average = " +str(avg))  
above =0
for i in temp:
  if i>avg:
    above+=1
    print(str(above) + " Day's above average")
