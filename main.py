def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))


def concat_strings(s1, s2):
    return s1 + s2
