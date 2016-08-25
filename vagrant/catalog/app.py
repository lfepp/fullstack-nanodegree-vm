from flask import Flask, render_template, make_response, request
from flask import session as user_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Industry, Company
import random
import string
import os
import json
import httplib2
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

config_filname = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_filname) as config_file:
    config = json.load(config_file)['web']


@app.route('/')
@app.route('/industry/')
def index():
    industries = session.query(Industry)
    companies = session.query(Company)
    return render_template(
        'index.html',
        industries=industries,
        companies=companies,
        user=user_session
    )


@app.route('/industry/<int:industry_id>')
def industry(industry_id):
    industry = session.query(Industry).filter_by(id=industry_id).one()
    companies = session.query(Company).filter_by(industry_id=industry_id)
    return render_template(
        'industry.html',
        industry=industry,
        companies=companies,
        user=user_session
    )


@app.route('/industry/<int:industry_id>/company/<int:company_id>')
def company(industry_id, company_id):
    industry = session.query(Industry).filter_by(id=industry_id).one()
    company = session.query(Company).filter_by(id=company_id).one()
    return render_template(
        'company.html',
        industry=industry,
        company=company,
        user=user_session
    )


@app.route('/login')
def login():
    state = ''.join(
        random.choice(string.ascii_uppercase + string.digits)
        for n in xrange(32)
    )
    user_session['state'] = state
    return render_template(
        'login.html',
        client_id=config['client_id'],
        state=state,
        user=user_session
    )


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != user_session['state']:
        response = make_response(json.dumps('Invalid state.'), 401)
        response.headers['Content-type'] = 'application/json'
        return response
    # Get access token
    credentials = json.loads(request.form.keys()[0])
    access_token = credentials['access_token']
    print "we get this far? 1"
    url = (
        'https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={token}'
        .format(token=access_token)
    )
    h = httplib2.Http()
    r = json.loads(h.request(url, 'GET')[1])
    # Abort login if there is an error with the access token
    print "we get this far? 2"
    if r.get('error') is not None:
        response = make_response(json.dumps(r.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify the token is for the current user
    # FIXME: But how do I get the gplus ID from the id token?
    from pprint import pprint
    pprint(credentials)
    gplus_id = credentials['id_token']
    if r['user_id'] != gplus_id:
        response = make_response(
            json.dumps('User ID does not match user ID of token', 401)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    # Verify the access token is valid for this application
    print "we get this far? 3"
    if r['issued_to'] != config['client_id']:
        response = make_response(
            json.dumps('Client ID does not match client ID of token', 401)
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    # Store the access token in the user session
    print "we get this far? 4"
    user_session['credentials'] = credentials.to_json()
    user_session['gplus_id'] = gplus_id
    # Get the user data
    print "we get this far? 5"
    url = 'https://www.googleapis.com/oauth2/v1/userinfo'
    payload = {'access_token': credentials.access_token, 'alt': 'json'}
    r = requests.get(url, params=payload)
    user_data = r.json()
    user_session['name'] = user_data['name']
    user_session['email'] = user_data['email']
    user_session['picture'] = user_data['picture']
    # Get industry and company information for index
    print "we get this far? 6"
    industries = session.query(Industry)
    companies = session.query(Company)
    return render_template(
        'index.html',
        industries=industries,
        companies=companies,
        user=user_session
    )


@app.route('/signout')
def gdisconnect():
    credentials = user_session.get('credentials')
    # Ensure user is connected
    if credentials is None:
        response = make_response(
            json.dumps('Current user is not connected'), 401
        )
        response.headers['Content-Type'] = 'application/json'
        return response
    # Revoke current access token
    url = 'https://accounts.google.com/o/oauth2/revoke?token={token}'.format(
        token=credentials['access_token']
    )
    h = httplib2.Http()
    r = h.request(url, 'GET')[0]
    # Check status and reset user_session if successful
    if r['status'] == '200':
        del user_session['credentials']
        del user_session['gplus_id']
        del user_session['name']
        del user_session['email']
        del user_session['picture']
    # Get industry and company information for index
    industries = session.query(Industry)
    companies = session.query(Company)
    return render_template(
        'index.html',
        industries=industries,
        companies=companies
    )

if __name__ == '__main__':
    app.secret_key = config['client_secret']

    app.debug = True
    app.run(host='0.0.0.0', port=5000)
