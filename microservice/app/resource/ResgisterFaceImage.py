from flask_restful import Resource, reqparse
import werkzeug
import logging

# Este archivo es para recibir imagenes y archivos ademas de json
parser = reqparse.RequestParser()
parser.add_argument('ci_number', help='This field cannot be blank', required=True)
parser.add_argument('face_file', type=werkzeug.datastructures.FileStorage, location='files')


class RegisterFaceImage(Resource):

    def post(self):

        def save_image(face_file, ci_number):
            path = "images"
            face_file.save("{}/{}_face.jpg".format(path, ci_number))
        # TODO [create response wrapper]
        success_response = {"message": "Image received successfully"}

        data = parser.parse_args()
        save_image(**data)

        return success_response