#Cow Interpreter
A python based interpreter for the esoteric language Cow.
SOURCE: https://bigzaphod.github.io/COW/
SOURCE 2: https://frank-buss.de/cow.html

## Using the Interpreter
```
Cow Interpreter

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  .cow file to interpret (default: None)
  -s SEPERATOR, --seperator SEPERATOR
                        How the code is seperated. Options: None,
                        Space, NewLine (default: None)
  -d, --debug           Enable Debug Output; Adds command, and memory
                        output for every instruction. (default: False)
  -ds, --stepper        Enable stepping mode, requires user to press
                        enter between every instruction. (default:
                        False)
```
NOTE: File and Seperator are required options.

To use Cow Interpreter for test.cow
```
python3 cow-interpreter.py -f test.cow -s none
```

To use Cow Interpreter for test_nl.cow
```
python3 cow-interpreter.py -f test_nl.cow -s NewLine
```

## Files
* cow-interpreter.py - A Python based COW interpreter with debugging support. Might not be the most efficient code.
* fs.cow - The fibanacci sequence code from the SOURCE above
* hw.cow - Hello, World program from teh SOURCE above
* test*.cow - Three different forms showing the different seperator styles for the interpreter. Based on the Frank code from SOURCE 2.
