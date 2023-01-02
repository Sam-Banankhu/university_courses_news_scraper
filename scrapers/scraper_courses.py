# importing necessary libraries
import pandas as pd
import sys
 
# adding root folder to the system path
sys.path.insert(0, '/home/pandas/Desktop/scraper/')
import app


url ='http://www.mubas.ac.mw/programmes?page='


for i in range(1, 7):
    link = f"{url}{i}"
    soup = app.get_link(link)
    divs = app.get_souped_courses(soup)
    faculty, course, level, award, duration = app.get_course_divs(divs)
    
    df = app.create_repo(faculty, course, level, award, duration)
    # df.to_csv(os.path.join(output_dir, f"{}"))

df.to_csv('courses.csv', index=False)