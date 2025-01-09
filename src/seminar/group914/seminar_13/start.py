from ui import Console
from repository import Repository
from services import Service

repo=Repository()
service=Service(repo)
UI=Console(service)
UI.run()