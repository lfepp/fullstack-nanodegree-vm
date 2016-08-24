from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Industry, Company

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def get():
    industry = session.query(Industry).first()
    companies = session.query(Company).filter_by(industry_id=industry.id)
    output = ''
    for company in companies:
        output += "{company_name}</br>".format(company_name=company.name)
    return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
