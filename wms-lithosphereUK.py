from owslib.wms import WebMapService 
wms = WebMapService('http://ogc.bgs.ac.uk/cgi-bin/BGS_Bedrock_and_Superficial_Geology/wms', version= '1.1.1') 

print('type: ', wms.identification.type) 
print('version: ', wms.identification.version) 
print('title: ', wms.identification.title) 
print('abstract: ', wms.identification.abstract) 
for content in wms.contents:
	print('contents: ', content)
	
print('content title: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].title) 
print('queryable: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].queryable) 
print('opaque: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].opaque) 
print('bounding box: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].boundingBox) 
print('bounding box wgs84: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].boundingBoxWGS84) 
print('crs options: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].crsOptions) 
print('styles: ', wms['BGS_EN_Bedrock_and_Superficial_Geology'].styles) 
print([op.name for op in wms.operations]) 
print('methods: ', wms.getOperationByName('GetMap').methods) 
print('format options: ', wms.getOperationByName('GetMap').formatOptions) 

img = wms.getmap(	layers=['BGS_EN_Bedrock_and_Superficial_Geology'],
					styles=['default'],
					srs='EPSG:4326',
					bbox=(-8.6476, 48.8639, 1.76943, 60.8622),
					size=(800,1200),
					format='image/jpeg',
					transparent=True
			) 
			
out = open('UKlithosphere.jpg', 'wb')
out.write(img.read())
out.close() 	
print('done')
