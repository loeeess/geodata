from owslib.wcs import WebCoverageService
wcs=WebCoverageService('http://cida.usgs.gov/thredds/wcs/prism',version='1.0.0')
# Take a look at the contents (coverages) of the wcs.
print('contents: ', wcs.contents)
tmin = wcs['tmn']
# Take a look at the attributes of the coverage
dir(tmin)
print('bounding box: ', tmin.boundingBoxWGS84)
#print('time positions: ', tmin.timepositions)
print('supported formats: ', tmin.supportedFormats)
# mock up a simple GetCoverage request.
output = wcs.getCoverage(	identifier='tmn',
							time=['1895-01-01T00:00:00Z'],
							bbox=(-125,25,-67,50),
							format='GeoTIFF')
# Write the file out to disk.
f = open('data.tif','wb')
f.write(output.read())
f.close()
print('done')
