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



