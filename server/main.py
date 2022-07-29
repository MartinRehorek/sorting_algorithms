from algorithms.selection import selection_sort
from algorithms.insertion import insertion_sort
import sys
import time

def algorithms_available():
    algos = []
    for element in sys.modules.keys():
        if 'algorithms.' in str(element):
            algos.append(str(element).replace('algorithms.', ''))
    return algos

def main():
    # get all available algorithms by imported modules
    available_algorithms = algorithms_available()
    # intro
    input_array = []
    # user input
    while True:
        user_input = input('Enter a list of integers to sort separated by comma: ')
        if len(user_input) != 0:
            break
    # for number in user_input put them in input array
    for element in user_input.split(','):
        try:
            input_array.append(int(element))
        except:
            print(f'Could not add: ', element)
    #print(input_array)
    print('')
    # choose a sorting algo
    print(f"Choose out of these sorting algorithms: {', '.join(available_algorithms)}")
    while True:
        user_choice_algorithm = input('Enter a sorting algorithm of your choice: ')
        if user_choice_algorithm in available_algorithms:
            break
    print('')
    # execute the user choice algo
    start_time = time.time()
    sorted_array = globals()[user_choice_algorithm + "_sort"](input_array)
    print(sorted_array)
    print("--- It took %s seconds ---" % (time.time() - start_time))

    # each iteration printed
    # final time?
    # keeping the input arr, choose maybe another?
    # if "stop" => stop the script



if __name__ == "__main__":
    main()