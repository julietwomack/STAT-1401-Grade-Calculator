import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(layout="wide", page_title="Grade Calculator for STAT 1401")

st.header("Welcome!")
st.markdown("Hello and welcome to the STAT 1401 grade calculator for Ms. Womack's class. This calculator will help you estimate your current or final grade in STAT 1401.")
st.markdown("- __DISCLAIMER:__ By using this calculator, you agree that the results of this calculator are an __estimation__ of your grade and it is __not__ a guarentee of your final grade that will be posted on Owl Express at the end of the semester.")
st.markdown("- This calculator does account for (1) dropping your lowest quiz grade when all 9 quiz grades are entered and (2) replacing your lowest unit test grade with the final exam grade if your final exam grade is higher than your lowest unit test grade.")
st.markdown("- This calculator will only provide an (estimated) overall course average once you had entered in at least one test grade")
st.markdown("If you have any questions about the course or your final grade, please contact Ms. Womack at [jwomac20@students.kennesaw.edu](mailto:jwomac20@students.kennesaw.edu)")

# Homework Grade
st.markdown("____")
st.header("Homework")

hwk_avg = st.container()
with hwk_avg:
    hw = st.number_input("Enter your homework average:", min_value=0.0, max_value=100.0)


# Quiz Grade
st.markdown("____")
st.header("Quizzes")
quiz_num = st.number_input("How many quizzes have been given this semester?", min_value = 0, max_value = 9, step = 1)

st.subheader("Enter your quiz grades below:")
if quiz_num == 0:
    st.error("You need to take a quiz to enter in values")

if quiz_num == 1:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    quiz_list = [q1]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 2:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    quiz_list = [q1, q2]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 3:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    quiz_list = [q1, q2, q3]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 4:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    q4 = st.number_input("Quiz 4:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    quiz_list = [q1, q2, q3, q4]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 5:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    q4 = st.number_input("Quiz 4:", min_value=0.0, max_value=100.0)
    q5 = st.number_input("Quiz 5:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    quiz_list = [q1, q2, q3, q4, q5]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 6:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    q4 = st.number_input("Quiz 4:", min_value=0.0, max_value=100.0)
    q5 = st.number_input("Quiz 5:", min_value=0.0, max_value=100.0)
    q6 = st.number_input("Quiz 6:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    quiz_list = [q1, q2, q3, q4, q5, q6]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 7:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    q4 = st.number_input("Quiz 4:", min_value=0.0, max_value=100.0)
    q5 = st.number_input("Quiz 5:", min_value=0.0, max_value=100.0)
    q6 = st.number_input("Quiz 6:", min_value=0.0, max_value=100.0)
    q7 = st.number_input("Quiz 7:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    n = 7
    quiz_list = [q1, q2, q3, q4, q5, q6, q7]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 8:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    q4 = st.number_input("Quiz 4:", min_value=0.0, max_value=100.0)
    q5 = st.number_input("Quiz 5:", min_value=0.0, max_value=100.0)
    q6 = st.number_input("Quiz 6:", min_value=0.0, max_value=100.0)
    q7 = st.number_input("Quiz 7:", min_value=0.0, max_value=100.0)
    q8 = st.number_input("Quiz 8:", min_value=0.0, max_value=100.0)
    # Calculate the quiz average
    n = 8
    quiz_list = [q1, q2, q3, q4, q5, q6, q7, q8]
    quiz_avg = sum(quiz_list)/len(quiz_list)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

if quiz_num == 9:
    q1 = st.number_input("Quiz 1:", min_value=0.0, max_value=100.0)
    q2 = st.number_input("Quiz 2:", min_value=0.0, max_value=100.0)
    q3 = st.number_input("Quiz 3:", min_value=0.0, max_value=100.0)
    q4 = st.number_input("Quiz 4:", min_value=0.0, max_value=100.0)
    q5 = st.number_input("Quiz 5:", min_value=0.0, max_value=100.0)
    q6 = st.number_input("Quiz 6:", min_value=0.0, max_value=100.0)
    q7 = st.number_input("Quiz 7:", min_value=0.0, max_value=100.0)
    q8 = st.number_input("Quiz 8:", min_value=0.0, max_value=100.0)
    q9 = st.number_input("Quiz 9:", min_value=0.0, max_value=100.0)

    # Calculate the quiz average with lowest quiz grade dropped
    n = 8
    quiz_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9]
    quiz_list.sort(reverse = True)
    top_8_quizzes = quiz_list[:n]
    quiz_avg = sum(top_8_quizzes)/len(top_8_quizzes)
    st.subheader("Your quiz average is: {}".format(round(quiz_avg,2)))

# Test Grade
st.markdown("____")
st.header("Tests")
test_num = st.number_input("How many tests have been given this semester? If you are exempting the final enter 3, otherwise enter 4.", min_value = 0, max_value = 4, step = 1)
st.subheader("Enter your test grades below:")

if test_num == 0:
    st.error("You need to take a test to enter in values")

if test_num == 1:
    t1 = st.number_input("Unit 1 Test:", min_value=0.0, max_value=100.0)
    # Calculate the test average
    n = 1
    test_list = [t1]
    test_avg = sum(test_list)/len(test_list)
    st.subheader("Your test average is: {}".format(round(test_avg,2)))
    st.header("Your current course average is: {}".format(round((((hw*0.10)+(quiz_avg*0.10)+(t1*0.20))/40)*100),2))

if test_num == 2:
    t1 = st.number_input("Unit 1 Test:", min_value=0.0, max_value=100.0)
    t2 = st.number_input("Unit 2 Test:", min_value=0.0, max_value=100.0)
    # Calculate the test average
    n = 2
    test_list = [t1, t2]
    test_avg = sum(test_list)/len(test_list)
    st.subheader("Your test average is: {}".format(round(test_avg,2)))
    weighted_grade = (hw*0.10)+(quiz_avg*0.10)+(test_avg*0.40)
    final_avg = (weighted_grade/60)*100
    st.header("Your current course average is: {}".format(round(final_avg,2)))

if test_num == 3:
    t1 = st.number_input("Unit 1 Test:", min_value=0.0, max_value=105.0)
    t2 = st.number_input("Unit 2 Test:", min_value=0.0, max_value=105.0)
    t3 = st.number_input("Unit 3 Test:", min_value=0.0, max_value=105.0)
    # Calculate the test average
    n = 3
    test_list = [t1, t2, t3]
    test_avg = sum(test_list)/len(test_list)
    st.subheader("Your test average is: {}".format(round(test_avg,2)))
    final_avg = (((hw*0.10)+(quiz_avg*.10)+(test_avg*0.60))/80)*100
    if final_avg >= 90.00:
        st.header("Your current (estimated) course average is: {}, A".format(round(final_avg,2)))
    elif 80.00 <= final_avg <= 89.00:
        st.header("Your current (estimated) course average is: {}, B".format(round(final_avg,2)))
    elif 70.00 <= final_avg <= 79.00:
        st.header("Your current (estimated) course average is: {}, C".format(round(final_avg,2)))
    elif 60.00 <= final_avg <= 69.00:
        st.header("Your current (estimated) course average is: {}, D".format(round(final_avg,2)))
    else:
        st.header("Your current (estimated) course average is: {}, F".format(round(final_avg,2)))

if (test_num == 4):
    t1 = st.number_input("Unit 1 Test:", min_value=0.0, max_value=105.0)
    t2 = st.number_input("Unit 2 Test:", min_value=0.0, max_value=105.0)
    t3 = st.number_input("Unit 3 Test:", min_value=0.0, max_value=105.0)
    final_test = st.number_input("Final Exam:", min_value=0.0, max_value=100.0)
    # Calculate the test average with the lowest test grade dropped if the final is greater than one of the unit Tests
    unit_test = [t1,t2,t3]
    min_unit_test = min(unit_test)
    final = [final_test]

    if min_unit_test > final_test:
        all_tests = unit_test + final
        st.markdown("Your Final Exam __will not__ replace your lowest unit test grade")
        st.subheader("Your test average is: {}".format(sum(all_tests)/len(all_tests)))
        test_avg = sum(all_tests)/len(all_tests)
        st.markdown("____")
        final_avg = (hw*0.10)+(quiz_avg*.10)+(test_avg*0.80)
        if final_avg >= 90.00:
            st.header("Your current (estimated) course average is: {}, A".format(round(final_avg,2)))
        elif 80.00 <= final_avg <= 89.00:
            st.header("Your current (estimated) course average is: {}, B".format(round(final_avg,2)))
        elif 70.00 <= final_avg <= 79.00:
            st.header("Your current (estimated) course average is: {}, C".format(round(final_avg,2)))
        elif 60.00 <= final_avg <= 69.00:
            st.header("Your current (estimated) course average is: {}, D".format(round(final_avg,2)))
        else:
            st.header("Your current (estimated) course average is: {}, F".format(round(final_avg,2)))

    else:
        unit_test[unit_test.index(min(unit_test))] = final_test
        all_tests = unit_test + final
        st.write("Your Final Exam __will replace__ your lowest unit test grade")
        st.subheader("Your test average is: {}".format(sum(all_tests)/len(all_tests)))
        test_avg = sum(all_tests)/len(all_tests)
        st.markdown("____")
        final_avg = (hw*0.10)+(quiz_avg*.10)+(test_avg*0.80)
        if final_avg >= 90.00:
            st.header("Your current (estimated) course average is: {}, A".format(round(final_avg,2)))
        elif 80.00 <= final_avg <= 89.00:
            st.header("Your current (estimated) course average is: {}, B".format(round(final_avg,2)))
        elif 70.00 <= final_avg <= 79.00:
            st.header("Your current (estimated) course average is: {}, C".format(round(final_avg,2)))
        elif 60.00 <= final_avg <= 69.00:
            st.header("Your current (estimated) course average is: {}, D".format(round(final_avg,2)))
        else:
            st.header("Your current (estimated) course average is: {}, F".format(round(final_avg,2)))
