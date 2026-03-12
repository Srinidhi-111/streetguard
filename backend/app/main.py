from fastapi import FastAPI
app = FastAPI(title='GigShield API', description='AI-Powered Parametric Income Insurance for Gig Workers', version='1.0.0')
@app.get('/')
def root():
    return {'message': 'GigShield API is running'}
