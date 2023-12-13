from .models import ApiData
import json
file_path = r'C:\Users\dagad\Downloads\jsondata.json'

with open(file_path,encoding='iso-8859-1') as f: #context manager
    dt = json.load(f)


def save_data():
    for i in dt:
        ApiData.objects.create(
            end_yr=i['end_year'],
        intensity = i['intensity'],
        sector = i['sector'],
        topic = i['topic'],
        insight = i['insight'],
        url = i['url'],
        region = i['region'],
        start_year = i['start_year'],
        impact = i['impact'],
        added = i['added'],
        published = i['published'],
        country = i['country'],
        relevance = i['relevance'],
        pestle = i['pestle'],
        source = i['source'],
        title = i['title'],
        likelihood = i['likelihood']

    )
save_data()
