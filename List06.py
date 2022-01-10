def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    s=list1.replace(1,"True")
    return s
print(main("1,0,1,0,0,1"))