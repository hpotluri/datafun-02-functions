import statistics

dataset1 = [10,11,14,20,20,20,22,24,28,31]
print(f"Mean of Dataset1 is {statistics.mean(dataset1)}")
print(f"Median of Dataset1 is {statistics.median(dataset1)}")
print(f"Mode of Dataset1 is {statistics.mode(dataset1)}")
print(f"Variance of Dataset1 is {statistics.variance(dataset1):.2f}")

dataset2 = [2,9,13,14,20,20,24,26,32,40]
print(f"Mean of Dataset2 is {statistics.mean(dataset2)}")
print(f"Median of Dataset2 is {statistics.median(dataset2)}")
print(f"Mode of Dataset2 is {statistics.mode(dataset2)}")
print(f"Variance of Dataset2 is {statistics.variance(dataset2):.2f}")