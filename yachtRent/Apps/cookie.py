from Apps import MysqlConnecter
import random
import string


def generateCookie():
    """
    generate random 20 bytes cookie
    :return: a string of length 20
    """
    token = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    while MysqlConnecter.get_one('YachtClub', 'select * from cookies where token = %s', token) is not None:
        token = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    return token


def storageCookieInfo(username, token):
    """
    storage cookie info into database for further use
    :param token:
    :param username:
    :return: None
    """
    print([username, token])
    MysqlConnecter.modify('YachtClub', 'DELETE FROM cookies WHERE username = %s', [username])
    MysqlConnecter.modify('YachtClub', 'INSERT INTO cookies (token, username) VALUES(%s, %s)',
                          [token, username])
