
from fileRecord import CapOneRecord
from databaseuploader import CapOneDB
import pyodbc


class CapOneFileObj:
    
    def normalizeFile(self, f):
        x = 0
        normFile = []
        for r in f:
           
            coR = CapOneRecord()
            ds = coR.determineRecordId(r)
           
            x = x + 1
            
            if type(ds) == list :
                normFile.append(ds)
         
        
        
        return normFile
    
    def createNewFile(self, f, cleanedFile):
        header = []
        for rw in cleanedFile:
            coR = CapOneRecord()
          
            headerType = rw[0][:2]
            
            if headerType == '10':
                header = coR.processHeader(rw)
                print(header)
            
            if headerType == '20':pass

    def processFileStringBased(self, f, actCount):
        header = []
        detail = []
        for rw in f:
            
            coRec = CapOneRecord()
            rc = coRec.processStringBasedRecord(rw)
      
            if type(rc) == list:
                if str(rc[0]) == '10':
                    header.append(rc)
                     
                if str(rc[0]) == '20':
                    
                    detail.append(rc)
        
        combined = self._combineHeaderDetail(header, detail, actCount)     
        return combined
    
    def writeFile(self, pthDest, combined, fileType):
        flName = pthDest + '\\' + 'CapOne' +  fileType + '_processed.txt'
        f = open(pthDest + '\\' + 'CapOne' +  fileType + '_processed.txt', 'a')
#         print(flName)
        for rw in combined:
            rw.append('\n')
            newRw = '|'.join(rw)
            
            f.write(newRw)
        
        f.close()
        coDB = CapOneDB(flName).go()
 
    def _combineHeaderDetail(self, header, detail, actCount):
        combined = []
        fields = self.getActivityFieldNames()
        
        if actCount == 1:
            combined.append(fields)
        for d in detail:
            newd = d + header[0]
            combined.append(newd)
            
        
        return combined
   
    def processFileStringBasedEnrolled(self, f, enrolCount):
        header = []
        detail = []
        for rw in f:
            
            coRec = CapOneRecord()
            rc = coRec.processStringBasedRecordEnrolled(rw)
      
            if type(rc) == list:
                if str(rc[0]) == '10':
                    header.append(rc)
                      
                if str(rc[0]) == '02':
                    
                    detail.append(rc)
        
        combined = self._combineHeaderDetailEnrolled(header, detail, enrolCount)  
#         print(combined)   
        return combined
    
    def _combineHeaderDetailEnrolled(self, header, detail, enrolCount):
        combined = []
        fields = self.getEnrolledFieldNames()
        
        if enrolCount == 1:
            combined.append(fields)
        for d in detail:
            newd = d + header[0]
            combined.append(newd)
            
        
        return combined
    
    def _combineHeaderDetailACC(self, header, detail, accCount):
        combined = []
        fields = self.getACCFieldNames()
#
        if accCount == 1:
            combined.append(fields)
        for d in detail:
            newd = d + header[0]
            combined.append(newd)
            
#         print(combined)
        return combined 
    
    def processFileStringBasedACC(self, f, accCount):
        header = []
        detail = []
        for rw in f:
            
            coRec = CapOneRecord()
            rc = coRec.processStringBasedRecordACC(rw)
      
            if type(rc) == list:
                if str(rc[0]) == '10':
                    header.append(rc)
                       
                if str(rc[0]) == '08':
                     
                    detail.append(rc)
        f.close()
        combined = self._combineHeaderDetailACC(header, detail, accCount)  
#         print(combined)   
        return combined
    
    def getActivityFieldNames(self):
        
        fieldNames = [
                      'Record_Id',
                      'Tacking_Number',
                      'Account_Reference_Number',
                      'PCR_Member_Number',
                      'Source_Agent',
                      'Description_Field',
                      'Promotion_Identifier',
                      'Alliance_Code',
                      'Partner_Transaction_Date',
                      'Total_PCR_Credits_Earned',
                      'Status_Code',
                      'Transaction_Status',
                      'Status_Description',
                      
                      
                      'Record_Id_Header',
                      'Version',
                      'Agent_id',
                      'File_Creation_Date',
                      'Program_Id',
                      'Description',
                      'File_Sequence_Number'
                      
                      
                      
                      
                      ]
        
        return fieldNames
    
    def getEnrolledFieldNames(self):
        
        fieldNames = [
                      'Record_Id',
                      'Account_Reference_Number',
                      'PCR_Member_Id',
                      'Card_Type',
                      'First_Name',
                      'Middle_Name',
                      'Last_Name',
                      'Address_Type',
                      'EN_Address_Line1',
                      'EN_Address_Line2',
                      'EN_City',
                      'Country_Code',
                      'EN_State/Province',
                      'EN_ZIP/Postal_Code',
                      'Language_Spoken',
                      'Phone_Number_1',
                      'Phone_Number_1_Usage_Type',
                      'Phone_Number_2',
                      'Phone_Number_2_Usage_Type',
                      'Status_Code',
                      'Transaction_Status',
                      'Status_Description',
                      
                      
                      
                      'Record_Id_Header',
                      'Version',
                      'Agent_id',
                      'File_Creation_Date',
                      'Program_Id',
                      'Description',
                      'File_Sequence_Number'
                      
                      ]
        
        return fieldNames
  
    def getACCFieldNames(self):
        
        fieldNames = [
                      
                      'Record_Id',
                      'Account_Reference_Number',
                      'PCR_Member_Id',
                      'Enrolling_Source_Code',
                      'Card_Type',
                      'Last_Name',
                      'First_Name',
                      'Language_Spoken',
                      'Status_Code',
                      'Status_Description',
                      'Transaction_Status',
                      
                      'Header_Record_Id',
                      'Version',
                      'Agent_id',
                      'File_Creation_Date',
                      'Program_Id',
                      'Description',
                      'File_Sequence_Number'
                     
                  
              
                      
                      ]
        
        return fieldNames
    

        
        
        