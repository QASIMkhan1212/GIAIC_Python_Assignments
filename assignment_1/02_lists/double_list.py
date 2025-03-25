def main():
    numbers: list[int] = [1, 2, 3, 4]  

    for i in range(len(numbers)): 
        element_at_index = numbers[i] 
        numbers[i] = element_at_index * 2  

    print(numbers) 

main()