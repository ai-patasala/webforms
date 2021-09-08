###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request,jsonify
from forms import ContactForm
import pandas as pd
from sqlalchemy import create_engine


###############################################
#          Define flask app                   #
###############################################
app = Flask(__name__)
app.secret_key = 'dev fao football app'


###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET", "POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        res = pd.DataFrame(dict(request.form), index=[0])
        engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                               .format(user="root",
                                       pw="mypass",
                                       db="webforms"))
        #query = """INSERT INTO contactus VALUES ("anil","anilgmail.com","hyderbad","banking",98765432)"""
        res.to_sql('contactus', con=engine, if_exists='append', chunksize=1000,index=None)
        return jsonify(True),200
    else:
        return render_template('contact.html', form=form)


###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)
