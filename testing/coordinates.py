from pyproj import CRS , Transformer
from main_app.models import Coordinates


transformer = Transformer.from_crs( "EPSG:2100","EPSG:4326" )#"EPSG:4087","EPSG:2100"

print(transformer.transform(152741.83 ,4373002.16))#

print(Coordinates.objects.all())


#create world coordinates from greek ones
for xy in Coordinates.objects.all():
...     res = transformer.transform(xy.x_value , xy.y_value)
...     ok = xy
...     ok.world_x = res[0]
...     ok.world_y = res[1]
...     ok.save()