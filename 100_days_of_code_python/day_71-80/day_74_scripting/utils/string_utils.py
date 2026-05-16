def is_balanced(s: str) ->  bool:
    """Check if the brackets in the string are balanced.
    Args:
        s (str): The string containing brackets to check.
    Returns:
        bool: True if the brackets are balanced, False otherwise.
        """

    open_bracket = ['(','[','{']
    close_bracket = [')',']','}']
    bracket_map = {
                        '(':')',
                        '[':']',
                        '{':'}'
                   }
    bracket_list = []
    for bracket in s:
        if bracket in open_bracket:
            bracket_list.append(bracket)
        elif bracket in close_bracket:
            if bracket == bracket_map[bracket_list[-1]]:
                bracket_list.pop()

    if not bracket_list:
        return True
    else:
        return False
