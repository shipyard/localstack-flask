from flask import (
    Blueprint,
    render_template
)

from src.models import Counter


blueprint = Blueprint('counter', __name__)


@blueprint.route('/')
def index():
    counter = Counter.get_create(label='Test')
    counter.increment()
    return render_template('counter.html', counters=Counter.list())
