# from . import Personal, District, Temperature, School, Building, Requisites
from main.MyModelFile import MyModel
from main.models.DistrictModel import District
from main.models.SchoolModel import School
from main.models.BuildingModel import Building
from main.models.PersonalModel import ZavHoz, Personal, Bookkeeper, Director, Updater
from main.models.RequisitesModel import Requisites
from main.models.TemperatureModel import Temperature
from main.models.DocumentsModel import Document
from main.models.OrdersModel import Rospotreb, Gospozh, Rostech, Sudeb, OtherOrders
from main.models.Mandate import MandateAssembly, MandateCouncil

__all__ = [
    "Personal",
    "District",
    "Temperature",
    "School",
    "Building",
    "Requisites",
    "Document",
    "Rospotreb",
    "Gospozh",
    "Rostech",
    "Sudeb",
    "OtherOrders",
    'MandateCouncil',
    'MandateAssembly',
]
