<style>
  td {
    border: 1px solid black;
  }
</style>

# Course Information

* Title: {{- include.courseTitle }}
* Description: {{- include.courseDescription }}

# Student learning outcomes
{% include_relative relative.md %}

{% assign courseInfo=include.courseSLO | split: "\n" %}

{% for courseInfoLine in courseInfo %}
{{ courseInfoLine -}}
{% endfor %}

# Class/section Information

{% assign classInfo=include.classInfo | split: "\n" %}

{%- for classInfoLine in classInfo -%}
{{ classInfoLine -}}
{% endfor %}

# Professor information

* Tak Auyeung
* email: auyeunt@arc.losrios.edu
* phone: 916-484-8250
* office: Diane Bryant STEM Innovation Center (STEM) 316
{% assign officeHour=include.officeHour | split: "\n" %}
{%- for officeHourLine in officeHour %}
{{ officeHourLine -}}
{% endfor %}

# Important dates

* Check the [Academic Calendar](https://arc.losrios.edu/admissions/academic-calendar-and-deadlines) for important dates.
  * Last day to drop with a refund.
  * Last day to add (enroll) with a permission number.
  * Last day to withdraw with a 'W' notation.
* Check the [Final exam schedule](https://arc.losrios.edu/admissions/academic-calendar-and-deadlines/final-exams) for the date and time of the final exam.

# Presentation/Delivery Methods

The following are methods to distribute course content:

* Reading material: links from the Canvas shell.
* Lectures:
  * in-person: face-to-face (in-person)
    * the instructor may record lectures
    * attendance is still 100% required
    * if you think the recording is useful, please help remind the instructor to enable recording
  * synchronous online mode: live-streamed lectures and/or lab sessions
  * asynchronous online mode: recorded lectures
* interactive activities

# Regular effective contact and communication policy

To stay in touch with the instructor:

* utilize office hours
* email
* messaging using the learning management system or communication platform chosen by the instructor
* check Canvas course announcements

Expectation of time frame:

* a turn-around time of no more than 24 hours to messages sent between Monday midnight (0:00) and Friday midnight (0:00) excluding college holidays
* otherwise, a turn-around time of no more than 48 hours *during a semester*

For an in-person/synchronous class, to initiate communication with the instructor:

* office hours
* the instructor may schedule additional meeting time

# Accommodations

Individuals who can benefit from accommodations can do the following:

* Individuals who have already contacted the DSPS (Disability Services and Programs for Students)
  * Let the instructor know about the accommodation requirements as early as possible
* Individuals who have not already contacted the DSPS
  * Visit the DSPS in person or online:
    * ARC DSPS is located inside the Welcome and Support Center, North Entrance
    * [Email](mailto:arcdspsde@arc.losrios.edu)
    * [home page](https://arc.losrios.edu/student-resources/support-services/disability-services-and-programs-for-students)

Note that the instructor only provides accommodations according to DSPS officially approved ones. 

The instructor is available to discuss accommodation issues. Please visit the instructor during office hour or schedule an appointment for a discussion.

# Conduct

[Refer to the college's expectations of behavior and conduct](https://arc.losrios.edu/student-resources/office-of-student-conduct/expectations-of-behavior-and-conduct) for more details. Specifically, refer to the [guide](https://arc.losrios.edu/student-standards-of-conduct-guide/student-standards-of-conduct-guide/student-standards-of-conduct-guide).

The instructor's policy is to be consistent with the expectations from the [Office of Student Conduct](https://arc.losrios.edu/student-resources/office-of-student-conduct). The instructor **will report all cases of violations**. The *minimum* consequence of a violation is a score of zero assigned to the assessment that is in violation (in the case of academic dishonesty). In the case of violations that are not of the nature of academic dishonesty (such as bullying), The instructor can choose to remove the involved people from one or more class meeting(s). The Office of Student Conduct may incur additional consequences.

## Academic honesty/integrity

The basis of academic integrity policies is that the grade of an individual X should reflect the academic performance of X, and X alone. Furthermore, the performance assessment should also be conducted in a way that is consistent with the peers of X. Academic integrity also includes rule-compliance and truthfulness in all class-related activities, such as roll taking. 

For example, signing a roll sheet for someone is a violation of academic integrity. Affirming presence when a student is absent in an in-person class is also considered a violation of the academic integrity policy.

Most assessments include rules that are applied consistently to all participants. For example, an assessment (such as an exam) may allow the use of any handwritten or printed content on paper, but not electronic devices. Another assessment consistency is the start and end time of an assessment. Other rule examples include the start time, end time, and answer collection method of an assessment.

As such, a *violation* of the policy happens when the grade/score of an individual X does not reflect the academic performance of X, and X alone. Or, the participation of the assessment is inconsistent with the peers of X. 

## Non-integrity conduct expectations

Please refer to the college student conduct web page for a long list.

The bottom line is that a class, virtual or in-person, should be an environment that is free of elements that impede teaching and learning. In this context, the "elements" refer to human behaviors. This is a list of such behaviors:

* Chatting. 
* Devices.
* Other disruptions.
* Bullying.
* Threatening.

### Chatting

In most cases, chatting is disruptive to students who are around the chatters. No matter how quiet the chatters intend, chatting is still audible to those around the chatters.

Conversations that do not relate to class should not be in a classroom, period. 

Conversations that relate to class can be handled differently. For example, raising a hand and ask the professor instead of a neighboring peer may better serve the class as a whole.

### Devices

Sometimes, we forget to disable the notifications on a phone, and a notation can disrupt the concentration of people who are around us.

Most devices have a "do not disturb" feature, please make use of this feature! On a laptop computer, the speaker can usually be muted completely using a hot-key.

### Other disruptions

It is impossible to enumerate every single possible source of disruption. Please report to me if you experience disruption in class in case I do not realize it during class.

### Bullying

This college has zero tolerance of bullying. Note that bullying is the act of harming, intimidating, and/or coercing another person. Bullying can occur physically, but it can also occur in other forms.

If you experience or witness bullying, please try to collect as much evidence as possible, and report to the instructor or other college personnel as soon as possible.

Note the bullying can occur on-campus physically, but it can also occur via electronic means of communication. Cyber-bullying is not new, and it can harm individuals just as much. 

### Threatening

Although a component of bullying is threatening, this section addresses the threatening of a person who is not the second party. In other words, this section addresses the case of threatening when the "target" is a third person.

For example, a person within a Discord private server may mention something like "Sal is such a teacher's pet, I'd like to smack him in his face with he own laptop computer!" In this example, Sal may not even be on the private Discord server.

This is still a declared threat intention. Obviously, in many cases, the intended threat is not actually carried out. However, there is no way for others who read the message to differentiate whether this is just venting or a serious declaration.

Threats like these should also be reported for several reasons. First, these declarations can make others (not the "target") feel uncomfortable, even if the declared threat is not carried out. Second, in the event that the threat is actually serious, intervention can prevent the actual harm.

# Attendance/absences

Refer to "Attendance" on the college's web page on [College and Academic Regulations](https://arc.losrios.edu/2021-2022-official-catalog/while-you-are-here/college-and-academic-regulations). Specifically, read [the district's attendance requirements](https://arc.losrios.edu/shared/doc/board/regulations/R-2222.pdf) for a district-wide regulation.

Note that the district or college has no policy regarding what absences are "excused." This prompts [certain opinions](https://www.arcurrent.com/opinion/2013/12/02/arc-drop-policy-shows-no-mercy-for-students/) from certain students.

Attendance can be tracked by a variety of methods. The idea is that every student should be present and on-time. In a synchronous or in-person class, This means being late *can be counted as absent*. Not paying attention to attendance instruction *can be counted as absent*. Each student is responsible to arrange time and other resources to attend lectures and labs on-time, without interruptions/distractions, and pay attention for the entire scheduled duration.

## Why?

Attendance is positively correlated with performance and success in a class. While attendance by itself does not guarantee academic success, it is a *necessary* component. 

## Specific to in-person or synchronous online classes

Attendance is taken using specific means as mentioned by the instructor. Note that in a synchronous online class, just having a "presence" in a communication platform such as Zoom or Discord is insufficient to count as being present. The instructor can specify how attendance is taken *during* a lecture.

## Excessive absences

As per the district's regulation, the threshold to be counted as excessive is 6%. In a 16-week (full semester) class, each week is more than 6%. This means that a *total* of absences that is equivalent to one week's of lectures and/or lab activities is excessive.

If a 16-week class meets twice per week, this means that two absences adds up to $\frac{2}{16 \times 2}=\frac{1}{16}=6\frac{1}{4} \%>6 \%$. Note that this method of computing absence ratio is generous because it does not take college observed holidays and other non-instruction days into consideration.

## What about excused absences?

Neither the college (ARC) nor district (LRCCD) specifies what reasons of absence can be excused. California Education Code [does have a section](https://www.cde.ca.gov/ls/ai/tr/) regarding truancy and absences. This part of California Education Code [falls under Title 2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=EDC&sectionNum=48260.) which applies to "elementary and secondary education." College is considered "higher education" and falls under Title 5.

*As such*, the excuses mentioned in Title 2 (Section 48205) **do not apply** to colleges. 

## So what is Tak's policy regarding absences?

### Absence allowance

Each student can be absent according to roll taking mechanisms up to five (5) times before qualifying as excessively absent and dropped from class. This policy excludes the first three (3) class meetings. *Any absences* in the first three meetings of a class qualifies to be dropped (this is a part of district wide regulation).

Essentially, the absence allowance permits up to 5 absences throughout the entire semester. Note that $\frac{5}{2\times 16}=15.625\%$.

### Consideration of excuses

An absence *may be excused at the discretion of the instruction*. In terms of lecture and lab presence, most cases are not excused and handled by the aforementioned absence allowance.

The only case where excuse is significant applies to exams. The instructor expects each student to plan ahead and make sure that he/she does not miss an exam, or arrive late. This may include, but is not limited to: 

* Setting an alarm to wake up on time, 
* Planning for alternative transportation, 
* Accounting for worst case transit time, bus schedule disruption, etc.
* In the case of fasting, conserve energy, drink plenty of water. Fasting is not an acceptable excuse for being absent.
* Religious (regardless of religion) holidays and/or related activities.
* Family trips and/or related activities.

Sickness can potentially be excused if *all* the following criteria are met:

* Inform the instructor prior to the exam start-time in a reasonable time-frame.
* Send the instructor a doctor's note, prior to the exam. The doctor's note must meet all the following criteria:
  * On paper. The instructor will request to see the doctor's note on paper.
  * With the letter head of a licensed medical facility, including contact information of the doctor (verifiable phone number, full name, email, etc.) in case the instructor chooses to contact the doctor for verification.
  * Dated, *not* back-dated.
  * A range of days to be excused, where the range *starts* with the day on which the doctor writes the note. This means the note cannot back-date days excused.

At the discretion of the instructor, the instructor may exempt time sensitive criteria if the onset of the sickness is of an acute nature, such as acute appendicitis. The doctor must note that the medical condition has an acute nature as well as when the medical condition is diagnosed.

In the event that the instructor excuses a student from taking an exam on the scheduled day, the instructor may elect to administer an exam that is different from the one administered on the scheduled day. 

# Grading

## What is being assessed

An assessment can be a lab activity, a homework assignment, a Canvas activity, a quiz, or an exam. For each individual part (defined by the assessment). There are some dimensions of assessment:

### Prior knowledge and recall

This dimension is moot in an assessment that is open book and open notes.

### Analysis/critical thinking

This dimension quantifies the ability to understand and break down a question/problem into components that correlate with the *correct* symbols, definitions, techniques, procedures, and concepts introduced in class.

### Synthesis/Problem-solving

This dimension quantifies the ability to utilize symbols, definitions, concepts introduced in class to achieve an objectively defined goal.

### Performance

This dimension quantifies the familiarity and efficiency of performing critical thinking and problem-solving.

## Meanings of 0 to 4

Each assessment is reflected by a value ranging from 0/4 to 4/4. The following lists how 0/4 to 4/4 are determined in the context of the subject matter being assessed.

* 0/4, 0% (letter grade of F): 
  * no work is submitted, or
  * the submitted work shows, no evidence of 
    * the ability to analyze and think critically
    * the ability to synthesize or problem-solve
  * unless otherwise specified:
    * code that does not compile or assemble
* 1/4, 25% (letter grade of D):
  * the submitted work shows some, but insufficient, evidence of
    * the ability to analyze and think critically
    * the ability to synthesize or problem-solve
    * familiarity and efficiency do not matter when there is insufficient evidence of the abilities to analyze and/or synthesize
* 2/4, 50% (letter grade of C):
  * the submitted work shows sufficient evidence of
    * the ability to analyze and think critically
    * the ability to synthesize or problem-solve
  * the submitted work also shows evidence of
    * one or more conceptual mistakes
    * insufficient familiarity and/or efficiency
* 3/4, 75% (letter grade of B):
  * the submitted work provides sufficient evidence of
    * the ability to analyze and think critically
    * the ability to synthesize or problem-solve
    * complete and correct understanding of material
  * the submitted work also shows evidence of
    * one or more operational (as opposed to conceptual) mistakes and/or omissions
    * room for improvement in terms of familiarity and/or efficiency
* 4/4, 100% (letter grade of A):
  * the submitted work provides sufficient evidence of
    * the ability to analyze and think critically
    * the ability to synthesize or problem-solve
    * complete and correct understanding of material
    * operational correctness
    * excellent familiarity and/or efficiency

In order to convert an aggregated score $x$ (0/4 to 4/4) into a letter grade, the threshold is the midpoint between two letter grades. The following are the thresholds of a specific grade:

* F: $x < \frac{1}{8}=12.5\%$
* D: $12.5\% \le x < \frac{3}{8}=37.5\%$
* C: $37.5\% \le x < \frac{5}{8}=62.5\%$
* B: $62.5\% \le x < \frac{7}{8}=87.5\%$
* A: $87.5\% \le x$

## Late and makeup policy

In order for a submission to count to the final grade, it should be submitted on time. In *certain cases*, the instructor may agree to late submissions. The verifiable reasons of a late submission should be provided to the instructor prior to the due date, and preferably at the time the assessment is scheduled. *The instructor reserves the right not to allow/grade a late submission.*
 
Specific to exams, a makeup is possible *only if* all the following conditions are satisfied:

1. The instructor agrees to the makeup and the reason of the makeup.
1. The reason(s) of the makeup is/are satisfactorily verifiable.
1. The request of a makeup is prior to the scheduled date/time of the exam.

Again, *the instructor reserves the right not to allow a makeup of am exam.*

## Assessments

### Homework assignments and lab activities (20%)

These are low-impact activities designed to test the application or materials learned in class. Homework assignments typically have at least 2 days between assignment and collection, whereas lab activities are due at the end of a lab session.

A lab session is characterized by having the instructor being present to address questions.

### First Exam (20%)

This exam occurs at about $\frac{1}{3}$ through the semester. This exam uses the entire duration of a lecture session. 

### Second Exam (20%)

This exam occurs at about $\frac{2}{3}$ through the semester. This exam also uses the entire duration of a lecture session.

### Final exam (40%)

This exam occurs at the end of the semester. The instructor follows the policies regarding *when* to hold the final exam. For synchronous online classes and face-to-face classes, refer to the final exam schedule for the date and time of the final exam.

# Topics

<pre>
{% assign topics=include.topics | split: "\n" %}
{%- for topicLine in topics %}
{{ topicLine -}}
{% endfor %}
</pre>

<script>
  document.title = "Syllabus of {{include.courseTitle }} section {{ include.courseCode }} in {{ include.semester }}";
</script>
