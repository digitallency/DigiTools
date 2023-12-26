def generateMeteDataFromAQuery(iQuery):
    from sql_metadata import Parser

    # query="""
    # SELECT 
    # 	country.country_name_eng,
    # 	SUM(CASE WHEN call.id IS NOT NULL THEN 1 ELSE 0 END) AS calls,
    # 	AVG(ISNULL(DATEDIFF(SECOND, call.start_time, call.end_time),0)) AS avg_difference
    # FROM country 
    # LEFT JOIN city ON city.country_id = country.id
    # LEFT JOIN customer ON city.id = customer.city_id
    # LEFT JOIN call ON call.customer_id = customer.id
    # CROSS JOIN (SELECT RAND() as RAND_ID FROM DUAL) CONSTVALS
    # GROUP BY 
    # 	country.id,
    # 	country.country_name_eng
    # HAVING AVG(ISNULL(DATEDIFF(SECOND, call.start_time, call.end_time),0)) > (SELECT AVG(DATEDIFF(SECOND, call.start_time, call.end_time)) FROM call)
    # ORDER BY calls DESC, country.id ASC
    # """
    query=iQuery

    # Parse the query and extract metadata
    print(query)
    parser = Parser(query)
    # metadata = parser.parse(query)

    # Get the table and column names referenced in the query
    tables = parser.tables
    columns=parser.columns
    alliases=parser.columns_aliases
    alliases_dict=parser.columns_aliases_dict
    columns_dict=parser.columns_dict
    subQ=parser.subqueries

    dependentTableCount=0
    dependentColumnCount=0
    alliasIndex=0
    alliasDictIndex=0
    columnsDictIndex=0
    subQIndex=0

    for allias in alliases:
        alliasIndex+=1
        print("Allias ",alliasIndex,":",allias)
    for allias_d in alliases_dict:
        alliasDictIndex+=1
        print("Allias Names ",alliasDictIndex,":",allias_d)
    for columns_d in columns_dict:
        columnsDictIndex+=1
        print("Column Dict ",columnsDictIndex,":",columns_d)
        
    for subq in subQ:
        subQIndex+=1
        print("Sub Query ",subQIndex,":",subq)

    for table in tables:
        dependentTableCount+=1
        print("Dependent Table",dependentTableCount,":",table)
        dependentColumnCount=0
        for column in columns:
            if(column[0:len(table)]==table):
                dependentColumnCount+=1
                startIndex=len(table)+1
                csplt=column.split(".")
                print("\tDependent Column",dependentColumnCount,":",csplt[1])
    
    tokens=parser.tokens
    tokenIndex=-1

    for token in tokens:
        tokenIndex+=1
        print("Token Index:",tokenIndex,"\tToken Value:",token.value)


    # columns=tables[table].columns
    # dependentColumnCount=0
    # for column in columns:
    #     dependentColumnCount+=1
    #     print("\tDependent Column",dependentColumnCount,"Of",table,"Table :",column)

def generateMeteDataFromAQueryFile(fileName):
    with open(fileName, 'r') as dosya:
        query = dosya.read()
    generateMeteDataFromAQuery(query)

def generateMeteDataFromAQueryFileDirectory(directoryName):
    import os
    for fileName in os.listdir(directoryName):
    # Tam dosya yolu
        fqn = os.path.join(directoryName, fileName)
        generateMeteDataFromAQueryFile(fqn)