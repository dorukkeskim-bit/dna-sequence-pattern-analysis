def analyze_dna(sequence):
    """Calculate basic statistics and transformations for a DNA sequence."""
    sequence = sequence.upper()

    nucleotide_counts = {
        nucleotide: sequence.count(nucleotide)
        for nucleotide in "ATGC"
    }

    gc_count = nucleotide_counts["G"] + nucleotide_counts["C"]
    gc_content = (gc_count / len(sequence) * 100) if sequence else 0

    complement_map = str.maketrans("ATGC", "TACG")
    complement = sequence.translate(complement_map)
    reverse = sequence[::-1]
    reverse_complement = complement[::-1]

    return {
        "length": len(sequence),
        "nucleotide_counts": nucleotide_counts,
        "gc_content": round(gc_content, 2),
        "complement": complement,
        "reverse": reverse,
        "reverse_complement": reverse_complement,
    }


def pattern_positions(text, pattern):
    """Return starting positions of all pattern matches, including overlaps."""
    text = text.upper()
    pattern = pattern.upper()

    if not pattern:
        return []

    positions = []

    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            positions.append(i)

    return positions


def pattern_count(text, pattern):
    """Count occurrences of a pattern, including overlapping matches."""
    return len(pattern_positions(text, pattern))


def frequent_patterns(text, patterns):
    """Return all patterns with the highest occurrence count."""
    if not patterns:
        return [], 0

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
    sequence = "ATGATGATCCATG"
    patterns = ["ATG", "TGA", "GAT", "ATC"]

    analysis = analyze_dna(sequence)

    print("DNA Sequence:", sequence)
    print("Sequence Length:", analysis["length"])
    print("Nucleotide Counts:", analysis["nucleotide_counts"])
    print("GC Content (%):", analysis["gc_content"])
    print("Complement:", analysis["complement"])
    print("Reverse:", analysis["reverse"])
    print("Reverse Complement:", analysis["reverse_complement"])

    print("\nPattern Analysis:")

    for pattern in patterns:
        positions = pattern_positions(sequence, pattern)
        print(
            f"{pattern}: count={len(positions)}, "
            f"positions={positions}"
        )

    results, max_count = frequent_patterns(sequence, patterns)

    print("\nMost Frequent Patterns:", results)
    print("Maximum Occurrence Count:", max_count)
