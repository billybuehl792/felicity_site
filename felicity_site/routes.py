# routes.py - routes to app pages

from flask import render_template, url_for
from felicity_site import app, media_config

@app.route('/')
def home():
    nav_image = media_config.get('nav-image')
    home_image = media_config.get('home-image')
    about_text = media_config.get('about-text')

    return render_template('home.html', title='Home', nav_image=nav_image, home_image=home_image, about_text=about_text)

@app.route('/prints')
def prints():
    nav_image = media_config.get('nav-image')
    prints = media_config.get('prints')

    return render_template('work.html', title='Prints', nav_image=nav_image, images=prints)

@app.route('/illustrations')
def illustrations():
    nav_image = media_config.get('nav-image')
    prints = media_config.get('illustrations')

    return render_template('work.html', title='Illustrations', nav_image=nav_image, images=prints)

@app.route('/shop')
def shop():
    nav_image = media_config.get('nav-image')

    return render_template('shop.html', title='Shop', nav_image=nav_image)
