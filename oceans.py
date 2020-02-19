from owslib.wcs import WebCoverageService
wcs=WebCoverageService('https://oceanwatch.pfeg.noaa.gov/thredds/wcs/satellite/QA/wekm/14day',version='1.0.0')
# Take a look at the contents (coverages) of the wcs.
print('contents: ', wcs.contents)
qawekm=wcs['QAwekm']
# Take a look at the attributes of the coverage
dir(qawekm)
print('bounding box: ', qawekm.boundingBoxWGS84)
#print('time positions: ', qawekm.timepositions)
print('supported formats: ', qawekm.supportedFormats)
# mock up a simple GetCoverage request.
output = wcs.getCoverage(identifier='QAwekm',time=['2019-07-02T03:11:59.000Z'],bbox=(0, -74, 350, 60),format='GeoTIFF')
# Write the file out to disk.
f=open('oceans.tif','wb')
f.write(output.read())
f.close()
print('done')
