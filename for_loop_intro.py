heights = [180, 124, 165, 173, 189, 169, 146]

#print(round((height[0] + height[1] + height[2] + height[3] + height[4] + height[5] + height[6]) / 7))
#TOTAL LENGTH IN LIST
length = 0
for total_length in heights:
    length = length + 1
print(f"{length} is the total amount in list")

#TOTAL SUM IN LIST
sum = 0
for total_sum in heights:
    sum = sum + total_sum
print(sum)

average = sum / length
print(round(average))

