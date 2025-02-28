from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import bcrypt

# Database setup
DATABASE_URL = "sqlite:///shop.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

app = FastAPI()

# User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    address = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)

# Product model
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)

# Order model
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)

Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Password hashing function
def hash_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    address: str = None

class UserLogin(BaseModel):
    username: str
    password: str

@app.post("/signup")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if username or email already exists
    if db.query(User).filter(User.username == user.username).first():
        return {"error": "Username already exists"}
    if db.query(User).filter(User.email == user.email).first():
        return {"error": "Email already exists"}
    
    # Create new user
    hashed_pw = hash_password(user.password)
    new_user = User(username=user.username, password=hashed_pw, email=user.email, address=user.address)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}

@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user or not bcrypt.checkpw(user.password.encode(), db_user.password.encode()):
        return {"error": "Invalid username or password"}
    return {"message": "Login successful"}

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    return user


@app.post("/users/")
def create_user(username: str, password: str, email: str, address: str = None, is_admin: bool = False, db: Session = Depends(get_db)):
    hashed_pw = hash_password(password)
    new_user = User(username=username, password=hashed_pw, email=email, address=address, is_admin=is_admin)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully", "user": new_user}

@app.post("/products/")
def create_product(name: str, description: str, price: float, stock: int, db: Session = Depends(get_db)):
    new_product = Product(name=name, description=description, price=price, stock=stock)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message": "Product added successfully", "product": new_product}

@app.post("/orders/")
def create_order(user_id: int, product_id: int, quantity: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product or product.stock < quantity:
        return {"error": "Insufficient stock or product not found"}
    
    total_price = product.price * quantity

    new_order = Order(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price)
    product.stock -= quantity
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    
    return {"message": "Order placed successfully", "order": new_order}