
def get_input_from_user(message, user_list):
    """
    An utility func to obtain user specific input value

    Args:
        (str) message - an information message for a particular request
    Returns:
        (str) user_data - requested data from user
    """
    while True:
        user_input_data = input(message).lower()
        if user_input_data in user_list:
            break
        if user_input_data == 'all':
            break

    return user_input_data