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
eg("basic", "testing basic", test_basic)
eg("pre", "testing pre", test_pre)
eg("five", "testing five", test_five)
eg("six", "testing six", test_six)
eg("tiles", "testing tiles", test_tiles)
eg("sk", "testing sk", test_sk)

if __name__ == "__main__":
    main(egs)