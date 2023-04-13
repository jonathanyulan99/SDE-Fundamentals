def fullJustify(words, maxWidth):
    result = []
    row = []
    rowChars = 0

    for word in words:
        lineLength = rowChars + len(word) + len(row)
        if lineLength > maxWidth:
        # Traverse length of difference and add spacing
            for i in range(maxWidth - rowChars):
                row[i % (len(row) - 1 or 1)] += " "
      
            # Join row content and push to result
            result.append("".join(row))

            # Reset row and character count
            row = []
            rowChars = 0

        # Push word to result and add word length to row count
        row.append(word)
        rowChars += len(word)

     # Join row words and pad
    paddedRow = " ".join(row).ljust(maxWidth)

    # Add final row and return justified result
    return result + [paddedRow]

words =["This", "is", "an", "example", "of", "text", "justification."]
maxlength = 16
print(fullJustify(words,maxlength)==["This    is    an","example  of text","justification.  "])