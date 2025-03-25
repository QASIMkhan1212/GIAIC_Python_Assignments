
import random
random_numbers = [random.randint(1, 100) for _ in range(10)] # The underscore (_) is used as a variable here because we don’t actually need to use the loop variable; we just care about repeating the process 10 times.
print(random_numbers)