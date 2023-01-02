import app

url ='http://www.mubas.ac.mw/programmes?page='


for i in range(1, 7):
    link = f"{url}{i}"
    soup = app.get_link(link)
    divs = app.get_souped_courses(soup)
    faculty, course, level, award, duration = get_divs(divs)
    
    df = create_repo(faculty, course, level, award, duration)