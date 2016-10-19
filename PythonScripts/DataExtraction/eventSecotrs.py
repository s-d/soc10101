import pymysql


def get_event_sectors(event_table, pattern_no):

    tolerance = 10
    con = pymysql.connect(host='localhost', port=3306, user='root', passwd='admin', db='schoolsv6')
    curr = con.cursor()

    curr.execute("SELECT patternX FROM fittssectorid WHERE patternRef = %s", pattern_no)
    pattern_sectors = []
    for row in curr:
        pattern_sectors.append(list(row))

    query = "SELECT collectionref, sequenceNo, patternRef, xCoord FROM %s WHERE patternRef = %s" %(event_table, pattern_no)
    curr.execute(query)
    header = ['collectionref', 'sequenceNo', 'patternRef', 'xCoord', 'sectorID']
    event_sectors = [header]
    for row in curr:
        sector_count = 1
        for val in pattern_sectors:
            if row[3] > (val[0] - tolerance):
                sector_count += 1

        temp_row = list(row)
        temp_row.append(sector_count)
        event_sectors.append(temp_row)

    return event_sectors
