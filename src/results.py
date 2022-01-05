
from counters import Counter, CsurosCounter, FixedProbabilityCounter
from collections import defaultdict
from utils import accuracy, mre, mae, mad, max_deviation, num_bits
from visualizer import visualize
import string
from random import seed
import time


def compare_char_counts(file_name:str, n_trials:int = 10):

    accepted_chars = set(string.ascii_uppercase)

    t1 = time.perf_counter()

    # read book and save all the exact occurences
    chars_exact_count = defaultdict(Counter)
    with open(file_name, 'r', errors='ignore') as file:
        for line in file:
            for char in line.upper():
                if char not in accepted_chars: continue
                chars_exact_count[char].increment()

    # loop though all encountered chars
    sorted_chars = sorted(chars_exact_count.items(), key=lambda x: x[1].value, reverse=True)
    char_statistics = defaultdict(lambda: defaultdict(list))
    for char, counter in sorted_chars:
        fixed_probability_list = list()
        csuros_list = list()

        exact_count = counter.value

        # perform n experiments
        for _ in range(n_trials):
            fixed_probability_counter = FixedProbabilityCounter(1/32)
            csuros_counter = CsurosCounter(6)

            # for each counter perform the number of the exact counter increments
            for _ in range(exact_count):
                fixed_probability_counter.increment()
                csuros_counter.increment()
            fixed_probability_list.append(fixed_probability_counter)
            csuros_list.append(csuros_counter)
        
        # statistics
        for i, lst in enumerate([fixed_probability_list, csuros_list]):
            float_list = [counter.value for counter in lst]
            char_statistics['accuracy'][char].insert(i, accuracy(float_list, exact_count))
            char_statistics['max_deviation'][char].insert(i, max_deviation(float_list))
            char_statistics['mad'][char].insert(i, mad(float_list))
            char_statistics['mae'][char].insert(i, mae(float_list, exact_count))
            char_statistics['mre'][char].insert(i, mre(float_list, exact_count))
            char_statistics['max'][char].insert(i, max(float_list))
            char_statistics['min'][char].insert(i, min(float_list))
            char_statistics['num_bits'][char].insert(i, num_bits([counter.x for counter in lst]))
        char_statistics['exact_count'][char].insert(0, exact_count)
        char_statistics['num_bits'][char].insert(2, num_bits([exact_count]))

        print_stats = lambda i: print(f"accuracy: {char_statistics['accuracy'][char][i]},\
            max dev: {char_statistics['max_deviation'][char][i]},\
            mad: {char_statistics['mad'][char][i]},\
            mae: {char_statistics['mae'][char][i]},\
            mre: {char_statistics['mre'][char][i]},\
            max: {char_statistics['max'][char][i]},\
            min: {char_statistics['min'][char][i]},\
            bits: {char_statistics['num_bits'][char][i]}\
        ")

        print('-'*20)
        print(f'{char}: {str(counter)}')
        print(f'Fixed Probability Counter', )
        print_stats(0)
        print('-'*10)
        print(f'Csuros Counter')
        print_stats(1)


    t2 = time.perf_counter()
    visualize(char_statistics)
    print(f'took {round(t2-t1, 3)} seconds')
            

if __name__ == '__main__':
    seed(100)
    compare_char_counts("datasets/history_of_portugal.txt", 5000)