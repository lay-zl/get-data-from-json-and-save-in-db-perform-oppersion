
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('',home,name='home'),

    path('all/',all,name='all'),
    path('sector/',sector,name='sector'),
    path('financail/',financial_services_sector,name='financial_services_sector'),
    path('constructor/',Constructionr,name='contruct'),
    path('support_services/',support_services,name='support_services'),

    path('environment/',environment,name='environment'),
    path('Information_Technology/',Information_Technology,name='Information_Technology'),
    path('Energy/',Energy,name='Energy'),
    path('Healthcare/',Healthcare,name='Healthcare'),
    path('Tourism_hospitality/',Tourism_hospitality,name='Tourism_hospitality'),

    path('Media_entertainment/',Media_entertainment,name='Media_entertainment'),
    path('Security/',Security,name='Security'),
    path('Food_agriculture/',Food_agriculture,name='Food_agriculture'),
    path('Manufacturing/',Manufacturing,name='Manufacturing'),
    path('Retail/',Retail,name='Retail'),


    path('Transport/',Transport,name='Transport'),
    path('Government/',Government,name='Government'),
    path('Aerospace_defence/',Aerospace_defence,name='Aerospace_defence'),
    path('Water/',Water,name='Water'),
    path('Automotive/',Automotive,name='Automotive'),




    #region
    path('region/',region,name='region'),
    path('Southern_Africa/',Southern_Africa,name='Southern_Africa'),
    path('South_America/',South_America,name='South_America'),
    path('Europe/',Europe,name='Europe'),
    path('Africa/',Africa,name='Africa'),
    path('Southern_Europe/',Southern_Europe,name='Southern_Europe'),

    path('Oceania/',Oceania,name='Oceania'),
    path('Northern_Europe/',Northern_Europe,name='Northern_Europe'),
    path('Northern_America/',Northern_America,name='Northern_America'),
    path('Eastern_Africa/',Eastern_Africa,name='Eastern_Africa'),
    path('Western_Asia/',Western_Asia,name='Western_Asia'),


    path('South_Eastern_Asia/',South_Eastern_Asia,name='South_Eastern_Asia'),
    path('World/',World,name='World'),
    path('Asia/',Asia,name='Asia'),
    path('Southern_Asia/',Southern_Asia,name='Southern_Asia'),
    path('Eastern_Europe/',Eastern_Europe,name='Eastern_Europe'),

path('Central_Africa/',Central_Africa,name='Central_Africa'),
    path('Western_Africa/',Western_Africa,name='Western_Africa'),
    path('Western_Europe/',Western_Europe,name='Western_Europe'),
    path('Northern_Africa/',Northern_Africa,name='Northern_Africa'),
    path('Central_Asia/',Central_Asia,name='Central_Asia'),

path('Central_America/',Central_America,name='Central_America'),


    #
    path('country/',country,name='country'),

    ############
    path('chart/',show),
    # path('count/',country_count_show),
    ###################
    path('sample/',sample)

]
