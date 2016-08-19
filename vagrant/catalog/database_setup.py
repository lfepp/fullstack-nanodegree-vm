#!/usr/bin/env python

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Industry(Base):
    """Store industries

    Arguments:
        id: Category ID
        name: Name of the industry
    """

    __tablename__ = 'industry'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)


class Company(Base):
    """Store companies within each industry

    Arguments:
        id: Item ID
        name: Name of the company
        description: Description of the company
        category_id: ID of the industry the company is under
    """

    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(String(256), nullable=False)
    industry_id = Column(Integer, ForeignKey('industry.id'))

    industry = relationship(Industry)

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)

if __name__ == '__main__':
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    # Add base industries
    industries = [
        'Automotive',
        'Electronics',
        'Engineering',
        'Pharmaceuticals',
        'Consumer Goods',
        'Food & Beverages',
        'Finance'
    ]
    for industry in industries:
        session.add(Industry(name=industry))
        session.commit()

    # Add base companies
    companies = [
        {
            'name': 'Toyota',
            'type': 'Automotive',
            'description': 'Toyota Motor Corporation is a Japanese automotive manufacturer headquartered in Toyota, Aichi, Japan. In March 2014 the multinational corporation consisted of 338,875 employees worldwide and, as of February 2016, is the 13th-largest company in the world by revenue. Toyota was the largest automobile manufacturer in 2012 (by production) ahead of the Volkswagen Group and General Motors. In July of that year, the company reported the production of its 200-millionth vehicle. Toyota is the world\'s first automobile manufacturer to produce more than 10 million vehicles per year. It did so in 2012 according to OICA, and in 2013 according to company data. As of July 2014, Toyota was the largest listed company in Japan by market capitalization (worth more than twice as much as #2-ranked SoftBank) and by revenue.'  # NOQA
        },
        {
            'name': 'Volkswagen Group',
            'type': 'Automotive',
            'description': 'Volkswagen Group and its subsidiaries, is a German multinational automotive manufacturing company headquartered in Wolfsburg, Lower Saxony, Germany. It designs, manufactures and distributes passenger and commercial vehicles, motorcycles, engines, and turbomachinery and offers related services including financing, leasing and fleet management. In 2012, it produced the second-largest number of motor vehicles of any company in the world, behind Toyota and ahead of General Motors. It has maintained the largest market share in Europe for over two decades. As of 2013, it ranked ninth in the Fortune Global 500 list of the world\'s largest companies. In 2014, it reached production output of 10.14 million vehicles.'  # NOQA
        },
        {
            'name': 'Samsung Electronics',
            'type': 'Electronics',
            'description': 'Samsung Electronics Co., Ltd. is a South Korean multinational electronics company headquartered in Suwon, South Korea. Through extremely complicated ownership structure with some circular ownership it is the flagship division of the Samsung Group, accounting for 70% of the group\'s revenue in 2012. It is the world\'s second largest information technology company by revenue, after Apple. Samsung Electronics has assembly plants and sales networks in 80 countries and employs around 370,000 people. Since 2012, Kwon Oh-hyun has served as the company\'s CEO.'  # NOQA
        },
        {
            'name': 'Fujitsu',
            'type': 'Electronics',
            'description': 'Fujitsu Ltd., commonly referred to as Fujitsu, is a Japanese multinational information technology equipment and services company headquartered in Tokyo, Japan. In 2015, it was the world\'s fourth-largest IT services provider measured by IT services revenue (after IBM, HP and Accenture). Fortune named Fujitsu as one of the world\'s most admired companies and a Global 500 company.'  # NOQA
        },
        {
            'name': 'Intel',
            'type': 'Electronics',
            'description': 'Intel Corporation is an American multinational technology company headquartered in Santa Clara, California. Intel is one of the world\'s largest and highest valued semiconductor chip makers, based on revenue. It is the inventor of the x86 series of microprocessors, the processors found in most personal computers. Intel supplies processors for computer system manufacturers such as Apple, Samsung, HP and Dell. Intel also makes motherboard chipsets, network interface controllers and integrated circuits, flash memory, graphics chips, embedded processors and other devices related to communications and computing. Intel Corporation was founded on July 18, 1968, by semiconductor pioneers Robert Noyce and Gordon Moore and widely associated with the executive leadership and vision of Andrew Grove, Intel combines advanced chip design capability with a leading-edge manufacturing capability.'  # NOQA
        },
        {
            'name': 'Canon Inc.',
            'type': 'Electronics',
            'description': 'Canon Inc. is a Japanese multinational corporation specialized in the manufacture of imaging and optical products, including cameras, camcorders, photocopiers, steppers, computer printers and medical equipment. It is headquartered in Ōta, Tokyo, Japan.'  # NOQA
        },
        {
            'name': 'General Electric',
            'type': 'Engineering',
            'description': 'General Electric is an American multinational conglomerate corporation incorporated in New York, and headquartered in Boston, Massachusetts. As of 2016, the company operates through the following segments: Power & Water, Oil and Gas, Aviation, Healthcare, Transportation and Capital which cater to the needs of Financial services, Medical devices, Life Sciences, Pharmaceutical, Automotive, Software Development and Engineering industries.'  # NOQA
        },
        {
            'name': 'Mitsui',
            'type': 'Engineering',
            'description': 'Mitsui Group is one of the largest keiretsu in Japan and one of the largest corporate groups in the world. The major companies of the group include Mitsui & Co., Sumitomo Mitsui Banking Corporation, Sapporo Breweries, Toray Industries, Mitsui Chemicals, Isetan Mitsukoshi Holdings, Sumitomo Mitsui Trust Holdings, Mitsui Engineering & Shipbuilding, Mitsui O.S.K. Lines and Mitsui Fudosan.'  # NOQA
        },
        {
            'name': 'Cardinal Health',
            'type': 'Pharmaceuticals',
            'description': 'Cardinal Health, Inc. is an American Fortune 500 health care services company based in Dublin, Ohio. The company specializes in distribution of pharmaceuticals and medical products, serving more than 100,000 locations. The company also manufactures medical and surgical products, including gloves, surgical apparel and fluid management products. In addition, it operates the nation\'s largest network of radiopharmacies. Cardinal Health provides medical products to over 75 percent of hospitals in the United States. In December 2013, it was announced that Cardinal Health would team up with CVS Caremark, which would form the largest generic drug sourcing operation in the United States. The venture was named Red Oak Sourcing and began operations in July 2014.'  # NOQA
        },
        {
            'name': 'Pfizer',
            'type': 'Pharmaceuticals',
            'description': 'Pfizer Inc. is an American global pharmaceutical corporation headquartered in New York City, with its research headquarters in Groton, Connecticut. It is among the world\'s largest pharmaceutical companies. Pfizer is listed on the New York Stock Exchange, and its shares have been a component of the Dow Jones Industrial Average since 2004.'  # NOQA
        },
        {
            'name': 'Procter & Gamble',
            'type': 'Consumer Goods',
            'description': 'Procter & Gamble Co., also known as P&G, is an American multinational consumer goods company headquartered in downtown Cincinnati, Ohio, United States, founded by William Procter and James Gamble, both from the United Kingdom. Its products include cleaning agents and personal care products. Prior to the sale of Pringles to the Kellogg Company, its product line also included foods and beverages.'  # NOQA
        },
        {
            'name': 'Nestle',
            'type': 'Food & Beverages',
            'description': 'Nestlé S.A. is a Swiss transnational food and drink company headquartered in Vevey, Vaud, Switzerland. It is the largest food company in the world measured by revenues, and ranked #72 on the Fortune Global 500 in 2014.'  # NOQA
        },
        {
            'name': 'Kraft Foods',
            'type': 'Food & Beverages',
            'description': 'Kraft Foods Group, Inc., is an American manufacturing and processing conglomerate headquartered in the Chicago suburb of Northfield, Illinois. The company was restructured in 2012 as a spin off from Kraft Foods Inc., which in turn was renamed Mondelēz International. The new Kraft Foods Group was focused mainly on grocery products for the North American market, while Mondelēz is focused on international confectionery and snack brands. Until the merger with Heinz, Kraft Foods Group was an independent public company listed on the NASDAQ stock exchange.'  # NOQA
        },
        {
            'name': 'PepsiCo',
            'type': 'Food & Beverages',
            'description': 'PepsiCo, Inc. is an American multinational food, snack and beverage corporation headquartered in Purchase, New York, United States, with interests in the manufacturing, marketing, and distribution of grain-based snack foods, beverages, and other products. PepsiCo was formed in 1965 with the merger of the Pepsi-Cola Company and Frito-Lay, Inc. PepsiCo has since expanded from its namesake product Pepsi to a broader range of food and beverage brands, the largest of which includes an acquisition of Tropicana in 1998 and of Quaker Oats in 2001, which added the Gatorade brand to its portfolio.'  # NOQA
        },
        {
            'name': 'Tyson Foods',
            'type': 'Food & Beverages',
            'description': 'Tyson Foods, Inc. is an American multinational corporation based in Springdale, Arkansas, that operates in the food industry. The company is the world\'s largest processor and marketer of chicken, beef, and pork and annually exports the largest percentage of beef out of the United States. Together with its subsidiaries it operates major food brands, including Jimmy Dean, Hillshire Farm, Sara Lee, Ball Park, Wright, Aidells, and State Fair. With 2011 sales of US$32 billion, Tyson Foods is the second-largest food production company in the Fortune 500, the second largest meat producer in the world, and according to Forbes, one of the 100 largest companies in the United States.'  # NOQA
        },
        {
            'name': 'Exor',
            'type': 'Financial',
            'description': 'Exor is an Italian investment company, controlled by the Agnelli family. With a capitalization of US$12 billion, its principal investments include Fiat Chrysler Automobiles, CNH Industrial and Ferrari. Resultantly, Exor is first as a economic group in Italy for sales volume, and the 19th in the world.'  # NOQA
        },
        {
            'name': 'Goldman Sachs',
            'type': 'Financial',
            'description': 'The Goldman Sachs Group, Inc. is an American multinational banking firm that engages in global investment banking, investment management, securities, and other financial services, primarily with institutional clients. Goldman Sachs was founded in 1869 and is headquartered at 200 West Street in Lower Manhattan, New York City, with additional offices in other international financial centers. The firm provides asset management, mergers and acquisitions advice, prime brokerage, and underwriting services to its clients, which include corporations, governments, and individuals. The firm also engages in market making and private equity deals, and is a primary dealer in the U.S. Treasury security market.'  # NOQA
        }
    ]
    for company in companies:
        industry_id = session.query(Industry).filter_by(
            name=company['type']
        ).one().id
        session.add(Company(
            name=company['name'],
            description=company['description'],
            industry_id=industry_id
        ))
        session.commit()
