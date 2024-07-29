v3.0

This is a major release so please test carefully.

* Removed: `old_state` of the object from database, but still the changes can be done against previous object.
* Added: `get_history(reverse=True)` to get all object changes, this returns a Queryset so it can be filtered 
* Added: `View Data Changes` in Django Model Admin to see the object changes
* Change: add urls under `tracker` namespace.