def accounting(orders):
    """Creates a list of customers who underpaid for their melons.
    
    Function only prints out list of customers from text file who underpaid."""

    melon_cost = 1.00 # Original cost of melons

    # The purpose of the 'with' statement is to ensure that the file is 
    # properly closed after the block of code is executed. It takes care of opening and 
    # closing the file, even if an error occurs within the block. 'as accounting_log' assigns 
    # the file object returned by open(orders) to a variable named accounting_log. 
    # This variable is used to interact with the file.
    with open(orders) as accounting_log: 
        for line in accounting_log: # This for loop iterates over each line in the file object
            line = line.strip() # This remove trailing whitespaces (spaces, tabs, or newline 
                                # characters) in each line and creates one string
            words = line.split('|') # This is splitting a string (line) into a list of 
                                    # substrings based on a specified delimiter, 
                                    # which is the pipe character (|) in this case. 
                                    # This then turns "2|Andrea Cruz|12|12.00" into a words list like this: 
                                    # ['2', 'Andrea Cruz', '12', '12.00']

    # After turning the line into a list of strings, I can then access the different strings through indexing
            customer_number = int(words[0]) 
            customer = words[1]  # The customer is in index 1
            melons = int(words[2]) # Melon amount is in index two. Since this index will be used in an equation
                                    # below, it needs to be turned into an integer from a string.
            customer_paid = float(words[3]) # This is a dollar amount, meaning the variable type is a floating 
                                            # number and not an integer. The difference between the two
                                            # are the existence of decimals 

    # This is a variable that multiplies melons by melon_cost (1.00)
            customer_expected = melons * melon_cost 

    # This if statement states that if what the customer paid does not equal melons * melon_cost,
    # the function will print out a list of customers who underpaid. Notice that this statement is
    # still within the for loop because it is a part of looping through the list. 
            if customer_expected != customer_paid:
                print(f"{customer} paid ${customer_paid:.2f}, expected ${customer_expected:.2f}")


accounting("customer-orders.txt")
