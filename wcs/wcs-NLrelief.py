from owslib.wcs import WebCoverageService

wcslayer = WebCoverageService('https://geoservice.dlr.de/eoc/basemap/wcs',version='1.0.0')

# Take a look at the contents (coverages) of the wcs.
for content in wcslayer.contents:
	print('contents: ', content)
	
baselayer = wcslayer['eoc:world_relief_dark']

# Take a look at the attributes of the coverage
dir(baselayer)
print('bounding box: ', baselayer.boundingBoxWGS84)
print('time positions: ', baselayer.timepositions)
print('supported formats: ', baselayer.supportedFormats)

# mock up a simple GetCoverage request.
output = wcslayer.getCoverage(	identifier='eoc:world_relief_dark',
							width=350,
							height=350,
							crs='EPSG:4326',
							bbox=(3.31497114423, 50.803721015, 7.09205325687, 53.7104033474),
							format='GeoTIFF')
							
# Write the file out to disk.
f = open('data.tif','wb')
f.write(output.read())
f.close()
print('done')
