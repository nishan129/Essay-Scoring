import sys

def error_message_detail(error,error_detail: sys):
    """Write a Code for Exception Handaling 

    Args:
        error (_type_): _description_
        error_detail (sys): _description_
    """
    _,_, exc_tb = error_detail.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = "Error occurred python script name [{0}] line number [{1}] error massage [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message


class ModelException(Exception):
    """
    Params error_message : error message in string format
    """
    def __init__(self, error_message, error_detail) -> None:
        
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    