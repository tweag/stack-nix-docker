#!/usr/bin/env python

import os
import sys
from subprocess import call

args = []
for i in range(1, len(sys.argv)):
    # Quote all arguments, just in case they were so originally.
    args.append("\"%s\"" % sys.argv[i])
    # XXX hack: If calling Stack have to pass env var as arguments.
    if os.path.basename(sys.argv[i]) == 'stack':
        args.append('--no-nix')
        args.append('--system-ghc')
        args.append('$STACK_IN_NIX_EXTRA_ARGS')

drv_exist = os.access("/shell.drv", os.F_OK)
shell_file = "/shell.drv" if drv_exist else "/shell.nix"

command = ["nix-shell", shell_file, "--run"] + [' '.join(args)]

call(command)
