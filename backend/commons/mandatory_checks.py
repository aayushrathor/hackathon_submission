# FUNCTION FUNCTIONALITIES :-
# - Will have null check for mandatory params
def mandatory_param_check(data_list):
    # if empty request param
    if not data_list:
        return True

    # all null check values
    null_check_values_list = [None, 'null', 'None', '', ['']]

    check = any(item in null_check_values_list for item in data_list)

    return check
