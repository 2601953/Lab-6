def sorted_string(s):
    # Join as a string
        # Sort the characters as a tuple of (char, is_lower)
            # Where the char is the same, it will istead compare the boolean
    return ''.join(sorted(s, key=lambda c: (c.lower(), c.islower())))
