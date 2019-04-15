
def get_input_from_user(message, user_list):
    while True:
        user_input_data = input(message).lower()
        if user_input_data in user_list:
            break
        if user_input_data == 'all':
            break

    return user_input_data