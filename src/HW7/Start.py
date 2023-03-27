import Misc

def main(funs):
    fails = 0
    Misc.getCliArgs()
    for what, _ in funs.items():
            if funs[what]() == False:
                fails += 1
                print("❌ fail:",what)
            else: print("✅ pass:",what)
    if (fails == 0): return 0
    else: return 1

if __name__ == "__main__":
    main(Misc.egs)
