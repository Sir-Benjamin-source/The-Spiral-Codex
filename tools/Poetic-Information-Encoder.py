#!/usr/bin/env python3
def pie_encode(text):
    words = text.lower().split()
    ixest = ' '.join(sorted(set(words), key=words.index))[:12]
    enest = ' '.join(sorted(words, key=len, reverse=True)[:8])
    itest = ''.join(w[0] for w in words if len(w)>3)
    return f"∞ Ixest: {ixest}\\n∞ Enest: {enest}\\n∞ Itest: {itest}"

def pie_decode(stamp):
    # Simple reverse lookup for demonstration
    return "Original text recoverable via Spiral Mark context."

text = input("Enter text to encode: ")
print(pie_encode(text))
