from owslib.wms import WebMapService 
wms = WebMapService('http://mesonet.agron.iastate.edu/cgi-bin/wms/nexrad/n0r.cgi', version= '1.1.1') 
print('type: ', wms.identification.type) 
print('version: ', wms.identification.version) 
print('title: ', wms.identification.title) 
print('abstract: ', wms.identification.abstract) 
print('contents: ', list(wms.contents)) 
print('content title: ', wms['nexrad-n0r-900913-m05m'].title) 
print('queryable: ', wms['nexrad-n0r-900913-m05m'].queryable) 
print('opaque: ', wms['nexrad-n0r-900913-m05m'].opaque) 
print('bounding box: ', wms['nexrad-n0r-900913-m05m'].boundingBox) 
print('bounding box wgs84: ', wms['nexrad-n0r-900913-m05m'].boundingBoxWGS84) 
print('crs options: ', wms['nexrad-n0r-900913-m05m'].crsOptions) 
print('styles: ', wms['nexrad-n0r-900913-m05m'].styles) 
print([op.name for op in wms.operations]) 
print('methods: ', wms.getOperationByName('GetMap').methods) 
print('format options: ', wms.getOperationByName('GetMap').formatOptions) 
img = wms.getmap(	layers=['nexrad-n0r-m50m'],
					styles=[''],
					srs='EPSG:4326',
					bbox=(-120,23,-65,40),
					size=(1200,800),
					format='image/jpeg',
					transparent=True
			) 
out = open('WeatherFrontUS.jpg', 'wb')
out.write(img.read())
out.close() 	
print('done')
