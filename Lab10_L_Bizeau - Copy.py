import arcpy

def main():
    
    # user inputs a feature class path
    fc = r"C:\Python_GIS\Week10\Lab10\Virginia_Site_Address_Point_Dataset_2021Q2.gdb/addresses_fc"

    # set overwrite to true and set workspace gdb
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = r"C:\Python_GIS\Week10\Lab10\Virginia_Site_Address_Point_Dataset_2021Q2.gdb"

    # create new field in the feature class and declare all needed fields
    arcpy.AddField_management(fc, "mailing_address", "TEXT", 50)
    fields = ["FULLADDR",  "STATE", "ZIP_5", "mailing_address"]

    # update cursor to update the value of newly created field for each row
    with arcpy.da.UpdateCursor(fc, fields) as cursor:
        for row in cursor:
            row[3] = (str(row[0]) + ", " + str(row[1]) + " " + str(row[2]))
            cursor.updateRow(row)


if __name__ == "__main__":
    main()
