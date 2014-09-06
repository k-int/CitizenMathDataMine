Howto..

1. Download and install python 2
2. Download and install google app engine
3. Download and install coursebuilder(http://releases.course-builder.googlecode.com/git/coursebuilder_1.6.0_20140221_144131.zip)
4. Copy get.py to coursebuilder/tools/etl
5. cd to ~/coursebuilder and run 

    python tools/etl/get.py download datastore / citizenmaths1 citizenmaths1.appspot.com --archive_path archive.zip --datastore_types Student,StudentPropertyEntity

6. copy archive.zip here and run

    python toCsv.py from 
