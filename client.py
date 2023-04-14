# requests 
import requests 
import json 
# Local files
import models
# random
import random
import names
 
 
URL = "http://localhost:8080" 
API = { 
    "insert": "/api/v1/insertUser", 
    "get": "/api/v1/getUser" 
} 
 
def get_info(): 
    users: list[dict] = []

    i: int
    for i in range(50):
        user = models.User.get_user_dict(
            id=i,
            username=names.get_first_name(),
            date_birth= \
                f'0{random.randint(1, 9)}-{random.randint(1, 9)}-{random.randint(1900,2005)}',
            email=f'{names.get_first_name().lower()}@{random.choice(models.pattern_email)}',
            phone=f'87{random.randint(10, 99)}{random.randint(1000000, 9999999)}'
        )
        request_to_insert_user = \
        requests.post( 
            url=URL+API['insert'], 
            json=user
        ) 
        result = request_to_insert_user 
        try: 
            data: dict = result.json() 
            try: 
                check: str = data['success'] 
                users.append(data)
            except: 
                print(data['error']) 
        except: return "Server response is not correct"

    request_to_get_users = \
        requests.post( 
            url=URL+API['get']
        ) 
    result = request_to_get_users 

    data = result.json()
    id: str = input()
    
    if id == 'all':
        i: int
        for i in range(50):
            print("User - {0}".format(
                    models.User.get_user_str(data.get('success').get(f'{i}'))
                )
            )
    elif int(id) > 49:
        print("inputed id is not correct") 
    else:
        try: 
            print(
                "User - {0}".format(
                    models.User.get_user_str(data.get('success').get(f'{id}'))
                )
            ) 
        except: 
            print("no User") 
get_info()