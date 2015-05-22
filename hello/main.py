"""
This is the main file for hello package.
"""

def main(lang="en"):
    """This is the main function."""
    if lang == "es":
       spanish()
    elif lang == "it":
       italian()
    elif lang == "pt":
       portuguese()

    return 0

def spanish():
    """This is the english version."""
    print("Buenos dias!")

def italian():
    """This is the italian version."""
    print("Buona sera!")

def portuguese():
    """This is the portuguese version."""
    print("Bom dia!")
