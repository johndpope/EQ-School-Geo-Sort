import urllib.request, json
import math

school_data_url = "https://schoolsdirectory.eq.edu.au/Search/SearchResultGeoJsonHome?CriteriaModel.SpecificGeographicRegion=&CriteriaModel.OnlyStateSchools=true&CriteriaModel.IncludePrimarySchools=false&CriteriaModel.IncludeSecondarySchools=false&CriteriaModel.IncludePrimarySecondarySchools=false&CriteriaModel.IncludeSpecialEdSchools=false&CriteriaModel.IncludeDistanceEdSchools=false&CriteriaModel.OnlyNonStateSchools=False&CriteriaModel.SpecificIntake=&CriteriaModel.SpecificStateElectorate=&CriteriaModel.SpecificFederalElectorate=&CriteriaModel.SpecificAffiliation=&CriteriaModel.IncludeBoardingSchools=False&CriteriaModel.IncludeCampuses=false&CriteriaModel.IncludeApprovedCentres=false&CriteriaModel.StateAndNonStateSchoolsOnly=false&CriteriaModel.OnlyOrgUnits=False&CriteriaModel.FullTextString=&CriteriaModel.IncludeOpenCentres=True&Headless=False&FullTextString="

home_coordinates = [0,0]  #Enter your center location coordinates here!
if(home_coordinates == [0,0]):
    print("+ Please Edit Home Coordinates!")
def getDistance(longitude_location, latitude_location, longitude_home, latitude_home):

    # convert decimal degrees to radians
    longitude_home, latitude_home, longitude_location, latitude_location = map(math.radians, [longitude_home, latitude_home, longitude_location,  latitude_location])

    # haversine formula
    longitude_difference = longitude_location - longitude_home
    latitude_difference = latitude_location - latitude_home
    temp = math.sin(latitude_difference/2)**2 + math.cos(latitude_home) * math.cos(latitude_location) * math.sin(longitude_difference/2)**2
    km = (2 * math.asin(math.sqrt(temp))) *  6367
    return km

with urllib.request.urlopen(school_data_url) as url:
    print("- Fetching School List...")
    data = json.loads(url.read().decode())
    print("- School List Fetched Successfully!")
    print("-",len(data["features"]),"schools found.")
    radius = input("+ Search Radius (KM): ")
    print("- Beginning Search...")
    print("- Using Home Coordinates:",home_coordinates

    filtered_schools = []
    for school in data["features"]:
        coordinates = school["geometry"]["coordinates"]
        if(getDistance(home_coordinates[0],home_coordinates[1],coordinates[1],coordinates[0]) < float(radius)):
            filtered_schools.append(school)
    print("- Finished Sorting Schools!")
    print("- Found",len(filtered_schools),"applicable schools")
    print("- Printing Applicable Schools...\n")
    for school in filtered_schools:
        print("+",school["properties"]["centrename"])
        print("+",school["properties"]["internetsite"])
        print("+",school["properties"]["emailaddress"])
        print("\n")
