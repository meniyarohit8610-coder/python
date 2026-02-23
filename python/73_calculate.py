# write a program to generate and display sum of all the float values in tuple and also calculate average of all the float values in tuple.
#using for loop
tup = (1.5, 2.5, 3.0, 4.5, 5.0)
total_sum = 0
count = 0
for item in tup:
    if isinstance(item, float):
        total_sum += item
        count += 1
average = total_sum / count if count > 0 else 0
print("Sum of float values:", total_sum)
print("Average of float values:", average)
