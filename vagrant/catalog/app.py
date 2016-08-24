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
@app.route('/industry/')
def index():
    industries = session.query(Industry)
    companies = session.query(Company)
    return render_template(
        'index.html',
        industries=industries,
        companies=companies
    )


@app.route('/industry/<int:industry_id>')
def industry(industry_id):
    industry = session.query(Industry).filter_by(id=industry_id).one()
    companies = session.query(Company).filter_by(industry_id=industry_id)
    return render_template(
        'industry.html',
        industry=industry,
        companies=companies
    )


@app.route('/industry/<int:industry_id>/company/<int:company_id>')
def company(industry_id, company_id):
    industry = session.query(Industry).filter_by(id=industry_id).one()
    company = session.query(Company).filter_by(id=company_id).one()
    return render_template(
        'company.html',
        industry=industry,
        company=company
    )

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
