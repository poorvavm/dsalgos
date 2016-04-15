# You are given a two-dimensional array of sales data where the first column 
# is a product ID and the second column is the quantity. Write a function to take 
# this list of data and return a new two-dimensional array with the total sales for each product ID. 
# Example:
# Input:
# 211,4
# 262,3
# 211,5
# 216,6
# Output:
# 211,9
# 262,3
# 216,6

def dictionary_to_mdarray(prod_d):
    data = []
    for key in prod_d:
        temp_list = []
        temp_list.append(key)
        temp_list.append(prod_d[key])
        
        data.append(temp_list)

    return data

def product_data(data):
    prod_d ={}
    for i in range(0,len(data)):
        product_id = data[i][0]
        product_qty = data[i][1]
        if product_id in prod_d:
            prod_d[product_id] += product_qty
        else:
            prod_d[product_id] = product_qty
    return dictionary_to_mdarray(prod_d)

test_data = [[211,4], [262,3], [211,5], [216,6], [262,5]]
print product_data(test_data)



