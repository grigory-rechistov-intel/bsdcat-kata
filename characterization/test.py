#! /usr/bin/env python3
# Compare outputs of commands against references

import os, sys
import difflib
import subprocess


pathname = os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(pathname)

def print_diff(a, b):
    d = difflib.Differ()
    result = list(d.compare(a.splitlines(keepends = True),
                            b.splitlines(keepends = True)))
    for line in result:
        print(line, end = "")
    print()

def get_input(input_file):
    with open(input_file, "rb") as f:
        return f.read().decode()   

def main():
    show_diff = True
    passed = 0
    failed = 0
    skipped = 0

    input_cases = (
        ([], "output0.ref"),
        (["input1"], "input1.ref"),
        (["-h"], "dash-h.ref"),
        (["-"], "output0.ref"),
    )

    for cmdline, reference in input_cases:
        cmd = ["../cat"] + cmdline
        print(f"{' '.join(cmd)} <-> {reference}", end = "")
        try:
            output = subprocess.check_output(cmd,
                                             stdin=subprocess.DEVNULL,
                                             stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            output = e.output.decode()

        reference_text = get_input(reference)   
        
        if reference_text != output:
            print(" FAIL")
            failed += 1
            if show_diff:
                print_diff(reference_text, output)
        else:
            print(" PASS")
            passed += 1

    total = passed + failed + skipped
    print("-"* 80)
    print(f"Total {total}, passed {passed}, failed {failed}, skipped {skipped}")
    return failed

if __name__ == "__main__":
    failed = main()
    sys.exit(failed != 0)
