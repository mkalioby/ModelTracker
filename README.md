# Model Tracker

Track model object changes over time so that you know who done what.
 

## Installation

* Install the package
```sh
pip install DjangoModelTracker
```
* Add Application to your project's INSTALLED_APPs
```python
INSTALLED_APPS = (
     '....',
    'ModelTracker',
    )
```    
* Run Migrations
```sh
   python manage.py migrate ModelTracker 
```

* Add the following line to your models.py file
```python
from ModelTracker import Tracker
```
*  Convert each Model you want to track to inhert from `Tracker.ModelTracker` instead of `models.Model`
     * Old Code
```python
            class Employee(models.Model):
                name=models.CharField(max_length=255)
                address=models.CharField(max_length=255)
                age=models.IntegerField()
 ``` 
     * New Code
```python
    class Employee(Tracker.ModelTracker):
      name=models.CharField(max_length=255)
      address=models.CharField(max_length=255)
      age=models.IntegerField()
```
* For each save() call, add the user the username
    * Old Code
 ```python
    emp=Employee()
    emp.save()
 ``` 
 
     * New Code
     ```python
        emp=Employee()
        emp.save(request.user.username)
     ```
