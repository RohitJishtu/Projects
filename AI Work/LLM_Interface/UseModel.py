import time
from SnowflakeConnect import *
from langChainLLM import *
import time
import pandas as pd
import nltk
from datetime import datetime
nltk.download('stopwords')
from nltk.corpus import stopwords

import string

class ModelClass:    
    # Snowflake Access 
    # Chat GPT 
    def CallModel(self,Prompt,Model='GPT',ConnLab=None,Content=None):
        if Content==None:
            Content=Prompt
            if Model=='GPT': 
                api_url_gpt= 'https://URL'
                api_key_gpt = 'KEY'
                print('GPT API')
                LLMObject = CustomLLM(max_tokens=4096)
                beg=time.time()
                result = LLMObject._call(Model,url=api_url_gpt, key=api_key_gpt, prompt=Prompt)
                end = time.time()
                timetaken=end-beg
              
                return result ,timetaken
            
            # elif Model=='Mistral':
                
            #     print('Mistral API')
            #     api_url=URL
            #     api_key =KEY
              
            #     LLMObject2 = CustomLLM(max_tokens=4096)

            #     beg=time.time()
            #     # result = 'Mistral Model WIP'
            #     result = LLMObject2._call(Model,url=api_url, key=api_key, prompt=Prompt)
            #     result = result[0]["0"]
            #     end = time.time()
            #     timetaken=end-beg
            #     return result  ,timetaken
        
            elif Model=='Mistral':
                
                print('Snowflake API Mistral')
                if '1-5' in Prompt:
                    SQL="""SELECT SNOWFLAKE.CORTEX.SENTIMENT('"""+Content+"""')/2*100 as result ;"""
                else:
                    SQL="""SELECT SNOWFLAKE.CORTEX.COMPLETE('mistral-7b','"""+Prompt+"""') result ;"""
                beg=time.time()
                result=pd.read_sql(SQL,ConnLab)
                end = time.time()
                res=''
                for i in result['RESULT']:
                    res=res+str(i)
                    timetaken=end-beg
                return res,timetaken

            elif Model=='Llama':  
                print('Snowflake API LLAMA')
                if '1-5' in Prompt:
                    SQL="""SELECT SNOWFLAKE.CORTEX.SENTIMENT('"""+Content+"""')/2*100 as result ;"""
                else:
                    SQL="""SELECT SNOWFLAKE.CORTEX.COMPLETE('llama2-70b-chat','"""+Prompt+"""') result ;"""
                beg=time.time()
                result=pd.read_sql(SQL,ConnLab)
                end = time.time()
                res=''
                for i in result['RESULT']:
                    res=res+str(i)
                timetaken=end-beg
                return res,timetaken
        else:
            print('No Content')

    def Clean_Context_Prompts(self,content,Question,CleaningReqd='Yes',ApplyRules='Yes'):
   

        if CleaningReqd=='Yes':
            content=content.translate(str.maketrans('', '', string.punctuation))
            stop_words = set(stopwords.words('english'))
            content =' '.join([word for word in content.split() if word not in stop_words])
            content=' '.join(content.split())
        
        # Prompt 1 
        if content:
            Rules=''
            if ApplyRules:
                context=content
                Rules=""" 1.you are a helpful assistant 
                        2.Please avoid unncessary information 
                        3.The results should be limited to a few words"""
        
    
            return context + '.' + Question +'.' + Rules
        else :
            return Question
        
    def WritetoDB(self,Question, model, Context, summary, timetaken, full_result):
        ConnDev = Dev_snowflake_connection()
        cursor = ConnDev.cursor()
        data = (Question,model,Context,summary,timetaken,full_result,datetime.utcnow())

        statement = f"INSERT INTO EDW_LS.DATASCIENCE_GENAI.LLM_COMPARE(Question,model,Context,summary,timetaken,full_result,LoadTime) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        print(statement)
        cursor.execute(statement, data)