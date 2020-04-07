from pyproj import CRS , Transformer

transformer = Transformer.from_crs( "EPSG:2100","EPSG:4326" )#"EPSG:4087","EPSG:2100"

print(transformer.transform(152741.83 ,4373002.16))#