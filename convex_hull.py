import incr_algo
import utils
import gift_wrapping_algo
import quickHull_algo

def main():
    #paths = ["../data/examples/"]
    paths = ["../data/images/", "../data/uniform/"]
    ch_algo = quickHull_algo.quickHull_algo
    for path in paths:
        utils.test2(path)

if __name__ == "__main__":
    main()

