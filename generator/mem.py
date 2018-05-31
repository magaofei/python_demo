from memory_profiler import profile

import cProfile
PATH = '/Users/mark/Desktop/hangdouts_add_10_60s.jtl'

@profile
def list_demo():
    f = [i*i for i in range(10000)]
    for i in f:
        pass

@profile
def generage_demo():
    f = (i*i for i in range(10000))
    for i in f:
        pass

# @profile
def read_file():
    a = []
    with open(PATH, 'r') as f:
        # a = [i for i in f]
        for i in f:
            a.append(i)

    with open(PATH + 'test_read.txt', 'a') as f:
        f.writelines(a)
    

# @profile
def open_lazy():
    def read_in_chunks(file_object, chunk_size=1024):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data


    f = open(PATH)
    a = read_in_chunks(f)

    with open(PATH + 'test_lazy.txt', 'a') as f:
        f.writelines(a)


if __name__ == '__main__':
    # list_demo()
    # generage_demo()
    cProfile.run('read_file()')
    cProfile.run('open_lazy()')
    # read_file()
    # open_lazy()

