import random

dataset_size = [100, 1000, 10000, 100000, 500000, 1000000]

# create 6 datasets
for i in range(1, 7):
    dataset_name = f"DataSet1-{i}.txt"
    with open(dataset_name, "w") as file:
        random.seed(1211103412)
        dataset = [random.randint(0, 999) for _ in range(dataset_size[i - 1])]
        for number in dataset:
            file.write(f"{number}\n")






