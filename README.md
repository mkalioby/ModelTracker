# Model Tracker

Track model object changes over time so that you know who done what.
 
## Installation

* Install the package
```sh
pip install django-model-tracker
```
* Add Application to your project's INSTALLED_APPs
```python
INSTALLED_APPS = (
     '....',
    'ModelTracker',
    )
```    
* Add the following line to your urls.py
```python
import ModelTracker
urlpatterns = patterns('',
...
url(r'^track/', include(ModelTracker.urls)),
...
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
   
**Old Code**

```python
   class Employee(models.Model):
     name=models.CharField(max_length=255)
     address=models.CharField(max_length=255)
     age=models.IntegerField()
 ``` 
  **New Code**
 
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
* Starting from version of 0.5, you can pass a event_name parameter to mark change as an event
 
     * New Code
 ```python
        emp=Employee()
        emp.save(request.user.username,event_name="Created the user")
 ```

Using The Middleware
====================
You can add `ModelTracker.middleware.ModelTrackerMiddleware` to your Middleware classes to get the username automatically from the request.

```python
INSTALLED_APPS = (
     '....',
    'ModelTracker.middleware.ModelTrackerMiddleware',
    )
```   

**Note:** If you pass username as `None` then the change won't be saved.

