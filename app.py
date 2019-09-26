from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# class News(db.Model):
#     # id = db.Column(db.Integer, primary_key=True)

#     __tablename__ = "news"

#     news_title = db.Column(db.String(50), nullable=False)
#     news_category = db.Column(db.String(20), nullable=False)
#     posted_date = db.Column(db.DateTime, default=datetime.utcnow)
#     news_summary = db.Column(db.String(300), nullable=False)
#     news_source_link = db.Column(db.String(500), nullable=False)
#     news_image_link = db.Column(db.String(500), nullable=False)
    

#     def __repr__(self):
#         return '<News %r>' % self.id


allNews = [
    {
        
    }
]

@app.route('/')
def index():
    # allNews = News.query.order_by(News.posted_date).all()
    return render_template('card.html', title='All News', allNews=allNews)

@app.route('/india')
def india():
    return render_template('base.html', title='India')

@app.route('/world')
def world():
    return render_template('base.html', title='World')

@app.route('/technology')
def technology():
    return render_template('base.html', title='Technology')

@app.route('/business')
def business():
    return render_template('base.html', title='Business')
    
@app.route('/sports')
def sports():
    return render_template('base.html', title='Sports')

@app.route('/politics')
def politics():
    return render_template('base.html', title='Politics')

@app.route('/entertainment')
def entertainment():
    return render_template('base.html', title='Entertainment')
    
@app.route('/science')
def science():
    return render_template('base.html', title='Science')

@app.route('/automobile')
def automobile():
    return render_template('base.html', title='Automobile')

if __name__ == '__main__':
    app.run(debug=True)

