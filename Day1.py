import streamlit as st

a = st.sidebar.selectbox("Choose an option",["Home","Student","Leaderboard"])
list1 = []

c = 90 + 85 + 94
d = 98 + 97 + 95
e = 85 + 90 + 72
f = 80 + 66 + 87
g = 96 + 90 + 92

if a == "Home":
    st.title("Home page")
    st.write("You can check the result in this app")
elif a == "Student":
    st.title("Student")
    b = st.sidebar.selectbox("Select student",["Arjun","Aarav","Aarya","Ananya","Aadi"])
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    if b == "Arjun":
        c1 = 90
        c2 = 85
        c3 = 94
        st.write("Maths :",c1)
        st.write("Science :",c2)
        st.write("English :",c3)
        c = (c1+c2+c3)
        st.write("Total =",c)
    elif b == "Aarav":
        d1 = 98
        d2 = 97
        d3 = 95
        st.write("Maths :",d1)
        st.write("Science :",d2)
        st.write("English :",d3)
        d = (d1+d2+d3)
        st.write("Total =",d)        
    elif b == "Aarya":
        e1 = 85
        e2 = 90
        e3 = 72
        st.write("Maths :",e1)
        st.write("Science :",e2)
        st.write("English :",e3)
        e = (e1+e2+e3)
        st.write("Total =",e)
    elif b == "Ananya":
        f1 = 80
        f2 = 66
        f3 = 87
        st.write("Maths :",f1)
        st.write("Science :",f2)
        st.write("English :",f3)
        f = (f1+f2+f3)
        st.write("Total =",f)
    elif b == "Aadi":
        g1 = 96
        g2 = 90
        g3 = 92
        st.write("Maths :",g1)
        st.write("Science :",g2)
        st.write("English :",g3)
        g = (g1+g2+g3)
        st.write("Total =",g)
elif a == "Leaderboard":
    students = [
        ("Arjun", c),
        ("Aarav", d),
        ("Aarya", e),
        ("Ananya", f),
        ("Aadi", g)
    ]

    students.sort(key=lambda x: x[1], reverse=True)

    st.write(students[0][0],"-->", students[0][1])
    st.write(students[1][0],"-->", students[1][1])
    st.write(students[2][0],"-->", students[2][1])
    st.write(students[3][0],"-->", students[3][1])
    st.write(students[4][0],"-->", students[4][1])