# bsdcat-kata
FreeBSD `cat` utility adapted to be a code kata on legacy code.

The file `cat.c` is taken from the FreeBSD project's implementation of Unix `cat` [1].
It is then adapted to be buildable as a Linux program.

How much of the original code can you safely delete without breaking the functionality?
How many tests do you need to have to ensure that your refactoring does not break anything?

## Get started

Make targets to be used during the kata:
- `make` - build the main program `cat`
- `make test` - run characterization test
- `make clean` - remove build artifacts
- `make coverage` - run the test and generate coveage report using `gcov`

1. https://github.com/freebsd/freebsd-src/blob/3a46fe226193dde1270ebb08d2066a77ae12d7e9/bin/cat/cat.c
