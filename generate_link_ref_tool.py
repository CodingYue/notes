'''
    Generate github wiki markdown file's link references.
'''
import sys
import re
import gflags
from gflags import FLAGS

gflags.DEFINE_string("file_name", None, "file name help")
gflags.DEFINE_integer("lower_bound", 1, "lower bound help")
gflags.DEFINE_integer("upper_bound", 2, "upper bound help")

times = None
def generate_link(link):
    # print link
    original_link = link.replace('#','').strip()
    number_of_sharp = 0
    for x in link:
        if x != '#':
            break
        number_of_sharp += 1
    
    link = link.strip().replace('# ', '').replace(' ', '-')
   # print link
    result = ""
    for x in link:
        s = str(x)
        if s.isdigit() or s.isalpha() or s == '-':
            result += s
    result = result.lower()
    
    value = 0
    if result in times:
        value = times[result]
    else:
        value = 0
    times[result] = value + 1
    if value > 0:
        result = result + "-" + str(value)
    return "%s * [%s](#%s)" % ("\t" * (number_of_sharp - FLAGS.lower_bound), 
        original_link, result.lower())

if __name__ == "__main__":
    FLAGS(sys.argv)

    file_name = FLAGS.file_name
    assert file_name != None
    lower_bound = FLAGS.lower_bound
    upper_bound = FLAGS.upper_bound

    content = open(file_name, "r").read()
    # print content

    #print content
    # print "^#{%d,%d} .*" % (lower_bound, upper_bound)
    regex = re.compile(r"\n+#{%d,%d} .*" % (lower_bound, upper_bound))

    times = dict()
    links = regex.findall(content)
    for link in links:
        print generate_link(link)
        # generate_link(link)