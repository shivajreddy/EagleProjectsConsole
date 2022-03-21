# ⭕️ Eagle Projects Console 


### **Goal ✅**

**Data visualization** and Data management for 'Eagle of VA'. That have 100’s of excel files (rows and tables) of data, relevant to the day-to-day operations of the company. Goal is to develope a Dashboard web-application.

> I intend to start this application addressing the General contractors in the home-building sector, who have multiple projects running simultaneously. (But this is not limited to GC’s)
> 
- This application stores the data in a relational database, and displays that data visually through graphs, plots, tables e.t.c,.
- CRUD functionality for user’s with editor roles.

![Screen Shot 2022-03-13 at 1.55.18 PM.png](Capstone%20-%203c7ef/Screen_Shot_2022-03-13_at_1.55.18_PM.png)

### **Who is it for ⁉️**

Mainly oriented for a specific company/organization. And the client can decide if the Content Dashboard is open to public, and/or controlled display of information to public.

### **Data 📊**

This application mainly focuses on data in the form of rows and columns, containing almost all data types.

### Application outline 📝

- Schema
    
    > Since it focused for addressing the mutliple projects, schema looks similar to the tabular representation of project’s details.
    > 
    
    ![Screen Shot 2022-03-13 at 1.42.39 PM.png](Capstone%20-%203c7ef/Screen_Shot_2022-03-13_at_1.42.39_PM.png)
    
    Starting of with the main table data, that has information for a specific project. Some columns will be referring to other tables.
    
- Possible Issues
    
    Tables: UI and displaying big data sets, in the form of tables.
    
    Graph plots: Performance, and UX. External library(pandas) performance dependant.
    
- Sensitive Information
    
    Only people with the organization’s email can create account, and will be assigned viewer roles.
    
    Users with editor roles, only can modify the data.
    
    CSRF attacks and URL navigation to modify data.
    
    User’s passwords should be hashed and stored securely.
    
- Functionality & Goals
    1. User’s able to create accounts, change password for their accounts.
    2. User roles, to control who can modify the data.
    3. (future functionality) Grouping users into Teams, and cross team communication.
    4. Notifications. Based on which group the user belongs to, emails will be sent to that team regarding a project, if that project is behind a deadline.
- UserFlow
    
    Viewer Role user → User securely log’s in (registers for first time) → Can view the dashboard → interact with interactive data charts & tables.
    
    Editor Role user → Does everything that viewer can do → ability to modify the data.
    

## Stack ⚙️

### Database
- PSQL
- MongoDB

### Back-end
- Flask with Jinja
- Pandas
- Flask SQLAlchemy
- WTForms
- Pymongo
- Bcrypt

### Front-end
- Vanilla JS
- Bootstrap5
- Tailwind

### API’s & Data
- Plotly
- Real organization data + (Mockup for public repo)

## TODO
- Build REST API for seed data.
