# Library imports
import uvicorn
from fastapi import FastAPI

# Create the app object
app = FastAPI()

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

#    Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)
    
#uvicorn app:app --reload
