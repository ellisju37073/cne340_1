import pandas

tables = pandas.read_excel ('https://www.eia.gov/dnav/pet/hist_xls/EMD_EPD2DXL0_PTE_R5XCA_DPGw.xls', sheet_name='Data 1',
                            header = 2, index_col='Date')

print(tables)