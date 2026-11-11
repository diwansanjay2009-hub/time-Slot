# time-Slot
# Exercise: 4
# Create a Time Slot Timetable Using Django Templates

### Objective
Create a Django application to display a daily timetable with different time slots in an HTML table.

### Step-by-Step Instructions

1. Create a new Django project named `TimeTableProject`.

2. Create a Django app named `timetable`.

3. Register the `timetable` app in the `INSTALLED_APPS` section of the project settings.

4. Create a model named `TimeSlot` with the following fields:
   - Day
   - Start Time
   - End Time
   - Subject Name
   - Faculty Name

5. Perform the necessary database migrations.

6. Register the `TimeSlot` model in the Django Admin panel.

7. Insert at least 10 timetable records for different days and time slots using the Admin panel.

8. Create a view function to retrieve all timetable records from the database using Django ORM.

9. Configure the application URLs and connect them to the main project URLs.

10. Create the required template folder structure inside the app.

11. Create an HTML template named `timetable.html`.

12. Design an HTML table with the following columns:
    - Day
    - Time Slot
    - Subject
    - Faculty Name

13. Use Django template tags (`for` loop and variable expressions) to display the timetable records dynamically in the HTML table.

14. Add a suitable heading such as **Class Timetable**.

15. Run the Django development server and display the timetable in the browser.

### Expected Output

A webpage displaying the class timetable in a properly formatted HTML table with day-wise time slots, subject names and faculty details.

### Additional Tasks

1. Add a new field named `Classroom` to the TimeSlot model.
2. Update the HTML table to display the classroom details.
3. Display a message if no timetable records are available.
