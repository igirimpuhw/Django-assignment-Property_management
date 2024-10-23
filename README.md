# Django-assignment-Property_management

UNIVERSITY OF RWANDA

COLLEGE OF SCIENCE AND TECHNOLOGY

YEAR 3 INFORMATION TECHNOLOGY

1. Names: IGIRIMPUHWE Jonathan 222004512


2. Names: UMUHOZA Amandine Divine 222005360


This is our property_management which has property_app(models,view,admin,setting)

. Firstly We have created Virtual Environment   

-install PIP DJANGO 

-running our initial migration

-creating super user with their credentials

-runing servers

-Access te admin interface 

..MODELS
the system includes the following models

.PROPERTY

  .name:Name of the property
  
  .address:Physical address
  
  .property_type:Type of property(e.g. Apartment,House,Commercial)
  
  .description:Additional details
  
  .number_of_units:Total units in the property
  
.UNIT

  .property:Foreignkey to property
  
  .unit_number:Unique identifier for the unit
  
  .bedrooms:Number of bedrooms
  
  .bathrooms:Number of bathrooms
  
  .rent:Monthly rent amount
  
  is_available:Availability status
  
  
.TENANT

  .name:Name of the tenant
  
  .email:Email address
  
  phone_number:Contact number
  
.LEASE

  .tentant:Foreignkey to tenant
  
  .unit:Foreignkey to unit
  
  .start_date:Lease start date
  
  .end_date:Lease end date
  
  .rent_amount:Amount of rent for the lease period

  
..ADMIN INTERFACE


  After running server and go to ADMIN INTERFACE


  You can login using credentials created in creation of super User 
  here admin is allowed to Add information in Properties, UNITS, TENANTS and Lease

  Admin is allowed to add ,delete and change all information

  

  


