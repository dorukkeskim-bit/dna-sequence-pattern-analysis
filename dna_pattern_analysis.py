def pattern_count(text, pattern):
    """Count occurrences of a pattern, including overlapping matches."""
    count = 0

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1

    return count


def frequent_patterns(text, patterns):
    """Return all patterns with the highest occurrence count."""
    counts = []

    for pattern in patterns:
        counts.append(pattern_count(text, pattern))

    max_count = max(counts)

    most_frequent = []

    for i in range(len(counts)):
        if counts[i] == max_count:
            most_frequent.append(patterns[i])

    return most_frequent, max_count


if __name__ == "__main__":
    text = "ATGATGATCCATG"
    patterns = ["ATG", "TGA", "GAT", "ATC"]

    results, max_count = frequent_patterns(text, patterns)

    print("DNA sequence:", text)
    print("Most frequent patterns:", results)
    print("Maximum occurrence count:", max_count)
