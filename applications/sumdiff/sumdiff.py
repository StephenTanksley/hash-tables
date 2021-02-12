"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

"""
    Problem: We want to find all of the 

"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


table = {}


def build_table(tup):

    for i in range(0, max(tup)):
        table[i] = f(i)
    return table


build_lookup = build_table(q)


def master_function(tup):
    results = []
    # This is where I've made a mistake. I'm pulling out all of the items in the tuple in order, but they won't always be in order. Sometimes
    for i in tup:
        a = i
        b = i + 1
        c = i + 2
        d = i + 3

        while (d <= len(tup)):

            l1 = table[a]
            l2 = table[b]
            r1 = table[c]
            r2 = table[d]

            left = l1 + l2
            right = r1 - r2

            if (left == right):
                results.append([l1, l2, " - ", r1, r2])
            else:
                return
    print("here are your results: ", results)
    return results


master_function(q)
