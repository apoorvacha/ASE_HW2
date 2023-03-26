import default 
from Examples import *
import Misc

def main(options, help, funcs, saved = {}, fails = 0):
    for k, v in Misc.cli(Misc.settings(help)).items():
        options[k] = v
        saved[k] = v
    if options["help"]:
        print(help)
    else:
        for what in funcs:
            if options["go"] == "all" or what == options["go"]:
                for k,v in saved.items():
                    options[k] = v
                if funcs[what]() == False:
                    fails = fails + 1
                    print("❌ fail:", what)
                else:
                    print("✅ pass:", what)
    exit(fails)

egs = {}
def eg(key, str, func):
    egs[key] = func
    default.help = default.help + ("  -g  %s\t%s\n" % (key,str))

eg("sym","check syms",test_sym)
eg("num","check nums",test_nums)
eg("the","show settings", test_the)
eg("every","check every", test_every)


main(default.the, default.help, egs)