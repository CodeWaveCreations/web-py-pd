from flask import Flask
from api.models.audio import db
from api.views.audio_view import AudioView
from api.models.audio import Audio
from api.database.config import Config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
db.init_app(app)

app.add_url_rule('/audios/', view_func=AudioView.as_view('audio'))
app.add_url_rule('/audios/<int:audio_id>/', view_func=AudioView.as_view('audio_by_id'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='127.0.0.1', port=8080, debug=True)
