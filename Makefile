
CC=clang
CFLAGS=-DNO_UDOM_SUPPORT -DBOOTSTRAP_CAT

cat: cat.c

clean:
	rm -rf cat *.gcno *.gcda *.gcov

test: cat
	python3 ./characterization/test.py

coverage: CFLAGS += --coverage
coverage: clean cat test
	llvm-cov gcov *.gcno
	
cat.c: compat.h Makefile
	touch cat.c