import sys, getopt
from Examples import *

argumentList = sys.argv[1:]
the = {"seed": 937162211, "dump": False, "go": "data", "help": False}
b4={}
ENV = {}
for k,v in ENV:
    b4[k]=v #cache old names (so later, we can find rogues)
# Options
options = "hg"
 
# Long options
long_options = []
def help():
    a= """
        script.lua : an example script with help text and a test suite
        (c)2022, Tim Menzies <timm@ieee.org>, BSD-2
        USAGE:   script.lua  [OPTIONS] [-g ACTION]
        OPTIONS:
        -d  --dump  on crash, dump stack = false
        -g  --go    start-up action      = data
        -h  --help  show help            = false
        -s  --seed  random number seed   = 937162211
        ACTIONS:
        -g  the	show settings
        -g  rand	generate, reset, regenerate same
        -g  sym	check syms
        -g  num	check nums
        """
    print(a)


def run_tests():
    func_pass= 0
    test_suite = [test_sym, test_nums, test_the, test_rand]
    #  , ,  test_clone, test_around, test_half, test_cluster, test_optimize] 

    for i,test in enumerate(test_suite):
        if(test()):
            func_pass += 1
            #print(i)
    print("\Total Test Cases Passing: " + str(func_pass) + "\nTotal Test Cases Failing: " + str(len(test_suite)-func_pass))
    



def main():

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        #, 
        # checking each argument
        # print(arguments,values)
        for currentArgument, currentValue in arguments:
            #  print(currentArgument)
             if currentArgument in ('-h', ''):
                help()
             if currentArgument in ("-g", ''):
               run_tests() 
                
    except getopt.error as err:
        # output error, and return with an error code
        print (str(err))

if __name__ == "__main__":
  main()