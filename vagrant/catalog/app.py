from flask import Flask, render_template
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
    industries = session.query(Industry)
    companies_by_industry = {}
    for industry in industries:
        companies = session.query(Company).filter_by(industry_id=industry.id)
        companies_by_industry[industry.name] = companies
    return render_template(
        'index.html',
        industries=industries,
        companies=companies_by_industry
    )
        # for company in companies:
        #     return render_template(
        #         'company_module.html',
        #         industry=industry,
        #         companies=companies
        #     )
    # industry = session.query(Industry).first()
    # companies = session.query(Company).filter_by(industry_id=industry.id)
    # output = ''
    # for company in companies:
    #     output += "{company_name}</br>".format(company_name=company.name)
    # return output

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
