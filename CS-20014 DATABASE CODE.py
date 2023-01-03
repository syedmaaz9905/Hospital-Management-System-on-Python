list=[]
def function(list):
      while True:
           x=input('Enter Name=')
           y=input('Enter Employee ID in ascending order=')
           z=input('Enter profession of Employee=')
           a=input('Enter Shift of Employee=')
           if z=='nurse':
                  if a=='morning'or a=='night' :
                         salary=300000
                         DA=(300000*20)/100
                         HRA=(300000*20)/100
                         gross_salary=300000+DA+HRA
                  elif a=='24hour':
                         salary:400000
                         DA=(400000*20)/100
                         HRA=(400000*20)/100
                         gross_salary=400000+DA+HRA
           elif z=='nurse' or 'Health care assisstant ':
                  if a=='morning' or a=='night' :
                         salary=150000
                         DA=(150000*20)/100
                         HRA=(150000*20)/100
                         gross_salary=150000+DA+HRA
                  elif a=='24hour':
                         salary:200000
                         DA=(200000*20)/100
                         HRA=(200000*20)/100
                         gross_salary=200000+DA+HRA
           elif z=='Ward House keeper':
                  if a=='morning'  or a=='night':
                         salary=100000
                         DA=(100000*20)/100
                         HRA=(100000*20)/100
                         gross_salary=100000+DA+HRA
                  elif a=='24hour':
                         salary:150000
                         DA=(150000*20)/100
                         HRA=(150000*20)/100
                         gross_salary=150000+DA+HRA

           list.append([x,y,z,a,[salary,DA,HRA,gross_salary]])
           c=input('Enter yes to continue=')
           if c!='yes' and c!='YES':
                 print(list)
                 break

def displaying_of_records(list) :
      for  data in list:
            print('Name:',data[0])
            print('Employee ID.:',data[1])
            print('rank:',data[2])
            print('shift:',data[3])
            print('Salary:',data[4][0])
            print('Dearness Allowance:',data[4][1])
            print('House Rent Allowance:',data[4][2])
            print('Gross Salary:',data[4][3])
            
def single_record(list):
      x=input('Enter Employee ID to search:')
      for data in list:
            if x==data[1]:
                  print('Name:',data[0])
                  print('Employee ID.:',data[1])
                  print('rank:',data[2])
                  print('shift:',data[3])
                  print('Salary:',data[4][0])
                  print('Dearness Allowance:',data[4][1])
                  print('House Rent Allowance:',data[4][2])
                  print('Gross Salary:',data[4][3])
            else:
                  print('no record found')
                  
def deleting_record(list):
      x=int(input('Enter Employee ID to delete:'))
      counter=0
      del list[x-1]
      
def save_record(list):
      c=input('enter name of file where data is to be saved:')
      f=open('G:/'+c+'.txt','w')
      for data in list:
            f.write(data[0]+'\n')
            f.write(data[1]+'\n')
            f.write(data[2]+'\n')
            f.write(data[3]+'\n')
            f.write(str(data[4][0])+'\n')
            f.write(str(data[4][1])+'\n')
            f.write(str(data[4][2])+'\n')
            f.write(str(data[4][3])+'\n\n')
      f.close()
      
def load_record():
       c=input('enter name of file where data is to be saved:')
       f=open('G:/'+c+'.txt','w')
       for line in list:
             print(line)
      
while True:
          print('''
      *************         WELOCOME!         *************

                       DATABASE OF HOSPITAL
-----------------------------------------------------------------------                      
      Select The Following
                       1.input of new records
                       2.displaying of record
                       3.Finding a single record
                       4.Deleting a record
                       5.Saving Record to a file
                       6.load a record
                       7.Exit

                       ''')
          y=int(input('enter your option here='))
          if y==1:
                function(list)
          elif y==2:
                displaying_of_records(list)
          elif y==3:
                single_record(list)
          elif y==4:
                deleting_record(list)
          elif y==5:
                save_record(list)
          elif y==6:
                load_record()
          else:
                print('program is now exiting')
                break    
      
          
      
            
                        
                  
                  
            
            
    

     
