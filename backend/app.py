from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from flask_migrate import Migrate

from googletrans import Translator
import MeCab

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tak8799you@localhost/japanese_freq'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)



class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    description = db.Column(db.Text(10000), nullable=False)

    def __repr__(self):
        return f"Event: {self.description}"

    def __init__(self, description):
        self.description = description

def format_event(event):
    return {
        "description": event.description,
        "id": event.id,
        "create_at": event.create_at
    }

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Category {self.id}: {self.name}>'

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Language {self.id}: {self.name}>'

@app.route('/')
def hello():
    return 'Hey!'

# create an event
@app.route('/events', methods = ['POST'])
def create_event():
    description = request.json['description']
    event = Event(description)
    db.session.add(event)
    db.session.commit()
    return format_event(event)

# get all events
@app.route('/events', methods = ['GET'])
def get_events():
    events = Event.query.order_by(Event.id.asc()).all()
    event_list = []
    for event in events:
        event_list.append(format_event(event))
    return {'events': event_list}

# get single event
@app.route('/events/<id>', methods = ['GET'])
def get_event(id):
    event = Event.query.filter_by(id=id).one()
    formatted_event = format_event(event)
    # print(formatted_event["description"])
    mecabTagger = MeCab.Tagger()
    count = {}
    # print(mecabTagger.parse(formatted_event["description"]))
    
    node = mecabTagger.parseToNode(formatted_event["description"])
    while node:
        word = node.surface
        hinshi = node.feature.split(",")[0]
        if word in count.keys() and hinshi == "名詞":
            freq = count[word]
            count[word] = freq + 1
        elif hinshi == "名詞":
            count[word] = 1
        elif word in count.keys() and hinshi == "形容詞":
            freq = count[word]
            count[word] = freq + 1
        elif hinshi == "形容詞":
            count[word] = 1
        elif word in count.keys() and hinshi == "形状詞":
            freq = count[word]
            count[word] = freq + 1
        elif hinshi == "形状詞":
            count[word] = 1
        elif word in count.keys() and hinshi == "動詞":
            freq = count[word]
            count[word] = freq + 1
        elif hinshi == "動詞":
            count[word] = 1
        else:
            pass
        node = node.next
    count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    print(type(count[0]))
    print(count[0][0])

    translator = Translator()

    translation = translator.translate(count[0], dest='en')
    listed = list(count[0])
    listed.append(translation.text)
    print(listed)

    listedArr = []

    for each in count:
        listedArr.append(list(each))
    print(listedArr)

    for each in listedArr:
        each.append(translator.translate(each[0], dest='en').text)
    print(listedArr)

    return {'event': listedArr}

# delete an event
@app.route('/events/<id>', methods = ['DELETE'])
def delete_event(id):
    event = Event.query.filter_by(id=id).one()
    db.session.delete(event)
    db.session.commit()
    return f'Event (id: {id}) deleted!'

# edit an event
# @app.route('/events/<id>', methods = ['PUT'])
# def update_event(id):
#     event = Event.query.filter_by(id=id)
#     description = request.json['description']
#     event.update(dict(description = description, create_at = datetime.utcnow()))
#     db.session.commit()
#     return {'event': format_event(event.one())}

if __name__ == '__main__':
    app.run()