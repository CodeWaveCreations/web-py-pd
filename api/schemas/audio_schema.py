from flask_marshmallow import Marshmallow

ma = Marshmallow()


class AudioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')
