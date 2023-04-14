# Local files
import app
# time
from datetime import datetime


pattern_email: list[str] = [
    'gmail.com', 'mail.ru', 'yandex.ru',
    'kahoo.com', 'yahoo.com', 'od.ru',
    'github.com', 'hotmail.com', 'tempmail.ru'
]

class CheckEmail:
    """Check validation of email"""

    @staticmethod
    def check_email(em) -> bool:
        pattern_email: list[str] = [
            'gmail.com', 'mail.ru', 'yandex.ru',
            'kahoo.com', 'yahoo.com', 'od.ru',
            'github.com', 'hotmail.com', 'tempmail.ru'
        ]
        email_elements: list[str] = em.split("@")
        if "" in email_elements:
            return False
        if len(email_elements) != 2:
            return False
        if email_elements[0] != email_elements[0].lower():
            return False
        if not email_elements[1] in pattern_email:
            return False
        return True
    

class CheckPhone:
    """Check validation of phone number"""

    @staticmethod
    def check_phone_number(num) -> bool:
        if num[:2] != '87':
            return False
        if len(num) != 11:
            return False
        return True


class User:
    """this class for inputing user's
    info more comfortable"""

    def __init__(
        self,
        id: int,
        username: str,
        date_birth: datetime,
        email: str,
        phone: str
    ) -> None:
        self.id = id
        self.username = username
        try:
            self.date_birth = datetime.strptime(date_birth, '%d-%m-%Y')
        except:
            raise ValueError(
                "date is not correct, please input like that -> \n\nday-month-full year"
            )
        self.age = datetime.now().year - self.date_birth.date().year
        if CheckEmail.check_email(email):
            self.email = email
        else: 
            raise ValueError(
                'Email is not correct'
            )
        if CheckPhone.check_phone_number(phone):
            self.phone = phone
        else:
            raise ValueError(
                'Phone number is not correct'
            )
        
    @staticmethod
    def get_user_dict(
        id: int,
        username: str,
        date_birth: str,
        email: str,
        phone: str
    ) -> dict:
        user: User = User(
            id=id,
            username=username,
            date_birth=date_birth,
            email=email,
            phone=phone
        )
        return {
            "id": user.id,
            "username": user.username,
            "date_birth": str(user.date_birth),
            "age": user.age,
            "email": user.email,
            "phone": user.phone
        }
    
    @staticmethod
    def get_user_str(
        user: dict
    ) -> dict:
        return f'''
            id - {user.get('id')}
            username - {user.get('username')}
            date_birth - {str(user.get('date_birth'))}
            age - {user.get('age')}
            email - {user.get('email')}
            phone - {user.get('phone')}
        '''
        

class GetErrors:
    """Collecting all errors from requests.post in client.py
    for app.py route 'insert_user'"""

    @staticmethod
    def get_errors_list(data: dict) -> list:
        errors: list[dict] = [] 

        try: 
            id_: str = data["id"] 
        except KeyError: 
            print("No key <id>") 
            errors.append( 
                { 
                    "error": "no key <id>" 
                } 
            ) 
        try: 
            username: str = data['username'] 
        except KeyError: 
            print("no key <username>") 
            errors.append( 
                { 
                    "error": "no key <username>" 
                } 
            ) 
        try: 
            username: str = data['date_birth'] 
        except KeyError: 
            print("no key <date_birth>") 
            errors.append( 
                { 
                    "error": "no key <date_birth>" 
                } 
            ) 
        try: 
            username: str = data['age'] 
        except KeyError: 
            print("no key <age>") 
            errors.append( 
                { 
                    "error": "no key <age>" 
                } 
            ) 
        try: 
            username: str = data['email'] 
        except KeyError: 
            print("no key <email>") 
            errors.append( 
                { 
                    "error": "no key <email>" 
                } 
            ) 
        try: 
            username: str = data['phone'] 
        except KeyError: 
            print("no key <phone>") 
            errors.append( 
                { 
                    "error": "no key <phone>" 
                } 
            ) 
        
        return errors