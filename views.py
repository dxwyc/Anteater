from utils import app
from login import login

app.register_blueprint(login, url_prefix='/login')

