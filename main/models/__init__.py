# from . import Personal, District, Temperature, School, Building, Requisites
from main.MyModelFile import MyModel
from main.models.DistrictModel import District
from main.models.SchoolModel import School
from main.models.BuildingModel import Building
from main.models.PersonalModel import ZavHoz, Personal, Bookkeeper, Director
from main.models.RequisitesModel import Requisites
from main.models.TemperatureModel import Temperature

__all__ = [
    "Personal",
    "District",
    "Temperature",
    "School",
    "Building",
    "Requisites",
]
