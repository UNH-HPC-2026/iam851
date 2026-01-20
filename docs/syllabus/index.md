# Syllabus: Introduction to High-Performance Computing

- **Course:** IAM751/851
- **Website:** The class notes etc. will go on the
  [Course Wiki Page](https://github.com/unh-hpc-2026/iam851/wiki)

```{todo}
Fix link.
```

- **Instructor:** Kai Germaschewski,
  [kai.germaschewski@unh.edu](mailto:kai.germaschewski@unh.edu), Morse 245E
- **Office Hours:** Mon 2-3pm (Morse 245E)
- **Slack / Discord URL** TBD

```{todo}
Poll class to figure out what tool to use and set it up.
```

- **Need help?**
  - Ask on Slack / Discord TBD

```{todo}
add links
```

  - You could also checkout github's
    [discussions](https://github.com/unh-hpc-2026/iam851/discussions) or create
    an [issue](https://github.com/unh-hpc-2026/iam851/issues).
  - [Email](mailto:kai.germaschewski@unh.edu) me for 1-on-1 help, or to set up a
    time to meet.

## Course Summary

Topics include: Elementary Numerical Methods, Algorithm Development and
Optimization, Parallel Programming Techniques, Distributed Processing over
Multiple CPUs, Code Management and Interfacing to Fortran/C Programming
Libraries, Data Visualization, Source Control.

## Course Description

This course gives an introduction into various areas of high-performance
computing, providing a basis for writing and working with high-performance
simulation codes.

The three main focus areas are "barely sufficient software engineering", basics
of high-performance and parallel programming, and visualization. Special topics
may include a modern HPC language like [Julia](http://julialang.org), specific
hardware architectures, automatic code generation and performance tuning, or
maybe some machine learning / deep learning / AI.

The section on software engineering will introduce basic tools and methods for
writing and maintaining portable code, selecting the right language for a task
at hand, and exploiting existing tools.

In the section on high-performance computing, we will review the history of HPC,
future directions and how it is now necessary to use parallelism at multiple
levels. Basic parallel programming models will be introduced, with a focus on
learning how to use MPI.

The last section will provide an overview of some of the visualization packages
available, with a focus on getting to know python/matplotlib and Visit. Other
topics are possible, like GPUs or data science / machine learning.

## Prerequisites

Enrollment in a CEPS graduate program, MATH 753, working knowledge of a
programming language (C, C++ or Fortran), or by permission of instructor.

## Reading

There is no required textbook for this class. Occasional readings assignments
will be posted and particpants are expected to finish those before class time.

Here are some books that might be useful:

- Writing Scientific Software -- A guide to good style, by Suely Oliveira \&
  David Stewart, Cambridge, 2006

- Parallel Programming, by Barry Wilkinson and Michael Allen, Pearson Prentice
  Hall, 2005

- Parallel Programming in C with MPI and OpenMP, by Michael J. Quinn, Michelle
  L. Flomenhoft, Elizabeth, A. Jones, McGraw-Hill, 2003

- Additional Resources:

  - To be added as we go / see the class notes

## Grading Policy

Regular homework and reading
[assignments](https://github.com/unh-hpc-2026/iam851/wiki/Assignments) will be
given and are expected to be completed by their due date. Late submissions may
receive partial credit. Attendance and participation in class discussions and in-class exercises
is required. Homework will be posted on the respective class web pages; it is
your responsibility to check for new assignments.

In addition there will be two projects: one midterm project and one final
project. Some projects may be divided into a number of subprojects which are
expected to be finished by their individual due date, before the due date of the
complete project. Some of the assignments will be designated as team efforts.

Every student registered for IAM 851 (as opposed to IAM 751) is expected to give
one presentation to the rest of the class during the course of the semester. You
will research one specific topic (from the area of HPC) and introduce it to the
rest of the class. Ideally, you will pick your topic yourself according to your
interests, in coordination with the instructor.

The final grade will be calculated as follows: Homework assignments and class
participation 30%, presentation 10%, midterm project: 30%, final project: 30%

## Class Policies

### Attendance

Class attendance is important for your learning. You are responsible for all
course assignments and meeting all deadlines unless exceptions are agreed upon
with the instructor ahead of time. Attendance in this course is mandatory.

In the event that a student needs accommodation for a religious or cultural
holiday/observance, that student is encouraged to make that request as early in
the semester as possible.

### Exceptional circumstances

For a variety of reasons, there may be times this semester when you cannot make
a deadline. If this happens, please contact me via email as soon as you can, let
me know how long of extension you will likely need. You do not need to share any
details of the circumstances with me; I want to respect your privacy.

### Grade records

You will be able to check your grades on myCourses; if you notice an error in a
recorded grade, please let me know as soon as you notice the error.

### Accessibility

According to the Americans with Disabilities Act (as amended, 2008), each
student with a disability has the right to request services from UNH to
accommodate their disability. If you are a student with a documented disability
or believe you may have a disability that requires accommodations, please
contact Student Accessibility Services (SAS); 227 Smith Hall, or
sas.office@unh.edu.

Accommodation letters are created by SAS with the student. Please follow-up with
your instructor as soon as possible to ensure timely implementation of the
identified accommodations in the letter. Faculty have an obligation to respond
once they receive official notice of accommodations from SAS, but are under no
obligation to provide retroactive accommodations.

For more information, contact SAS: 227 Smith Hall, www.unh.edu/sas,
603.862.2607, 711 (Relay NH) or sas.office@unh.edu

### Confidentiality and Mandatory Reporting of Sexual Violence or Harassment

The University of New Hampshire and its faculty are committed to assuring a safe
and productive educational environment for all students and for the university
as a whole. To this end, the university requires faculty members to report to
the university’s Title IX Coordinator (Bo Zaryckyj, Bo.Zaryckyj@unh.edu,
603-862-2930/1527 TTY) any incidents of sexual violence and harassment shared by
students. If you wish to speak to a confidential support service provider who
does not have this reporting responsibility because their discussions with
clients are subject to legal privilege, you can contact the SHARPP Center for
Interpersonal Violence Awareness, Prevention, and Advocacy at (603) 862-7233/TTY
(800) 735-2964. For more information about what happens when you report, how the
university treats your information once a report is made to the Title IX
Coordinator, your rights and reporting options at UNH (including anonymous
reporting options) please visit student reporting options . The uSafeUS app is
also available for students to keep reporting options and resources easily
accessible on their phones.

Help us improve our campus and community climate. If you have observed or
experienced an incident of bias, discrimination or harassment, please report the
incident by contacting the Civil Rights & Equity Office at
UNH.civilrights@unh.edu or TEL # (603) 862-2930 voice/ (603) 862-1527 TTY /
7-1-1 Relay NH, or visit the CREO website. Anonymous reports may be submitted.

### Credit Hour Policy

This syllabus reflects the federal definition of a credit hour, which entails a
minimum 3 hours of engaged time per week per credit over a 15-week semester.
Examples of engaged time include class time, assignments, examinations,
laboratories, participation in course-related experiences (attending a talk or
performance, speakers and events, fieldwork, etc.), conferences, and office
hours. Student work reflects intended learning outcomes and is verified through
evidence of student achievement. For more information, please see:
https://www.neche.org/wpcontent/uploads/2019/01/Affirmation-of-Compliance.pdf.

### Integrity

Working together on homework is encouraged. Obtaining solutions from other
sources after attempting on your own is also allowed. All sources should be
acknowledged.

Unless otherwise specified, the use of Automated Writing Tools, including
chatGPT and similar artificial intelligence (AI) tools, is prohibited in this
course, unless properly attributed.

### Emotional or Mental Health Distress

Your academic success and overall mental health are very important to me. Please
feel free to reach out to me (ideally, early). In addition, if, during the
semester, you find you are experiencing emotional or mental health issues,
please contact the University’s (PACS) (3rd floor, Smith Hall; 603-862-2090/TTY:
7-1- 1) which provides counseling appointments and other mental health services.
If urgent, students may call PACS M-F, 8 a.m.-5 p.m., and schedule an urgent
Same Day Appointment.

### Financial Literacy Resources

All students benefit from understanding their mindset about money, how to build
and use a personal budget, as well as understanding interest rates, loans,
insurance, investing, and more. UNH has wonderful free resources for students at
[Library Resource Guides](https://libraryguides.unh.edu/finlit), and every
student (and faculty!) can access [CA$H COURSE](http://www.cashcourse.org/) by
creating a free account. Find more information on the
[Financial Wellness](https://www.unh.edu/health/financial-wellness) site of
Health & Wellness.

### Curtailed Operations

If the university curtails operations due to weather, we will not hold in-person
activities for our safety and the safety of others. As soon as possible, I will
post an announcement on Canvas about due dates, any make-up work, and (if
applicable) any online options that may make sense depending on where we are in
the course. Please make sure you have access to the UNH Alert RAVE system. If
needed, sign up for RAVE Alerts at https://alert.unh.edu/.

### Class Recording Policy

Class lectures and activities may be recorded in order to make this course more
accessible, and recordings may be made available to students presently enrolled
in the class to assist in reviewing material and preparing for assessments.
Recordings are to be used for educational use/purposes only. Students may not
record class activities (including screenshots showing instructors and students)
without express permission from their instructor. If permission is granted,
student-initiated recordings may only be used for educational purposes in this
class and only during the period in which the student is enrolled in the class;
authorized student-initiated recordings may not be posted or shared in any
fashion outside of the class.
