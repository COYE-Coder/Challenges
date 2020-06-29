# An institutional broker wants to review their book of customers to see which are most active. 
# Given a list of trades by customer name, determine which customers account for at least 5% of the total number of trades. 
# rder the list alphabetically ascending by name. 



# Example n = 23 
# customers = ["Bigcorp", "Bigcorp", "Acme", "Bigcorp", "Zork", "Zork", "Abc", 
# 			"Bigcorp", "Acme", "Bigcorp", "Bigcorp", "Zork", "Bigcorp", "Zork", "Zork", 
# 			"Bigcorp", "Acme", "Bigcorp", "Acme", "Bigcorp", "Acme", "Little Corp", "Nadicorp"]. 

# Bigcorp had 10 trades out of 23, which is 43.48% of the total trades. 
# Both Acme and Zork had 5 trades, which is 21.74% of the total trades. 
# The Littlecorp, Nadir, and Abc had 1 trade each, which is 4.35% of the total trades. 
# So the answer is ["Acme", "Bigcorp", "Zork"] (in alphabetical order).


# mostActive() has the following parameter: 
# string customers[n]: an array customer names 
# Returns string[]: an alphabetically ascending array of customer names


def mostActive(customers):
    uniques = dict(zip(list(customers),
                    [list(customers).count(i) for i in list(customers)]))
    
    most_active = [u for u,c in uniques.items() if (c/len(customers)) >=0.05]
   
    return sorted(most_active)