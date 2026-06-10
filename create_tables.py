from src.database.db import engine
from src.database.db import Base

# Import model so SQLAlchemy knows about it
from src.database.lead_model import Lead

Base.metadata.create_all(bind=engine)

print("Tables created successfully")