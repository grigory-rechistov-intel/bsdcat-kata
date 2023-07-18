
CFLAGS=-DNO_UDOM_SUPPORT -DBOOTSTRAP_CAT

cat: cat.c

cat.c: compat.h Makefile
	touch cat.c