def ft_count_harvest_recursive():
    count = int(input("Days until harvest: "))

    def counter(current):
        if current > count:
            return
        print(f"Day {current}")
        counter(current + 1)

    counter(1)
    print("Harvest time!")
