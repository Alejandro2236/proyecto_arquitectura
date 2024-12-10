class Psw:

    def __init__(self):
        self.__zero_flag : str = ""
        self.__sign_flag : str = ""
        self.__overflow_flag : str = ""
        self.__carry_flag : str = ""

    def to_dict(self):
        return {
            "zero_flag": self.__zero_flag,
            "sign_flag": self.__sign_flag,
            "overflow_flag": self.__overflow_flag,
            "carry_flag": self.__carry_flag,
        }    
