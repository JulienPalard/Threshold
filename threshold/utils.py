import constants


class Check():
    @staticmethod
    def is_email(email):
        return constants.VerifiedExpression.EMAIL_ADDRESS_REG.search(email) is not None

    @staticmethod
    def is_url(url):
        return constants.VerifiedExpression.URL_ADDRESS_REG.search(url) is not None

    @staticmethod
    def is_include(param, vals):
        return param in vals

    @staticmethod
    def is_exclude(param, vals):
        return not param in vals

    @staticmethod
    def is_phone(phone):
        return constants.VerifiedExpression.PHONE_REG.search(phone) is not None

    @staticmethod
    def is_valid_datetime(datetime):
        import datetime
        try:
            datetime.datetime.strptime(val, formats)
            return True
        except ValueError:
            return False
