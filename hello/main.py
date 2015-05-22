"""
This is the main file for hello package.
"""

def main(lang="en"):
    """This is the main function."""
    if lang == "en":
       english()
    elif lang == "it":
       italian()

    return 0

def spanish():
    """This is the english version."""
    print("Buenos dias")

def italian():
    """This is the italian version."""
    print("Buona sera!")

def english():
    """This is the english version."""
    print("Hello!")
