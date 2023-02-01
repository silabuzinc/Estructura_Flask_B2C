from app import create_app
from app.db import db

app=create_app()

@app.route('/',) #ruta raiz
def index():
    #print(db.create_all())
    return "Hola mensaje de prueba"

db.init_app(app)
with app.app_context():
    db.create_all() 
    print("BD conectada!") 

if __name__ == "__main__":
    app.run(debug=True)