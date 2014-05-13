import os
import pyodbc
import shutil

class CiticDeposit:
    
    def readFile(self, PTH, flName):
        f = open(PTH + '\\' + str(flName), 'r')
        
        dataset = []
        header = []
        for rw in f:
            newRw = rw.split('\t')
           
            if str(newRw[0]) == 'H':
                
                newRwPrint = '|'.join(newRw)
                header.append(newRwPrint)
            elif str(newRw[0]) != 'H' and str(newRw[0]) != 'T':
                newRwPrint  = '|'.join(newRw)
#                 print(len(newRw))
                dataset.append(newRwPrint)

        return dataset, header
    
    def combine(self, hd, ds):
        finalDS = []
        hdP = '|' + str(hd[0])
    
        for rw in ds:
            newRW = rw.split('|')
#             print(len(newRW))
            newRW[25] = str(newRW[25])[:-1]
            newRWP = '|'.join(newRW)
            newRWT = newRWP + hdP
            finalDS.append(newRWT)
    
        return finalDS
    
    def getFileList(self,PTH):
        
        ls = os.listdir(PTH)
        
        return ls
    
    def writeFile(self, PTHDEST, ds):
        
        f = open(PTHDEST + '\\' + 'D_processed.txt', 'a')
        
        for rw in ds:
            f.write(rw)
    
    def moveFilesUploaded(self, pthDest):
        
        l = os.listdir(pthDest)
        pthdesUploaded = 'C:\\IHG\\CITIC\\DEPOSIT\\Uploaded'
        
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
            self.uploadDepositD(fn)
            self.moveFilesUploaded(PTHDEST)
    def getDepositDFile(self, PTHProcess):
        ds = []
        f = open(PTHProcess + '\\' + 'D_processed.txt', 'r')
        
        for r in f:
            ds.append(r)
            
        return ds
        
      
    def uploadDepositD(self,  ds): 
        conn = """DRIVER={SQL Server Native Client 11.0};Server=CN-L-CNU2141TR3\IHG;DATABASE=IHG;Trusted_Connection=yes"""

        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()  
        
        sql = """
       INSERT INTO [dbo].[Deposit]
           ([Record_Id]
           ,[PCR_Member_#]
           ,[Alliance_Code]
           ,[First_Name]
           ,[Last_Name]
           ,[Partner_Transaction_Date]
           ,[Promotion_Identifier]
           ,[Total_PCR_Credits_Earned]
           ,[Description_Field]
           ,[Address_Type]
           ,[EN_Address_Line1]
           ,[EN_Address_Line2]
           ,[EN_Address_Line3]
           ,[EN_Address_Line4]
           ,[EN_Address_Line5]
           ,[EN_City]
           ,[EN_State/Province]
           ,[EN_Zip/Postal_Code]
           ,[Country_Code]
           ,[Account_Reference_Number]
           ,[Hotel_Code]
           ,[Tracking_Number]
           ,[Source_Agent]
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
    
            
        
if __name__ == '__main__':
    
    print('hello')
    PTH = 'C:\\IHG\\CITIC\\DEPOSIT\\Original'
    r = CiticDeposit()
    ds, h = r.readFile(PTH, 'CITIC_DEPOSIT_20140304103452.TXT.RSP')
    
    fn = r.combine(h,ds)
    
    for rw in fn:
        print(rw)
    