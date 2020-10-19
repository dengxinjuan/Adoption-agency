from models import Pet,db
from app import app

#create all table
db.create_all()

# empty the existing table 
Pet.query.delete()

# add pets

woofly = Pet(id=1,name="woofly",species="dog",photo_url="https://i.pinimg.com/564x/60/a3/93/60a393b29c07f29b45d644a9e6f1ffcc.jpg",age="2",
notes="",available=True)

Porchetta = Pet(id=2,name="Porchetta",species="Rabbit",photo_url="https://i.pinimg.com/564x/24/b0/1c/24b01c1a095ee62f16dce823731de6c8.jpg",age="0",
notes="a very lovely friend",available=True)

Snargle = Pet(id=3,name="Snargel",species="cat",photo_url="https://i.pinimg.com/564x/03/2f/fe/032ffe5d4e498656f1649f7fa0db9641.jpg",age="1",
notes="",available=True)

xiaohei = Pet(id=4,name="xiaohei",species="dog",photo_url="https://i.pinimg.com/564x/2c/0c/4a/2c0c4a7e8f2e3a2494eba40ec71e60a0.jpg",age="4",
notes="",available=True)

cutie = Pet(id=5,name="cutie",species="monkey",photo_url="https://i.pinimg.com/236x/44/e2/12/44e212568dcc1cffe7ea303272fe0b33.jpg",age="4",
notes="",available=True)

peppa = Pet(id=6,name="peppa",species="pig",photo_url="https://i.pinimg.com/564x/3e/47/81/3e47812fc18e0176b8149003ceb35b3e.jpg",age="5",
notes="",available=True)


db.session.add_all([woofly,Porchetta,Snargle,xiaohei,cutie,peppa])
db.session.commit()




