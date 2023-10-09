from flask.views import View
from flask_restful import Resource
from flask import jsonify, request
from api.models.audio import db, Audio
from api.schemas.audio_schema import AudioSchema

audio_schema = AudioSchema()
audios_schema = AudioSchema(many=True)


class AudioView(Resource):
    def dispatch_request(self, audio_id=None):
        if request.method == 'GET':
            if audio_id is None:
                return self.get_all_audio()
            else:
                return self.get_audio_by_id(audio_id)
        elif request.method == 'POST':
            return self.post_audio()
        elif request.method == 'PUT':
            return self.put_audio(audio_id)
        elif request.method == 'DELETE':
            return self.delete_audio(audio_id)

    def get_all_audio(self):
        try:
            all_audio = Audio.query.all()
            result = audios_schema.dump(all_audio)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def get_audio_by_id(self, audio_id):
        try:
            single_audio = Audio.query.get(audio_id)
            if single_audio is None:
                return jsonify({'message': 'Audio not found'}), 404
            result = audio_schema.dump(single_audio)
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400


    def post_audio(self):
        data = request.get_json()
        name = data.get('name')
        if not name:
            return jsonify({"message": "Name is required"}), 400
        new_audio = Audio(name=name)
        db.session.add(new_audio)
        db.session.commit()
        return jsonify({"message": "Audio added successfully"}), 201

    def put_audio(self, audio_id):
        try:
            audio_to_update = Audio.query.get(audio_id)
            if audio_to_update is None:
                return jsonify({'message': 'Audio not found'}), 404

            new_name = request.json['name']
            audio_to_update.name = new_name

            db.session.commit()
            return jsonify({'message': 'Audio updated successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    def delete_audio(self, audio_id):
        try:
            audio_to_delete = Audio.query.get(audio_id)
            if audio_to_delete is None:
                return jsonify({'message': 'Audio not found'}), 404
            db.session.delete(audio_to_delete)
            db.session.commit()
            return jsonify({'message': 'Audio deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
