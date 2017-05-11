users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
def name2(users):
    for type in users:
        print type
        count=0
        for item in users[type]:
            count +=1 
            fn=item["first_name"]
            ln=item["last_name"]
            length=len(fn)+len(ln)
            print'{} {} {}'.format(count,fn,ln,length)
name2(users)