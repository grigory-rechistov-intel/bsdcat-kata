
CFLAGS=-DNO_UDOM_SUPPORT -DBOOTSTRAP_CAT

cat: cat.c

cat.c: cat.h compat.h

clean:
	rm -rf cat *.gcno *.gcda *.gcov

test: cat
	python3 ./characterization/test.py

coverage: CFLAGS += --coverage
coverage: clean cat test
	gcov cat
	
cat.c: compat.h Makefile
	touch cat.c