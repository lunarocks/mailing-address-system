# mailing-address-system
Simple script to turn csv into full addresses and add them to a point feature class

The provided csv file has the addresses broken down into individual columns. In order to easily print labels, this script adds one field with full mailing addresses. 
To do this, an update cursor was used to add the full mailing address to a new “mailing_address” column. The “mailing_address” is the FULLADDR, STATE, and ZIP_5 columns combined. 
Note: There are over 3 million address points in the original csv. Debugging was performed with an extract of the data. 
