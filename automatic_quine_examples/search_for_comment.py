this_code = "placeholder"
# unfortunately, it isn't possible to have a comment before
# the first line so here goes the first line

import time
import re
print("searching this code for comments...")
# give the feeling of needing a long time
time.sleep(1)
#######################################

# now, check the number of comments, for that...

# ...define a regex...

# I know it's not the best regex, but it's just an example
regex = re.compile("^#.*$")

# ...print all comments...
lines = this_code.split("\n")
for line in lines:
    if regex.match(line):
        print(line)

# ...and count them
print(f"{sum([1 for line in lines if regex.match(line)])=}")