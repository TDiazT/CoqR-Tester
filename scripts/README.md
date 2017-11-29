# Scripts

## Runner
It runs every command in a file, line by line, with the given interpreter and outputs
a file with a JSON-style result.

Example: 
```bash
# Running R on a file
$ python runner.py R input.R output.json

# Running proveR 
$ COQ_INTERP=/path/to/proveR/ python runner.py asdf input.R output.json
```

Arguments:
1. Interpreter: Either "R" or anything
1. R file: File with R expressions to be run
1. Output: name of the output file (Ideally .json)

Output:
A file with the results in the following format:
```javascript
[
    {
       "interpreter": "",
        "execution_time": ,
        "expression": "",
        "output": "",
        "line":  
    },
    ...
]
```

## Cleaner
Reads a file (in JSON format), "cleans" the output and returns a file with a new
"cleaned_output" field.

```bash
$ python cleaner.py R input.json output.json

```

Arguments:
1. Input file: Ideally the one from the runner phase or with the same format.
1. Output file: Where to write the resulting "cleaned" version.

Output:
A file with the same results as in the input file but with a new field:
```javascript
[
    {
       ...,
       "clean_output": ""
    },
    ...
]
```

## Comparator
Reads two files, Coq's output first and then R's output, compares the values and 
outputs a file with the resulting comparison.
```bash
$ python comparator.py coq.json r.json output.json
```

Arguments:
1. First input: Ideally Coq's cleaned output
1. Second input: Ideally R's cleaned output
1. Output file: Where to print resulting comparison

Output:
A file with the results in the following format:

```javascript
[
  {
    "clean_coq_output": ""
    "status_code": "",
    "expression": "",
    "clean_r_output": "",
    "coq_output": "",
    "r_output": ""
  },
  ...
 ]
```
