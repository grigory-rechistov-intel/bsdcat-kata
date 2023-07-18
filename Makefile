
CFLAGS=-DNO_UDOM_SUPPORT -DBOOTSTRAP_CAT

cat: cat.c

clean:
	rm -rf cat *.gcno *.gcda

coverage: CFLAGS += --coverage
coverage: cat

cat.c: compat.h Makefile
	touch cat.c