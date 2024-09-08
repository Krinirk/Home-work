def all_variants(text):
    i = len(text)
    for first in range(1, i + 1):
        for last in range(i - first + 1):
            yield text[last:last + first]


a = all_variants("abc")
for i in a:
    print(i)
