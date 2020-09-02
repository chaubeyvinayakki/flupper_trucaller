from rest_framework.views import exception_handler


def get_error_message(message):
    location = None
    while message.__class__ != list:
        location = list(message)[0]
        message = message[list(message)[0]]
    return location, message[0]


def custom_exception_handler(exc, context):
    """
        method to override the default exception class
    :param exc:
    :param context:
    :return:
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    if response is not None and 'detail' in response.data:
        message = response.data['detail']
        error = {
                    'location': 'server',
                    'message': message
                }
        response.data = {}
        response.data['status'] = response.status_code
        response.data['error'] = error
    else:
        try:
            errors = response.data
            error_location = list(errors.keys())[0]
            message = errors[error_location]

            # get location and message of error
            location, message = get_error_message(message)
            if location is not None:
                error_location = location

            if error_location == 'non_field_errors' or error_location == '':
                error_location = 'server'
            error = {
                        'location': error_location,
                        'message': message
                    }
            response.data = {}
            response.data['status'] = response.status_code
            response.data['error'] = error
        except Exception as e:
            pass
    return response
