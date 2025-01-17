from repository import Repository
from services import Services
from ui import UI

def main():
    repo = Repository()
    services = Services(repo)
    ui = UI(services)
    ui.run_main_menu()
    
main()