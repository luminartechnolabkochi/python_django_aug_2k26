### Variables
    -- container for storing values
    -- syntax
        
        variable_name = value

        --rules for variable name

            -- variable_name starts with an alphabet

            1age=32❌
            
            age =32 ✅

            age1=30 ✅

            age 1= 30❌ 

            age_1 = 32 ✅


### datatypes primitive

    - data type specifies the type of value that variable can hold
    
    - int,float,str,bool

    - company_name = "luminar technolab" ➡️ str

    - employee_count = 151 ➡️ int

    - rating = 5.0 ➡️ float

    - is_open = True ➡️ boolean



### Operators
    -- operators are symbols used for perform different operations 
        -Arithmetic Operators 
            - + addition
            - - subtraction
            - * multiplication
            - / division
            - % modulus
            - ** exponent
            -- // floor division

        -Relational operators
            - <  less than
            - >  gretater than
            - <= lessthan equalto
            - >= greater than equalto
            - == double equal
            - != not equal

        -Logical Operators
            - and logical and
            - or logical or
            - not logical not
        -Membership opertor 
            def: to chk value exist in a sequence 
                -sequence [string,list,set,tuple,dictionary] 
            - in

            eg:
                "a" in "apple" => True

                 12 in 123     => ❌ error 123 is not a sequnce
                 
                 "12" in "123" => True

                 3 in 12.3      => ❌ error 12.3 is not a sequnce

                 12 in [12,13,14] => True [] => list

                 12 in (10,11,12,13) => True ()=> tuple

                 12 in {10,11,12,13,15} =>True {} set

                 1 in {1:"i",2:"ii",3:"iii",4:"iv"}   =>True {k:v} dictionary

                

### Decisionmaking
    -- perform actions based on certain conditions
    --syntax

        if condition:
            stmt1
            stmt2
        default stmt

    --positive.py
        -read number
        -chk if number > 0 then 
            -display number is +ve
        
        number = int(input("enter number....))

        if number > 0 : 
            print("number is +ve")

    -- negative.py
        -read number
        -chk if number < 0  then
            -display number is -ve

        number = int(input("enter number"))

        if number < 0 :
            print("number is -ve")

    -- if...elif...else

        --syntax

            if condtion1:
                stmt1
            elif condition2:
                stmt2
            elif condition3:
                stmt3
            else:
                default stmt

        -eg
            -program to display number is +ve , -ve,or zero

            - read number
            -chk if number >0 then display +ve
            -chk elif number < 0 then display -ve
            -else display zero

            num_chk.py

            number = int(input("enter number)) #5

            if number > 0:

                print("+ve")
            elif number < 0:

                print("-ve")
            
            else:
                print("zero")

    -- match....case
### looping

    -- execute set of statements repeated number of times
    -- while loop (if range is unknown)
        
        syntax:
            initialization
            while(condition):
                statement1
                statement2
                incr|decr
        Eg:
            i = 1

            while(i<=10):

                print(i)

                i+=1
                
    --- for loop (if range is known)

        syntax:

            for i in range(start,stop,step):

                statements

        Eg:

            for i in range(1,11):

                print(i)


### programming techniques

    1)procedural programming | function

    2)object oriented programming


# Functions 

## there are two types of functions 
        
        - builtin functions 

            > print(message,end="\n")   # display message in console
            
            > range(start,stop,step=1) # return squence of numbers from start to stop
            
            > max(sequnce) # return maximum from sequence
            
            > min(sequence) # return minimum from sequence
            
            > len(obj)  # return length of object
            
            > input(message) => return value from user as string

        ## userdefined functions

           - we are defining our own functions

        ##syntax 

            def function_name(p1,p2,,,):

                function defnition


            function_name(p1,p2,,,)

        eg:

            def say_hello():

                print("HEllO")

            say_hello()


            def say_hi():

                print("HAI")

            say_hi()


        # function with parameter

            def function_name(p1,p2):

                function defnition

            function_name(p1_value,p2_value)

            Eg:

                def add_numbers(n1,n2):
                    result = n1+n2
                    print(result)

                add_numbers(100,200)

## function with return value

```
def function_name(p1,p2):

    function body

    return value

result = function_name(arg1,arg2)

EG:

def add_numbers(n1,n2):

    result = n1+n2

    return result

add_result=add_numbers(100,200)
print(add_result)
```
