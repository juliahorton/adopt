from app import app, db
from models import Pet


# Create all tables within application context
app.app_context().push()
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

p1 = Pet(name="Jane", species="bunny", photo_url="https://images.unsplash.com/photo-1591382386627-349b692688ff?q=80&w=2487&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", age=1)
p2 = Pet(name="Ollie", species="dog", photo_url="https://images.unsplash.com/photo-1659875459325-1668ea539627?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8bGFicmFkb29kbGV8ZW58MHx8MHx8fDI%3D", age=5, notes="Really likes ground beef.", available=True)
p3 = Pet(name="Blossom", species="cat", photo_url="https://images.unsplash.com/photo-1573865526739-10659fec78a5?q=80&w=2515&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", age=2, notes="Currently placed with foster family.", available=False)
p4 = Pet(name="Beloved", species="rat", photo_url="https://images.unsplash.com/photo-1718220186777-9dd24d5e0111?w=700&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8cmF0fGVufDB8fDB8fHww", age=1)


db.session.add_all([p1, p2, p3, p4])
db.session.commit()