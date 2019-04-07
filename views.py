from utils import app
from login import login
from tasks import tasks

app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(tasks, url_prefix='/tasks')
