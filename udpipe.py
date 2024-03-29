import sys

from ufal.udpipe import Model, Pipeline, ProcessingError # pylint: disable=no-name-in-module

# In Python2, wrap sys.stdin and sys.stdout to work with unicode.
if sys.version_info[0] < 3:
    import codecs
    import locale
    encoding = locale.getpreferredencoding()
    sys.stdin = codecs.getreader(encoding)(sys.stdin)
    sys.stdout = codecs.getwriter(encoding)(sys.stdout)

print(sys.argv)
sys.argv.append('tokenize')
print(sys.argv)
sys.argv.append('conllu')
sys.argv.append('russian-syntagrus-ud-2.4-190531.udpipe')
print(sys.argv)




sys.stderr.write('Loading model: ')
model = Model.load(sys.argv[3])
if not model:
    sys.stderr.write("Cannot load model from file '%s'\n" % sys.argv[3])
    sys.exit(1)
sys.stderr.write('done\n')

pipeline = Pipeline(model, sys.argv[1], Pipeline.DEFAULT, Pipeline.DEFAULT, sys.argv[2])
error = ProcessingError()

# Read whole input
text = 'Ходите во Вкусвилл, он офигенный, а Пятерочку обходите стороной, ведь она офигевшая.'

# Process data
processed = pipeline.process(text, error)
if error.occurred():
    sys.stderr.write("An error occurred when running run_udpipe: ")
    sys.stderr.write(error.message)
    sys.stderr.write("\n")
    sys.exit(1)
sys.stdout.write(processed)