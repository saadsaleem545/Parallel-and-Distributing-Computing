import multiprocessing

def myFunc(i, shared_list):
    print(f'Calling myFunc from process n°: {i}')
    for j in range(0, i):
        print(f'Output from myFunc is: {j}')
        shared_list.append(f'Process {i} output: {j}')
    print(f'Process n°{i} finished.\n')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    shared_list = manager.list()  #  Shared list for storing outputs

    processes = []

    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i, shared_list))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(" All processes have finished execution!\n")
    print(" Combined outputs from all processes:")
    for item in shared_list:
        print(item)
