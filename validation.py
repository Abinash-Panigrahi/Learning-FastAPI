# problem example 

# def insert_patient_data(name ,age):
#     print(name)
#     print(age)
#     print('Inserted in to database')
# insert_patient_data('Abinash','tewnty five')

# solution 1 type hinting

# def insert_patient_data(name : str,age : int):
#     print(name)
#     print(age)
#     print('Inserted in to database')
# insert_patient_data('Abinash',25)   
# insert_patient_data('Abinash','25')  #in this solution it can take string like before ,it just show a hint to write this datatype not showing the error.

# solution 2 ,if-else condition 

# def insert_patient_data(name : str,age : int):
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)                               #this is solution but not sclable ,if more than one function we create then we have to write everytime .thats why it is not good for production level.  
#         print('Inserted in to database')
#     else:
#         raise TypeError('Incorrect data types')     
# insert_patient_data('Abinash','25')   

# another problem is data validation 

# def insert_patient_data(name : str,age : int):
#     if type(name) == str and type(age) == int:
#         if age <= 0:
#             raise TypeError('Age cant be negetive')
#         else:                                           #same we have to write many things manually , this is a big problem for production level.
#             print(name)
#             print(age)                                 
#             print('Inserted in to database')
#     else:
#         raise TypeError('Incorrect data types')     
# insert_patient_data('Abinash',0)  



# _________________
# Pydantic solution
# -----------------

# from pydantic import BaseModel

# class Patient(BaseModel):
#     name : str
#     age : int

# def insert_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.age)
    
#     print('Inserted in to database')

# def update_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.age)
#     print('Updated')

# patient_info = {'name':'Abinash','age':25}
# patient1 = Patient(**patient_info)
# insert_patient_data(patient1)


# Bigger pydantic model more complex testing
# Type validation 
# _____________________________________________


# from pydantic import BaseModel
# from typing import List,Dict

# class Patient(BaseModel):
#     name : str
#     age : int
#     weight : float
#     married : bool
#     allergies : List[str]          #|this strcutur is used for double 
#     contact : Dict[str,str]        #|varification

# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.age)
#     print(pt.weight)
#     print(pt.married)
#     print(pt.allergies)
#     print(pt.contact)

# patient_info = {'name':'Abinash','age':25,'weight':75.3,'married':False,'allergies':['Pollen','Dust'],'contact':{'mail':'ap@gmail.com','phone':'5646757868'}}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)


# using optional 
# from pydantic import BaseModel
# from typing import List,Dict,Optional

# class Patient(BaseModel):
#     name : str
#     age : int
#     weight : float
#     married : bool = False                    #we could set it as a False cause False is also a boolean
#     allergies : Optional[List[str]] = None       #if anybody doesn't have any value then they could skip it 
#     contact : Dict[str,str]        

# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.age)
#     print(pt.weight)
#     print(pt.married)
#     print(pt.allergies)
#     print(pt.contact)

# patient_info = {'name':'Abinash','age':25,'weight':75.3,}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)


# Data validation  
# __________________

# from pydantic import BaseModel,EmailStr,AnyUrl,Field
# from typing import List,Dict,Optional

# class Patient(BaseModel):
#     name : str = Field(max_length = 10)
#     email : EmailStr                #|For mail validation 
#     linkedin_url : AnyUrl           #|For url validation
#     age : int = Field(gt = 0,lt = 120)     #|Custom validation 
#     weight : float = Field(gt = 0)         #|      !!         ,also this could handle if anybody give an number in a string ,ex: '75.3' this is called Type coercion
#     married : bool = False                    
#     allergies : Optional[List[str]] = None  #also we can add field in this list ,example :{ Field(max_length = 5) }.means no body could add above 5 allergies.
#     contact : Dict[str,str]        

# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.email)
#     print(pt.linkedin_url)
#     print(pt.age) 
#     print(pt.weight)
#     print(pt.married)
#     print(pt.allergies)
#     print(pt.contact)

# patient_info = {'name':'Abinash','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1234','age':25,'weight':75.3,'married':True,'allergies':['Pollen','Dust'],'contact':{'phone':'5646757868','email':'abc@gmail.com'}}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)


# How to add metadeta (description) using Annotated
# ___________________________________

# from pydantic import BaseModel,EmailStr,AnyUrl,Field
# from typing import List,Dict,Optional,Annotated

# class Patient(BaseModel):
#     name : Annotated[str,Field(max_length = 10,title='Name of the patient',description='Give the name of the patient less than 10words',examples=['Siddharth','Subha'])]           #|Adding title,desciption and some example of this field
#     email : EmailStr                  
#     linkedin_url : AnyUrl             
#     age : int = Field(gt = 0,lt = 120)
#     weight : Annotated[float, Field(gt = 0,strict=True)]          #|Type coercion may be lead any problem in future ,so to handle Type coercion i use strict parameter.(also we could use the strict parameter without using Annotated)
#     married : Annotated[bool,Field(default=None,description='Is the patient married or not')]                #|we could set default value for this using 'Field'     
#     allergies : Annotated[Optional[List[str]],Field(default = None,max_length=5)]
#     contact : Dict[str,str]        

# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.email)
#     print(pt.linkedin_url)
#     print(pt.age) 
#     print(pt.weight)
#     print(pt.married)
#     print(pt.allergies)
#     print(pt.contact)

# patient_info = {'name':'Abinash','email':'abc@gmail.com','linkedin_url':'http://linkedin.com/1234','age':25,'weight':75.3,'married':True,'allergies':['Pollen','Dust'],'contact':{'phone':'5646757868','email':'abc@gmail.com'}}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)  



# Field validator 
# __________________


# from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
# from typing import List,Dict,Optional,Annotated

# class Patient(BaseModel):
#     name : str
#     email : EmailStr
#     age : int
#     weight : float
#     married : bool
#     allergies : List[str]       
#     contact : Dict[str,str]    


#     @field_validator('email')
#     @classmethod
#     def email_validator(cls,value):
#         valid_domains = ['hdfc.com','icici.com']
#         #ex : abc@gmail.com (extract after '@')
#         domain_name = value.split('@')[-1]
#         if domain_name not in valid_domains:
#             raise ValueError('Not a vlaid Domain')
#         return value

#     @field_validator('name')
#     @classmethod
#     def transform_name(cls,value):
#         return value.upper()

#     @field_validator('age',mode='after')        #we can use this field_validator in both way using ( mode ), like before type coercion and after type coercion as well. and if nothing is given then the default vlaue is (after), and also it validates only one sinlge field data validation
#     @classmethod
#     def validate_age(cls,value):
#         if 0 < value < 100:
#             return value
#         else:
#             raise ValueError('Age is not between 0 ot 100')


# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.email)
#     print(pt.age) 
#     print(pt.weight)
#     print(pt.married)
#     print(pt.allergies)
#     print(pt.contact)

# patient_info = {'name':'Abinash','email':'abc@hdfc.com','age':'twenty-five','weight':75.3,'married':True,'allergies':['Pollen','Dust'],'contact':{'phone':'5646757868','email':'abc@gmail.com'}}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)  



# Data validation in more than one field (model_validator)

# from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
# from typing import List,Dict,Optional,Annotated

# class Patient(BaseModel):
#     name : str
#     email : EmailStr
#     age : int
#     weight : float
#     married : bool
#     allergies : List[str]       
#     contact : Dict[str,str]    

#     @model_validator(mode='after')
#     def validate_emergency(cls,model):                          #|This model is apply on the whole pydantic model ,like from this model we could access all of the field 
#         if model.age > 60 and 'emergency' not in model.contact:
#             raise ValueError('Patient older than 60 have must emergency contact')
#         return model

# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.email)
#     print(pt.age) 
#     print(pt.weight)
#     print(pt.married)
#     print(pt.allergies)
#     print(pt.contact)

# patient_info = {'name':'Abinash','email':'abc@hdfc.com','age':'61','weight':75.3,'married':True,'allergies':['Pollen','Dust'],'contact':{'emergency':'5646757868','email':'abc@gmail.com'}}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)  



# Computed Fields (using another fields to calculate and then create one computed field)
# _____________________BMI calculation test_____________________________


# from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator,computed_field
# from typing import List,Dict,Optional,Annotated

# class Patient(BaseModel):
#     name : str
#     email : EmailStr
#     age : int
#     weight : float #kgs
#     height : float #mtr
#     married : bool
#     allergies : List[str]       
#     contact : Dict[str,str]    


#     @computed_field
#     @property
#     def bmi(self) -> float:
#         bmi = round(self.weight / (self.height**2),2)
#         return bmi

    

# def insert_complex_patient_data(pt : Patient):
#     print(pt.name)
#     print(pt.email)
#     print(pt.age) 
#     print(pt.weight)
#     print('BMI' ,pt.bmi)

# patient_info = {'name':'Abinash','email':'abc@hdfc.com','age':'61','weight':75.2,'height':1.72,'married':True,'allergies':['Pollen','Dust'],'contact':{'emergency':'5646757868','email':'abc@gmail.com'}}

# patient1 = Patient(**patient_info)

# insert_complex_patient_data(patient1)  




# Nested models (In pydantic if any one model use in another model as a field it is called nested models)



# from pydantic import BaseModel

# class Address(BaseModel):
#     city : str
#     state : str
#     pin : str

# class Patient(BaseModel):

#     name  : str
#     gender : str
#     age : int
#     address : Address

# address_dict = {'city':'Bhubaneswar','state':'Odisha','pin':'751018'}

# address1 = Address(**address_dict)

# patient_dict = {'name':'Abinash','gender':'male','age':'25','address':address1}

# patient1 = Patient(**patient_dict)

# print(patient1)

# print('name:',patient1.name)
# print('name:',patient1.gender)
# print('name:',patient1.address.pin)
# print('name:',patient1.address.city)



# Topic : How to export the existing pydantic model in to a python dictionary or json (using the built-in method)

from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str

class Patient(BaseModel):

    name  : str
    gender : str
    age : int
    address : Address

address_dict = {'city':'Bhubaneswar','state':'Odisha','pin':'751018'}

address1 = Address(**address_dict)

patient_dict = {'name':'Abinash','gender':'male','age':'25','address':address1}

patient1 = Patient(**patient_dict)

#|Convert to python dictionary 

# temp = patient1.model_dump()           

# print(temp)
# print(type(temp))

#|Convert to json

# temp = patient1.model_dump_json()          

# print(temp)
# print(type(temp))


# |We can choose what to show by using (include function)

# temp = patient1.model_dump(include=['name','gender'])          

# print(temp)
# print(type(temp))

# |We can exclude any field as well by using (exclude function)

# temp = patient1.model_dump(exclude=['name','gender']) 
# temp = patient1.model_dump(exclude={'address':['state']})          
# temp = patient1.model_dump(exclude={'name': True, 'gender': True, 'address': {'state': True}})

# print(temp)
# print(type(temp))

# |If in Patient model i set the default value of gender is to "Male" then if we do not insert any value in creating the Patient object then it will show the default vlaue but here we could handle that as well by using (Exclude_unset = True), by using this if anybody do not set the value when creating the the nee object then when you exprt then it will not shown that field. 

temp = patient1.model_dump(exclude_unset=True)

print(temp)
print(type(temp))