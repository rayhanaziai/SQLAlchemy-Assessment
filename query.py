"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?
the value is <flask_sqlalchemy.BaseQuery at 0x7ff23c0c2c10>
the datatype is an object.




# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?
An association table us a table that is created when we have a many-to-many relationship between two tables. 
The association table is a middle table that connects the two tables and manages foreign keys.




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = db.session.query(Brand).filter_by(brand_id='ram').one()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = db.session.query(Model).filter_by(brand_id='che', name='Corvette').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year>1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter(Brand.founded==1903, Brand.discontinued ==None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter(db.or_(Brand.founded<1950, Brand.discontinued !=None)).all()

# Get any model whose brand_id is not "for."
q8 = Brand.query.filter(Brand.brand_id != "for").all()


# -------------------------------------------------------------------
# Part 4: Write Functions

def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_list = db.session.query(Model, Brand).filter(Model.year == year).join(Brand).all()

    for model, brand in model_list:
        print model.name, brand.name, brand.headquarters


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    joint_list = db.session.query(Brand, Model).join(Model, Model.brand_id == Brand.brand_id).all()

    brands_list = []

    for brand, model in joint_list:
        if brand.name in brands_list:
            print model.name, model.year
        else:
            print 'BRAND NAME:', brand.name
            print model.name, model.year
            brands_list.append(brand.name)


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
