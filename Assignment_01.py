salaries = ['20k', '40k', '50k', '60k', '35k', '89k','40k']

#  1. What is the length of the salaries list.
print(len(salaries))
    ## output   7

#  2. Retrieve the third salary in the list by using index.
print(salaries[2])
     ##   output  [50k]

#3. Extract the last salary from the list by using a negative index.
print(salaries[-1])
    ## output  [89k]

#  4. Slice the salaries list to get only the middle three salaries.
print(salaries[2:5])
    ## output  ['50k', '60k', '35k']

#  5. Add a new salary to the list, ‘100k’ by using append() method.
salaries.append('100k')
print(salaries)
     # output  ['20k', '40k', '50k', '60k', '35k', '89k', '40k', '100k']

#  5. Add a new salary to the list, ‘120k’ without method.
salaries[8] = '120k'
print(salaries)
     ## output   IndexError: list assignment index out of range


#  6. Replace the third salary in the list with '55k' and print the updated list.
salaries[2] = '55k'
print(salaries)
     ## output ['20k', '40k', '55k', '60k', '35k', '89k', '40k']

#  7. Count how many times '40k' appears in the list.
print(salaries.count('40k'))
     ##  output 2 

#  8. Insert a new salary at the second position.
salaries.insert(1, '45k')
print(salaries)
     ## Output   ['20k', '45k', '40k', '50k', '60k', '35k', '89k', '40k']

#  9. Reverse the order of the salaries list with method.
salaries.reverse()
print(salaries)
    ##  output ['40k', '89k', '35k', '60k', '50k', '40k', '20k']
    
    
#  10. Reverse the order of the salaries list without method.
salaries = salaries[::-1]
print(salaries)
     ##  output    ['40k', '89k', '35k', '60k', '50k', '40k', '20k']