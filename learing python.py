
income = 50000
tax_payable = 0
#print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

#print("Total tax to pay is", tax_payable)

############# 00101010101

#print("Hello World!!")


######## Binary search problem ##### 

def binary_search(alist, key):
    if len(alist) > 0:
        mid = len(alist) // 2

        if alist[mid] == key:
            return True
        
        elif alist[mid] > key:
            return binary_search(alist[:mid], key)
        
        elif alist[mid] < key:
            return binary_search(alist[mid+1:], key)
        
    else:
        return False
    

#print(binary_search([10, 20, 30, 40], 20))
#print(binary_search([10, 20, 30, 40], 40))
#print(binary_search([1, 1, 3, 4, 11, 33, 44, 55], 10))

########## Greedy Algorithm in python #################

def activity_selection(activities):
    # Step 1: Sort activities by finish time
    activities.sort(key=lambda x: x[1])  # Sort by end time

    selected_activities = []  # Store selected activities
    last_end_time = 0  # Track last selected activity's end time

    # Step 2: Iterate over activities
    for start, end in activities:
        if start >= last_end_time:  # Step 3: Select if non-overlapping
            selected_activities.append((start, end))
            last_end_time = end  # Update last selected end time

    return selected_activities  # Return the list of selected activities

# Example usage
activities = [(1, 3), (2, 5), (3, 9), (6, 8), (5, 7), (8, 9)]
selected = activity_selection(activities)

print("Selected Activities:", selected)


########### Array

def find_subarray_with_target_sum(arr, target):
    # Iterate through the array to find the subarray that sums up to the target
    for start in range(len(arr)):
        current_sum = 0
       # print(start)
        for end in range(start, len(arr)):
            #print (len(arr))
            current_sum += arr[end]
            if current_sum == target:
                return [start, end]
    return None  # If no such subarray is found

# Example usage
arr = [1, 2, 3, 7, 5]
target = 12
result = find_subarray_with_target_sum(arr, target)

if result:
    print(f"Output: {result}")
else:
    print("No subarray with the given target sum found.")