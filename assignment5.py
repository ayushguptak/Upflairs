            #Question 1
class calculate_area:
    def __init__(self , r):
        self.area = 3.14 * r * r

    def display(self):
        print(self.area)

x = int(input("Enter Radius Of The Circle : "))
R1 = calculate_area( r = x ) 
R1.display()


            #Question 2
class calculate_discount :
    def __init__(self , original_price , discount_percent) :
        self.discount = original_price * (discount_percent / 100)
        self.final_price = original_price - self.discount
    
    def display( self ) :
        print(  f" final price of item : {self.final_price}" )

x = int(input( "Enter price of item : " ))       
y = int(input( "Enter discount percentage on item : " ))         
item = calculate_discount(original_price = x , discount_percent = y )
item.display()


            #Question 3
class count_vowels :
    def __init__(self , s ) :
        self.string = s
        count = 0
        for i in self.string :
            if i in ( 'a', 'e', 'i', 'o', 'u' , 'A' , 'E' , 'I' ,'O', 'U' ):
                count = count + 1
        self.total_count = count

    def display( self ) :
        print(f" Total number of vowels in {self.string} : {self.total_count} ")  

x = input('Enter your string')
obj = count_vowels(s = x)
obj.display()