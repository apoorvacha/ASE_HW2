from Examples import *

def main(funs):
    fails = 0
    for what, _ in funs.items():
            if funs[what]() == False:
                fails += 1
                print("❌ fail:",what)
            else: print("✅ pass:",what)
    if (fails == 0): return 0
    else: return 1

egs = {}
def eg(key, string, fun):
     egs[key] = fun

eg("ok", "seed generation", test_ok)
eg("sample", " testing of samples", test_sample)
eg("nums","testing nums", test_num)
eg("gauss", "testing gaussian", test_gaussian)
eg("boot", "testing bootstrap", test_bootstrap)

if __name__ == "__main__":
    main(egs)