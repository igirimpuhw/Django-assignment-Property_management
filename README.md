# Django-assignment-Property_management

UNIVERSITY OF RWANDA

COLLEGE OF SCIENCE AND TECHNOLOGY

YEAR 3 INFORMATION TECHNOLOGY

1. Names: IGIRIMPUHWE Jonathan 222004512


2. Names: UMUHOZA Amandine Divine 222005360



This is our property_management which has property_app(models,view,admin,setting)
Access the admin interface

open your browser and click to link which specify by server.
manage properties,units,tenants, and leases:
use the admin interfaces tp add, edit, or delete entries as needed.
MODELS
the system includes the following models

.PROPERTY

  .name:Name of the property
  .address:Physical address
  .property_type:Type of property(e.g. Apartment,House,Commercial)
  .description:Additional details.
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


