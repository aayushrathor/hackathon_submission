# FUNCTION FUNCTIONALITIES :-
# - Basic response structure
def basic_response_dict(message, error, data, status):
    response = {
        "message": message,
        "error": error,
        "data": data,
        "status": status
    }

    return response
