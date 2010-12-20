import sys
import shutil
import os


def p(o, b):
    if 'win' in sys.platform:
        #import pdb;pdb.set_trace()
        dest = o['location']
        lib = os.path.join(dest, 'lib')
        bin = os.path.join(dest, 'bin')
        if not os.path.exists(bin): os.makedirs(bin)
        for dll in [libdll 
                    for libdll in os.listdir(lib) 
                    if libdll.endswith('dll')]:
            orig, ldest = os.path.join(lib, dll), os.path.join(bin, dll)
            if os.path.exists(ldest):
                os.remove(ldest)

            shutil.copy2(orig, ldest)

    
# vim:set ts=4 sts=4 et  :
