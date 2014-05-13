import os
import pyodbc
import shutil

class CiticVerify:
    
    def readFile(self, PTH, flName):
        f = open(PTH + '\\' + flName, 'r')
        dataset = []
        header = []
        for rw in f:
            newRw = rw.split('\t')
           
            if str(newRw[0]) == 'H':
                newRwPrint = '|'.join(newRw)
                header.append(newRwPrint)
            elif str(newRw[0]) != 'H' and str(newRw[0]) != 'T':
               
                newRwPrint  = '|'.join(newRw)
               
                
                dataset.append(newRwPrint)
    
         
        return dataset, header
    
    def combine(self, hd, ds):
        finalDS = []
        hdP = '|' + str(hd[0])

        for rw in ds:
            newRW = rw.split('|')
            newRW[44] = str(newRW[44])[:-1]
            newRWP = '|'.join(newRW)
            newRWT = newRWP + hdP

            finalDS.append(newRWT)

        return finalDS

    def getFileList(self,PTH):
        
        ls = os.listdir(PTH)
        
        return ls
    
    def writeFile(self, PTHDEST, ds):
        
        V = open(PTHDEST + '\\' + 'V_processed.txt', 'a')
        E = open(PTHDEST + '\\' + 'E_processed.txt', 'a')
        
        for rw in ds:
            newRw = rw.split('|')
            
            if str(newRw[0]) == 'E':
                E.write(rw)
            if str(newRw[0]) == 'V':
                E.write(rw)
    
    def moveFilesUploaded(self, pthDest):
        
        l = os.listdir(pthDest)
        pthdesUploaded = 'C:\\IHG\\CITIC\\VERIFY\\Uploaded'
        
        for f in l:

            src = pthDest + '\\' + str(f)
            de = pthdesUploaded + '\\' + str(f)
            shutil.move(src, de)
    
    
    
          
    def process(self,PTH, PTHDEST):
        
        fls = self.getFileList(PTH)
        
        for l in fls:
            ds, h = self.readFile(PTH, l)

            fn = self.combine(h, ds)

            self.writeFile(PTHDEST, fn)
            self.uploadVerifyE(fn)
            self.moveFilesUploaded(PTHDEST)
    

    def uploadVerifyE(self,  ds): 
        conn = """DRIVER={SQL Server Native Client 11.0};Server=CN-L-CNU2141TR3\IHG;DATABASE=IHG;Trusted_Connection=yes"""

        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()  
        
        sql = """
       INSERT INTO [dbo].[Verify_E]
           ([Record_ID]
           ,[Salutation]
           ,[First_Name]
           ,[Middle_Name]
           ,[Last_Name]
           ,[Generation/Suffix]
           ,[Account_Reference_Number]
           ,[Card_Type]
           ,[Card_Holder]
           ,[E-Mail_Address]
           ,[Phone_Number_1]
           ,[Phone_Number_1_Usage_Type]
           ,[Phone_Number_1_Type]
           ,[Phone_Number_2]
           ,[Phone_Number_2_Usage_Type]
           ,[Phone_Number_2_Type]
           ,[Language_Spoken]
           ,[Language_Written]
           ,[Address_Type]
           ,[Local_Language_Address_Line_1]
           ,[Local_Language_Address_Line_2]
           ,[Local_Language_Address_Line_3]
           ,[Local_Language_Address_Line_4]
           ,[Local_Language_Address_Line_5]
           ,[Local_Language_City]
           ,[Local_Language_State/Province]
           ,[Local_Language_Zip/Postal_Code]
           ,[EN_Address_Line1]
           ,[EN_Address_Line2]
           ,[EN_Address_Line3]
           ,[EN_Address_Line4]
           ,[EN_Address_Line5]
           ,[EN_City]
           ,[EN_State/Province]
           ,[EN_Zip/Postal_Code]
           ,[Country_Code]
           ,[Preferred_Alliance]
           ,[Alliance_Code]
           ,[Alliance_Number]
           ,[Enrolling_Source_Code]
           ,[Program_Code]
           ,[PCR_Member_ID]
           ,[Transaction_Status]
           ,[Status_Code]
           ,[Status_Description]
           ,[Record_ID_header]
           ,[Version]
           ,[File_Encoding_Type]
           ,[Program_ID]
           ,[File_Creation_Date]
           ,[Agent_id]
           ,[Description]
           ,[File_Sequence_number]
           ,[File_Processed_Date])
           Values 
               (
           """
     
        for d in ds:
            
            nwD = d.split('|')

            t = "'"
            cnt = 0
            for z in nwD:
                if cnt == 0:
                    t = "'" + str(z) + "'"
                else:
                    t = t + ',' + "'" +   str(z) + "'"
                
                cnt = cnt + 1
            up = sql + t + ')'
            cursor.execute(up)
            cnxn.commit()
    
    def uploadVerifyV(self, dbAddress, database, ds): 
        conn = """DRIVER={SQL Server Native Client 11.0};Server=localHost;DATABASE=IHG;Trusted_Connection=yes"""

        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()  
        
        sql = """
        INSERT INTO [dbo].[Verify_V]
           ([Record_ID]
           ,[Salutation]
           ,[First_Name]
           ,[Middle_Name]
           ,[Last_Name]
           ,[Generation/Suffix]
           ,[Account_Reference_Number]
           ,[Card_Type]
           ,[Card_Holder]
           ,[E-Mail_Address]
           ,[Phone_Number_1]
           ,[Phone_Number_1_Usage_Type]
           ,[Phone_Number_1_Type]
           ,[Phone_Number_2]
           ,[Phone_Number_2_Usage_Type]
           ,[Phone_Number_2_Type]
           ,[Language_Spoken]
           ,[Language_Written]
           ,[Address_Type]
           ,[Local_Language_Address_Line_1]
           ,[Local_Language_Address_Line_2]
           ,[Local_Language_Address_Line_3]
           ,[Local_Language_Address_Line_4]
           ,[Local_Language_Address_Line_5]
           ,[Local_Language_City]
           ,[Local_Language_State/Province]
           ,[Local_Language_Zip/Postal_Code]
           ,[EN_Address_Line1]
           ,[EN_Address_Line2]
           ,[EN_Address_Line3]
           ,[EN_Address_Line4]
           ,[EN_Address_Line5]
           ,[EN_City]
           ,[EN_State/Province]
           ,[EN_Zip/Postal_Code]
           ,[Country_Code]
           ,[Preferred_Alliance]
           ,[Alliance_Code]
           ,[Alliance_Number]
           ,[Enrolling_Source_Code]
           ,[Program_Code]
           ,[PCR_Member_ID]
           ,[Transaction_Status]
           ,[Status_Code]
           ,[Status_Description]
           ,[Record_ID_header]
           ,[Version]
           ,[File_Encoding_Type]
           ,[Program_ID]
           ,[File_Creation_Date]
           ,[Agent_id]
           ,[Description]
           ,[File_Sequence_number]
           ,[File_Processed_Date])
           Values 
               (
           """
     
        for d in ds:
            
            nwD = d.split('|')
          
            t = "'"
            cnt = 0
            for z in nwD:
                if cnt == 0:
                    t = "'" + str(z) + "'"
                else:
                    t = t + ',' + "'" +   str(z) + "'"
                
                cnt = cnt + 1
            up = sql + t + ')'
            cursor.execute(up)
            cnxn.commit() 
    
    def getVerifyEFile(self, PTHProcess):
        ds = []
        f = open(PTHProcess + '\\' + 'E_processed.txt', 'r')
        
        for r in f:
            ds.append(r)
            
        return ds
           
    def getVerifyVFile(self, PTHProcess):
        ds = []
        f = open(PTHProcess + '\\' + 'V_processed.txt', 'r')
        
        for r in f:
            ds.append(r)
            
        return ds
        
        
        
        
        
        
        