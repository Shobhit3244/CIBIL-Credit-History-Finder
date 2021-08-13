# -----------------Steady Imports--------------------
import json                       # To manage Incoming and Writing Data
import csv                        # To Read and Write the Input and Output File
from requests_html import *       # To Interact with the Javascript of Website


# --------------Data Gathering Module----------------
def info_gatherer(name: str):
    # Creating Browser session
    ses = HTMLSession()
    boror = name

    # Creating Payloads for Data Exchange
    payload1 = {'quarterIdSummary': 0,
                'quarterIdGrantors': 0,
                'croreAccount': 1,
                'quarterIdCrore': 0,
                'lakhAccount': 0,
                'quarterIdLakh': 0,
                'quarterDateStr': 'ALL',
                'fileType': 2,
                'searchMode': 1}
    payload2 = {'dunsNumber': '', 'borrowerName': boror, 'directorName': '',
                'directorBean.dinDir': '',
                'directorBean.panDir': '',
                'bankBean.bankId': 0,
                'stateBean.stateId': 0,
                'city': '',
                'suitSearchBean.quarterBean.quarterId': 0,
                'fileType': 2,
                'searchText': '',
                'selectedState': '',
                'selectedBank': ''}
    payload3 = {'fileType': 2,
                'suitSearchBeanJson': {"borrowerName": boror, "costAmount": "", "stateName": "",
                                       "directorName": "", "branchBean": 'null', "dunsNumber": "", "city": "",
                                       "bankBean": {"bankId": 0, "bankName": "",
                                                    "categoryBean": {"categoryId": 0, "categoryName": "",
                                                                     "categoryAllotedId": "", "active": 0,
                                                                     "enable": 'false'},
                                                    "bankNoRecords": 0, "bankTotalAmount": "", "enable": 'false',
                                                    "active": 0},
                                       "quarterBean": {"quarterId": 0, "quarterDate": 'null', "quarterDateStr": "",
                                                       "quarterName": "", "quarterMonthStr": "", "quarterYearStr": "",
                                                       "isPush": 0},
                                       "stateBean": {"stateId": 0, "stateName": "", "stateNoRecords": 0,
                                                     "stateTotalAmount": "", "category": "", "enable": 'false',
                                                     "isActive": 0}, "borrowerAddress": 'null', "borrowerId": 0,
                                       "sort": 0,
                                       "totalRecords": 0, "totalAmount": "", "quarterCol": "", "categoryBean": 'null',
                                       "noOFCGs1Cr": 0, "records1Cr": 0, "noOFCGs25Lac": 0, "records25Lac": 0,
                                       "cat": "",
                                       "catGroup": "", "fromQuarterId": 0, "toQuarterId": 0, "partyTypeId": 0,
                                       "quarterId": 0, "srNo": "", "userComments": "", "rejected": 0,
                                       "rejectComment": "",
                                       "lastLimit": 0, "firstLimit": 0, "reject": 'null', "edit": 'null',
                                       "modify": 'null',
                                       "editedTotalAmount": 'null', "editedDirectorNames": 'null',
                                       "rejectComments": 'null',
                                       "updateReject": "", "userId": 0, "isReview": "", "sortBy": 'null',
                                       "sortOrder": 'null',
                                       "summaryState": "", "summaryType": "", "directorId": 0, "directorSuffix": "",
                                       "dinNumber": "", "editedDirectorDin": 'null', "dirPan": "",
                                       "editedDirectorPan": 'null',
                                       "title": "",
                                       "directorBean": {"dirId": 0, "dir": 'null', "dinDir": "", "dirp25lId": 0,
                                                        "dirp1crId": 0, "dirPrefix": 'null', "dirSufix": 'null',
                                                        "dirStatus": 'null', "dirDeleteDate": 'null',
                                                        "panDir": ""}, "user": 'null', "importDataBean": 'null',
                                       "uploadBatchBean": 'null'},
                '_search': 'false',
                'nd': 1625811133694,
                'rows': 30,
                'page': 1,
                'sidx': '',
                'sord': 'asc'}

    # Gathering Data From the Website After Interaction
    boror = '%20'.join(boror.split())
    url = r'https://suit.cibil.com/loadSearchResultPage?fileType=2&suitSearchBeanJson={%22borrowerName%22:%22' + boror + '%22,%22costAmount%22:%22%22,%22stateName%22:%22%22,%22directorName%22:%22%22,%22branchBean%22:null,%22dunsNumber%22:%22%22,%22city%22:%22%22,%22bankBean%22:{%22bankId%22:0,%22bankName%22:%22%22,%22categoryBean%22:{%22categoryId%22:0,%22categoryName%22:%22%22,%22categoryAllotedId%22:%22%22,%22active%22:0,%22enable%22:false},%22bankNoRecords%22:0,%22bankTotalAmount%22:%22%22,%22enable%22:false,%22active%22:0},%22quarterBean%22:{%22quarterId%22:0,%22quarterDate%22:null,%22quarterDateStr%22:%22%22,%22quarterName%22:%22%22,%22quarterMonthStr%22:%22%22,%22quarterYearStr%22:%22%22,%22isPush%22:0},%22stateBean%22:{%22stateId%22:0,%22stateName%22:%22%22,%22stateNoRecords%22:0,%22stateTotalAmount%22:%22%22,%22category%22:%22%22,%22enable%22:false,%22isActive%22:0},%22borrowerAddress%22:null,%22borrowerId%22:0,%22sort%22:0,%22totalRecords%22:0,%22totalAmount%22:%22%22,%22quarterCol%22:%22%22,%22categoryBean%22:null,%22noOFCGs1Cr%22:0,%22records1Cr%22:0,%22noOFCGs25Lac%22:0,%22records25Lac%22:0,%22cat%22:%22%22,%22catGroup%22:%22%22,%22fromQuarterId%22:0,%22toQuarterId%22:0,%22partyTypeId%22:0,%22quarterId%22:0,%22srNo%22:%22%22,%22userComments%22:%22%22,%22rejected%22:0,%22rejectComment%22:%22%22,%22lastLimit%22:0,%22firstLimit%22:0,%22reject%22:null,%22edit%22:null,%22modify%22:null,%22editedTotalAmount%22:null,%22editedDirectorNames%22:null,%22rejectComments%22:null,%22updateReject%22:%22%22,%22userId%22:0,%22isReview%22:%22%22,%22sortBy%22:null,%22sortOrder%22:null,%22summaryState%22:%22%22,%22summaryType%22:%22%22,%22directorId%22:0,%22directorSuffix%22:%22%22,%22dinNumber%22:%22%22,%22editedDirectorDin%22:null,%22dirPan%22:%22%22,%22editedDirectorPan%22:null,%22title%22:%22%22,%22directorBean%22:{%22dirId%22:0,%22dir%22:null,%22dinDir%22:%22%22,%22dirp25lId%22:0,%22dirp1crId%22:0,%22dirPrefix%22:null,%22dirSufix%22:null,%22dirStatus%22:null,%22dirDeleteDate%22:null,%22panDir%22:%22%22},%22user%22:null,%22importDataBean%22:null,%22uploadBatchBean%22:null}&_search=false&nd=1625811133694&rows=15&page=1&sidx=&sord=asc'
    ses.post(url='https://suit.cibil.com/loadSuitFiledDataSearchAction', data=payload1)
    ses.post(url='https://suit.cibil.com/suitFiledAccountSearchAction', data=payload2)
    r3 = ses.get(url=url, data=payload3)

    # Returning the results
    return r3.content


# -------------------Main Loop---------------------
if __name__ == '__main__':
    # Reading the Input Files to get the Institution Names
    # Failsafe System
    while True:
        try:
            with open('namelist.csv', 'r') as rfile:
                reader = csv.reader(rfile)
                namelist = [x[0] for x in reader]
                print(namelist)
                break

        except:
            input("Please Put a 'namelist.csv' file in the program folder and press any key to continue")

    # Creating Data Storing Variable
    rdata = [['bank', 'branch', 'quarter', 'borrower', 'address', 'director', 'amount']]

    for i in namelist:
        # Traversing through the data and gathering useful information
        # Failsafe System
        try:
            data = info_gatherer(i)
            data = json.loads(data)

        except:
            continue
        # Writing Gathered Data to teh Mainstream DAta Holder
        if len(data['rows']) == 0:
            alpha = f"No Records Found For Entry: '{i}'"
            print(alpha)
            tmp = [alpha]
            rdata.append(tmp)

        else:
            for rd in data['rows']:
                tmp = [rd['bankBean']['bankName'], rd['branchBean']['branchName'], rd['quarterBean']['quarterDateStr'],
                       rd['borrowerName'], rd['importDataBean']['regaddr'], rd['directorName'], rd['totalAmount']]
                rdata.append(tmp)

    # Failsafe System
    while True:
        try:
            # Writing the Data to the output file
            with open('output.csv', 'w') as wfile:
                writer = csv.writer(wfile)
                writer.writerows(rdata)
            break
        # Failsafe System
        except:
            input("Please Close all Opened Instances of 'OUTPUT.CSV' and press enter to continue! ")
