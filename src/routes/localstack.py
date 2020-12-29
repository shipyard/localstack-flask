import uuid

import localstack_client.session
from flask import Blueprint
from flask import jsonify
from flask import redirect
from flask import url_for


BUCKET = 'test-bucket'

blueprint = Blueprint('aws', __name__)


def s3_client():
    return localstack_client.session.Session().client('s3')


@blueprint.route('/files')
def files():
    s3_client().create_bucket(Bucket=BUCKET)
    return jsonify(s3_client().list_objects(Bucket=BUCKET))


@blueprint.route('/files/create')
def add_file():
    s3_client().put_object(Bucket=BUCKET,
                           Key='{}.txt'.format(uuid.uuid1()),
                           Body=b'some content')
    return redirect(url_for('.files'))
