#!venv/bin/python3
# run.py - A&B Roofing App

from felicity_site import app

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)