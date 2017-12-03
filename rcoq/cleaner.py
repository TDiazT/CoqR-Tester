import json
import sys
import argparse

from ..Comparator.ROutputProcessor import ROutputProcessor

input_ = sys.argv[1]

parser = argparse.ArgumentParser(description="Processes output and returns a new standard one")

parser.add_argument("interp", )
# parser.add_argument('--Coq')
# parser.add_argument('--R')

processor = ROutputProcessor()

with open(input_) as file_:
    outputs = json.load(file_)

    for output in outputs:
        result = processor.process(output['output'])
        output['clean_output'] = result

with open(sys.argv[2], "w") as file_:
    json.dump(outputs, file_, indent=2)
