from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


engine = create_engine('sqlite:///test.db')
metadata_obj = MetaData()
metadata_obj.create_all(engine)

users = Table('users', metadata_obj,
Column('id', Integer, primary_key=True),
Column('name', String),
Column('fullname', String),)

addresses = Table('addresses', metadata_obj,
Column('id', Integer, primary_key=True),
Column('user_id', None, ForeignKey('users.id')),
Column('email_address', String, nullable=False))

ins = users.insert()
ins = users.insert().values(name='jackaaaa',fullname='jackaaa jonea')
ins.compile().params
conn = engine.connect() 
result = conn.execute(ins)
ins.bind = engine
print(result.inserted_primary_key)
xxxxxxx


                                         
                                         

                     