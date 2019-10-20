import re
import sys
from ufal.udpipe import Model, Pipeline, ProcessingError


# get sentences from input.txt, parse and write them in output.txt file
def get_text():
    with open('input.txt', 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    n = 0
    for sentence in sentences:
        n += 1
        parsed = parse(sentence)
        for line in parsed.split('\n'):
            if line.startswith('# sent_id '):
                line = '#sent_id = ' + str(n)
            # leave unnecessary lines out
            if line.startswith('# newdoc'):
                continue
            if line.startswith('# newpar'):
                continue
            # write output
            with open('output.txt', 'a+', encoding='utf-8') as file:
                file.write(line)
                file.write('\n')


# assemble parser and parse sentences
def parse(sentence):
    sys.argv.append('tokenize')
    sys.argv.append('conllu')
    sys.argv.append('russian-syntagrus-ud-2.4-190531.udpipe')
    model = Model.load(sys.argv[3])
    pipeline = Pipeline(model, sys.argv[1], Pipeline.DEFAULT, Pipeline.DEFAULT, sys.argv[2])
    error = ProcessingError()
    # small preproccessing step
    sentence = re.sub('«', '« ', sentence)
    sentence = re.sub('»', '» ', sentence)
    parsed = pipeline.process(sentence, error)
    print(parsed)
    return parsed


def main():
    get_text()


if __name__ == '__main__':
    main()

