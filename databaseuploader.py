
import pyodbc

class CapOneDB:
    
    
    def __init__(self, f):
        
        self.fileName = f
 
    def getConnection(self):
        conn = """DRIVER={SQL Server Native Client 11.0};Server=CN-L-CNU2141TR3\IHG;DATABASE=IHG;Trusted_Connection=yes"""
        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()  
        
        return cnxn, cursor
    
    def upload(self):
        activityFlag = self.fileName.find('Activity')
        enrollFlag = self.fileName.find('Enrolled')
        accFlag = self.fileName.find('ACC')
          
        if activityFlag != -1:
               
            self.uploadActivity()
            # go to the activity process
        if accFlag != -1:
#             print('im in acc')
            self.uploadACC()
            
        if enrollFlag != -1:
#             print('im in acc')
            self.uploadEnrolled()
            
    def uploadActivity(self):
        cnxn, cursor = self.getConnection()
        f = open(self.fileName, 'r')
        sql = """
        INSERT INTO [dbo].[caponeActivity_load]
           ([Record_Id]
           ,[Tacking_Number]
           ,[Account_Reference_Number]
           ,[PCR_Member_Number]
           ,[Source_Agent]
           ,[Description_Field]
           ,[Promotion_Identifier]
           ,[Alliance_Code]
           ,[Partner_Transaction_Date]
           ,[Total_PCR_Credits_Earned]
           ,[Status_Code]
           ,[Transaction_Status]
           ,[Status_Description]
           ,[Record_Id_Header]
           ,[Version]
           ,[Agent_id]
           ,[File_Creation_Date]
           ,[Program_Id]
           ,[Description]
           ,[File_Sequence_Number]
           ,[Column 20])
        """
        
        rcnt = 0
        for r in f:
           
            if rcnt != 0:
                valz = self._getColumns(r)
                fin = sql + ' ' + valz
                
                try:
                    cursor.execute(fin)
                    cnxn.commit()
                except:
                    continue
            rcnt = rcnt + 1
    
    def uploadACC(self):  
        
        cnxn, cursor = self.getConnection()
#         print(self.fileName)
        f = open(self.fileName, 'r')
#         for r in f:
#             print(r)
        sql = """
            INSERT INTO [dbo].[caponeACC_load]
           ([Record_Id]
           ,[Account_Reference_Number]
           ,[PCR_Member_Id]
           ,[Enrolling_Source_Code]
           ,[Card_Type]
           ,[Last_Name]
           ,[First_Name]
           ,[Language_Spoken]
           ,[Status_Code]
           ,[Status_Description]
           ,[Transaction_Status]
           ,[Header_Record_Id]
           ,[Version]
           ,[Agent_id]
           ,[File_Creation_Date]
           ,[Program_Id]
           ,[Description]
           ,[File_Sequence_Number]
           ,[Column 18])
        
                """
        rcnt = 0
        for r in f:
            
            valz = self._getColumns(r)
            fin = sql + ' ' + valz
#             print(fin)
            try:
                cursor.execute(fin)
                cnxn.commit()
            except:
                continue    
                
            rcnt = rcnt + 1
   
    def uploadEnrolled(self):  
        
        cnxn, cursor = self.getConnection()
#         print(self.fileName)
        f = open(self.fileName, 'r')
#         for r in f:
#             print(r)
        sql = """
             INSERT INTO [dbo].[caponeEnrolled_load]
           ([Record_Id]
           ,[Account_Reference_Number]
           ,[PCR_Member_Id]
           ,[Card_Type]
           ,[First_Name]
           ,[Middle_Name]
           ,[Last_Name]
           ,[Address_Type]
           ,[EN_Address_Line1]
           ,[EN_Address_Line2]
           ,[EN_City]
           ,[Country_Code]
           ,[EN_State Province]
           ,[EN_ZIP Postal_Code]
           ,[Language_Spoken]
           ,[Phone_Number_1]
           ,[Phone_Number_1_Usage_Type]
           ,[Phone_Number_2]
           ,[Phone_Number_2_Usage_Type]
           ,[Status_Code]
           ,[Transaction_Status]
           ,[Status_Description]
           ,[Record_Id_Header]
           ,[Version]
           ,[Agent_id]
           ,[File_Creation_Date]
           ,[Program_Id]
           ,[Description]
           ,[File_Sequence_Number]
           ,[Column 29])
                    """
        rcnt = 0
        for r in f:
            
            valz = self._getColumns(r)
            fin = sql + ' ' + valz
#             print(fin)
            try:
                cursor.execute(fin)
                cnxn.commit()
            except:
                continue    
                
            rcnt = rcnt + 1
     
    def _getColumns(self,rc):
        
        newR = rc.split('|')
        sql = 'values ('
        valz = ''
        le = len(newR)
        x = 0
        for r in newR:
            x = x + 1
            if x != le:
            
                valz = valz + """ '{0}', """.format(str(r))
            else:
                valz = valz + """ '{0}' """.format(str(r))
            
            
        sql = sql + valz + ")"
        
        return sql
   
    def go(self):
        
        
        self.upload()
    



class BarclaysDB:
    
        
    def __init__(self, f):
        
        self.fileName = f
 
    def getConnection(self):
        conn = """DRIVER={SQL Server Native Client 11.0};Server=CN-L-CNU2141TR3\IHG;DATABASE=IHG;Trusted_Connection=yes"""
        cnxn = pyodbc.connect(conn)
        cursor = cnxn.cursor()  
        
        return cnxn, cursor
 
    def upload(self):

        barclaysFlag = self.fileName.find('Barclays')
        if barclaysFlag != -1:
               
            self.uploadBarclays()
    
    def uploadBarclays(self):
        cnxn, cursor = self.getConnection()
        f = open(self.fileName, 'r')
        sql = """
  INSERT INTO [dbo].[barclays_load]
           ([Record_id]
      ,[PCR_Member_#]
      ,[Alliance_Code]
      ,[Partner_Transaction_Date]
      ,[Promotion_Identifier]
      ,[Total_PCR_Credits_Earned]
      ,[Source_Agent]
      ,[Transaction_Status]
      ,[Status_Code]
      ,[Status_Description]
      ,[Header_Record_Id]
      ,[Header_File_Creation_Date]
      ,[Header_Description]
      ,[Header_ProgramId]
      ,[Header_Agent_Id]
      ,[Header_File_Sequence_number]
      ,[Column 16])
        """
        
        rcnt = 0
        for r in f:
           
            if rcnt != 0:
                valz = self._getColumns(r)
                fin = sql + ' ' + valz
#                 print(fin)
                try:
                    cursor.execute(fin)
                    cnxn.commit()
                except:
                    continue
            rcnt = rcnt + 1

    def _getColumns(self,rc):
        
        newR = rc.split('|')
        sql = 'values ('
        valz = ''
        le = len(newR)
        x = 0
        for r in newR:
            x = x + 1
            if x != le:
            
                valz = valz + """ '{0}', """.format(str(r))
            else:
                valz = valz + """ '{0}' """.format(str(r))
            
            
        sql = sql + valz + ")"
        
        return sql
    
    def go(self):
        
        
        self.upload()
    