=======
HB Eats
=======

HB Eats is, in its current incarnation, a static website that shows you places
to eat nearby Hackbright Academy. I started the project while working there as
a Teaching Assistant, and I built it to get practice with APIs. My restaurant 
data came from the Yelp API, and my distance data came from the Google Maps 
Distance Matrix API.

Good news: it's deployed! `Check it out on Heroku. 
<https://hbeats.herokuapp.com/>`_

.. image:: https://github.com/jgriffith23/hb-eats/blob/master/images/hbeats.png?raw=true


Setup
=====

If you want to run your own version of HB Eats (or perhaps fork it and modify it
to work for a totally different sort of location), here's how to get started.

First, make sure you have Python and PostgreSQL installed. Then:

#. Clone this repo.

#. Create and activate a Python 2.7 virtual environment. (Updating for Python 3
   is on my list of things to do, but it's not done yet.)

   .. parsed-literal::

       $ virtualenv env
       $ source env/bin/activate

#. Install the requirements. ``pip install -r requirements.txt`

#. Sign up for API keys for Yelp Fusion and Google Maps Distance Matrix.

#. Put those keys, a secret key for Flask, and a DEBUG variable into your 
   environment. I recommend making a `secrets.sh` file with the following in it:

   .. code-block:: bash

       export YELP_APP_ID="your-yelp-app-id"
       export YELP_APP_SECRET="your-yelp-secret"
       export GOOGLE_MAPS_DISTANCE_MATRIX_API_KEY="your-gmaps-dm-secret"
       export FLASK_SECRET_KEY="your-chosen-flask-key"
       export DEBUG=True

   Set DEBUG to True for development.

   And don't forget to keep your secrets off the Internet. Add `secrets.sh` to
   your `.gitignore` file now.

   With this file created, just ``source`` it to get your variables in the
   environment:

   .. code-block:: bash

       source secrets.sh

At this point you shuold have a Python environment with all requirements
installed, it should be active, and you should have all required environment
variables exported. Check the steps above if you think you missed something.

Now, create a database:

.. parsed-literal::

    $ createdb hbeats

Run *model.py* interactively:

.. parsed-literal::

    $ python -i model.py

Inside Python, create the tables needed for this project:

.. parsed-literal::

    >>> db.create_all()

If you don't get any error messages, try running *seed_functions.py*. If this
step is successful, you should now have a working database full of data.

*Note: I suggest running this step on a weekday if you want weekday lunch info.
The focus of this project was getting data out of APIs, so ensuring a weekday
was always used wasn't a high priority.*

*Other Note: Setting up an automatic way to update the database each day is
high on my list of things to do next.*

Run *server.py*, and go to *http://localhost:5000* in your browser. You should
see your lunch options.


Helpful Resources
=================

- `Yelp Fusion Docs <https://www.yelp.com/developers/documentation/v3>`_ 
  (they're so good!)

- `Google Maps Distance Matrix docs
  <https://developers.google.com/maps/documentation/distance-matrix/intro>`_
  (Though if I revisit this project any time soon, I'm going to rework it to
  use PostGIS instead. Seriously, that's way better and would allow users to
  select for more specific distances.)

- `Datetime <https://docs.python.org/2/library/datetime.html>`_ and `Time docs 
  <https://docs.python.org/2/library/time.html>`_ (for the part in *yelp_api.py* 
  code that creates a Unix timestamp for the API request)