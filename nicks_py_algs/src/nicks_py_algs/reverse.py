"""Different algorithms to reverse a string."""

def reverse_0(s: str) -> str:
    """Reverse a string by traversing backwards and appending with each iteration."""
    reversed_output = ""
    s_length = len(s)
    for i in range(s_length-1, 0-1, -1):
        reversed_output = reversed_output + s[i]
    return reversed_output

def reverse_1(s: str) -> str:
    """Reverse a string by traversing forwards and appending to the front each iteration."""
    reversed_output = ""
    for c in s:
        reversed_output = c + reversed_output
    return reversed_output

def reverse_2(s: str) -> str:
    """Reverse a string by swapping elements around in a list and 'join'."""
    s_length = len(s)
    s_list = list(s)
    j = s_length-1
    for i in range(s_length-1):
        swap_var = s_list[j]
        s_list[j] = s_list[i] 
        s_list[i] = swap_var
        j=j-1
        if (j<i):
            break
    return ''.join(s_list)

def reverse_3(s: str) -> str:
    """Reverse a string with list 'reverse' and 'join'"""
    s_list = list(s)
    s_list.reverse()
    return ''.join(s_list)

def reverse_4(s: str) -> str:
    """Reverse a string with sequence 'reversed' and 'join'."""
    return ''.join(reversed(s))

def reverse_5(s: str) -> str:
    """Reverse a string by slicing."""
    return s[::-1]




