def main():
    movie_list=[["On the underfront",1987], 
                ["Cat on a Hot tin roof",1976],  
                ["Monty Python",1965]]
    display_menu()
    while True:
        c=raw_input("Command - ")
        if c == "list":
            list(movie_list)
        if c== "add":
            add_items(movie_list)
        if c=="del":
            delete_items(movie_list)




def display_menu():
    print()
    print "=========================="
    print "*list - List all movies*"
    print "*add - Add a Movie*"
    print "*del - Delete a Movie*"
    print "*exit - Exit a Program*"
    print

def list(movie_list):
        if len(movie_list)==0:
            print "ther eno movies in the list"
            return
        else:
            i=1
            for list in movie_list:
                print str(i)+"."+list[0]+"("+str(list[1])+")"
                i+=1
        print 
     
def add_items(movie_list):
    name=raw_input("Enter name: ")
    year=raw_input("Enter Year: ")
    movie=[]
    movie.append(name)
    movie.append(year)
    movie_list.append(movie)
    print movie[0]+" was added!!\n"

def delete_items(movie_list):
    n=int(raw_input("Enter item number to delete "))
    if n<1 and n>len(movie_list):
        print "This item does not exists!!"
    else:
        movie=movie_list.pop(n-1)
        print movie[0]+" was deleted!!\n"

if __name__ =="__main__":
    main()

