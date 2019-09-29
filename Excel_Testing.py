#File to test out gathering data from excel
#link to pip I installed: https://www.geeksforgeeks.org/reading-excel-file-using-python/
import xlrd

#file and location change to where you have it stored
loc = ("C:\\Users\\taboe\\Documents\\PythonStuff\\DnD_Calculator_Python-master\\DnD_4eDatabase.xlsx")
print(loc)

#opening the excel
wb = xlrd.open_workbook(loc)
sht0 = wb.sheet_by_index(0)

print("---------Single Cell---------")
print(sht0.cell_value(0,0)) #cell_value description(row, column)/cell N3 is (14,3)

shtRace = wb.sheet_by_index(2) #race table
#print out each row in the Race table
print("---------Row Printing---------")
for i in range(shtRace.nrows): #nrows: gets the number of rows
    print(shtRace.cell_value(i,0)+":"+shtRace.cell_value(i,1)) #prints out race key:race name
#if there are multiple tables in the sheet it will pull data from the table that starts in A1

shtAbilityScore = wb.sheet_by_index(3) #ability score table
#print out each row in the Race table
print("---------Column Printing---------")
for i in range(shtAbilityScore.ncols): #ncols: gets the number of columns
    print(shtAbilityScore.cell_value(0,i)) #prints out AbilityScore table columns
#if there are multiple tables in the sheet it will pull data from the table that starts in A1

shtWeapon = wb.sheet_by_index(10) #weapon table
#prints out the full row
print("---------Print Single Row---------")
print(shtWeapon.row_values(4))

#prints out a table via rows then columns
print("---------Table Via Rows---------")
for i in range(shtAbilityScore.nrows): #nrows: gets the number of rows
    print(shtAbilityScore.row_values(i))
print("---------Table Via Columns---------")
for i in range(shtAbilityScore.ncols): #nrows: gets the number of rows
    print(shtAbilityScore.col_values(i))
