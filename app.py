# Flask 
import flask 
# Local files
import models

 
app: flask.app.Flask = flask.Flask(__name__) 
app.secret_key: str = "qwerty12345" 
USERS: dict = {} 
 
@app.route('/api/v1/insertUser', methods=['POST', 'GET']) 
def insert_user() -> str: 
    data = flask.request.get_json() 
    errors: list = models.GetErrors.get_errors_list(data)

    if len(errors) > 0: 
        return flask.json.dumps( 
            { 
                'error': errors 
            } 
        ) 
    
    id: str = data.get('id')
    USERS[id] = data
    return flask.json.dumps( 
        { 
            "success": '0' 
        } 
    ) 
 
 
@app.route('/api/v1/getUser', methods=['POST', 'GET']) 
def get_user() -> str: 
    return flask.json.dumps( 
        { 
            "success": USERS 
        } 
    ) 
 
 
if __name__ == '__main__': 
    app.run( 
        host='localhost', 
        port=8080, 
        debug=True 
    )