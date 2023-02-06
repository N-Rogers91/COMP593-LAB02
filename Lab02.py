def main ():
   
    student_dict = {
        'full_name' : 'Noah Rogers',
        'student_id' : '10282524',
        'pizza_toppings' : [
            'BACON',
            'MUSHROOM',
            'PEPPERONI'
        ],
        'movies' : [
           
            {
                'title' : 'happy gilmore',
                'genre' : 'comedy'

            },
             {
                'title' : 'step brothers',
                'genre' : 'comedy'

            }      
       
        ]
    }
    new_movie = {
        'title' : 'get hard',
        'genre' : 'comedy'
    }
    student_dict ['movies'].append(new_movie)
    print_name_info(student_dict)
    #print(student_dict)

   
    return


def print_name_info(my_info : dict):
    full_name = my_info.get('full_name')
    first_name =  my_info.get('full_name').split()
    student_id = my_info.get('student_id')
    print(f'My name is {full_name}, but you can call Sir {first_name[0]}.')
    print(f'My student ID is {student_id}.')
   

    return
def add_toppings(my_toppings : dict):
     extra_toppings = add_toppings.add(extra_toppings) (['onion, olives, cheese']).append('pizza_toppings')
     
     #student_dict ['pizza_toppings'].append(student_dict)




if __name__ == '__main__' :
    main()
       